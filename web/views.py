"""App module for flask app exposing endpoints"""
import os
import requests
from flask import request, render_template
from flask_cors import cross_origin
from jinja2 import TemplateNotFound

from web import app
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
    except requests.Timeout:
        return render_template('page-error.html', error="Timeout occured!")
    except TemplateNotFound:
        return render_template('page-error.html', error="Page not found!")
    except Exception:
        return render_template('page-error.html', error="Server error!")


@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def train():
    """Train endpoint"""
    try:
        os.system("python main.py")
        return "Training done successfully!"
    except requests.Timeout:
        return render_template('page-error.html', error="Timeout occured!")
    except TemplateNotFound:
        return render_template('page-error.html', error="Page not found!")
    except Exception:
        return render_template('page-error.html', error="Server error!")


@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    """Predict endpoint"""
    try:
        if request.method == 'GET':
            return render_template('index.html')
        feature_identifier = "col_"
        features_dict = {}
        for key, val in request.form.items():
            if key.startswith(feature_identifier):
                feature=key.split(feature_identifier)[1]
                features_dict.update({feature: val})

        predict_pipeline = ModelPredictionPipeline()
        results = predict_pipeline.predict(features_dict=features_dict)
        return render_template('index.html', results=results)
    except requests.Timeout:
        return render_template('page-error.html', error="Timeout occured!")
    except TemplateNotFound:
        return render_template('page-error.html', error="Page not found!")
    except Exception:
        return render_template('page-error.html', error="Error in Prediction!")
