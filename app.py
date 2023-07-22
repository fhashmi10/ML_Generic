"""App module for flask app exposing endpoints"""
from flask import Flask, request, render_template

from src import logger
from src.pipeline.prediction_pipeline.model_prediction_pipeline import ModelPredictionPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    """root API endpoint"""
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """predict endpoint"""
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
        logger.error("Error in prediction %s", ex)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
