# ML Generic

A generic implementation of machine learning model building tool

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.

```bash
pip install -r requirements.txt
```

## Usage

### Data
The data that you desire to train on can be stored under data folder in root.<br>
New data file path needs to be configured in config.yaml<br>
New target column needs to be configured in config.yaml

### Model Training
A model that you desire to train can be added to the list of models in module - model_builder.py <br>
Model parameters can be configured in params.yaml<br>
Evaluation metric can be configured in params.yaml<br>
python main.py to run all pipelines (except prediction).

### Model Prediction
Prediction pipeline can be updated based on your project requirements.<br>
Current prediction code returns an output integer prediction.

### UI
Modify index.html based on your project requirements.<br>
python app.py to run flask app.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
opensource.org/licenses/mit-license