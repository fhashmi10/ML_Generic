"""App module for flask app exposing endpoints"""
import os
import requests
from flask import request, render_template
from flask_cors import cross_origin
from jinja2 import TemplateNotFound

from web import app
from src import logger
from src.pipeline.prediction_pipeline.model_prediction_pipeline import ModelPredictionPipeline


@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
@cross_origin()
def index(path):
    """App main route and generic routing"""
    try:
        if not path.endswith('.html'):
            path += '.html'
        return render_template(path)
    except TemplateNotFound:
        return render_template('page-404.html'), 404
    except Exception:
        return render_template('page-500.html'), 500


@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def train():
    """Train endpoint"""
    try:
        os.system("python main.py")
        return "Training done successfully!"
    except requests.Timeout as ex:
        logger.exception("Timeout occured %s", ex)
        raise ex
    except Exception as ex:
        logger.exception("Error in training %s", ex)
        return "Exception occured: Check logs"


@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    """Predict endpoint"""
    try:
        if request.method == 'GET':
            return render_template('index.html')
        features_dict = {}
        features_dict.update({
            "gender": request.form.get('gender'),
            "race_ethnicity": request.form.get('ethnicity'),
            "parental_level_of_education": request.form.get('parental_level_of_education'),
            "lunch": request.form.get('lunch'),
            "test_preparation_course": request.form.get('test_preparation_course'),
            "reading_score": float(request.form.get('writing_score')),
            "writing_score": float(request.form.get('reading_score'))
        })

        predict_pipeline = ModelPredictionPipeline()
        results = predict_pipeline.predict(features_dict=features_dict)
        return render_template('index.html', results=results)
    except Exception as ex:
        logger.exception("Error in prediction %s", ex)
        return render_template('index.html', results="Exception occured: Check logs")
