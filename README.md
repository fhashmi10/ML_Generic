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

### MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

#### cmd
- mlflow ui

#### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=[your dagshub uri] \
MLFLOW_TRACKING_USERNAME=[dagshubusername] \
MLFLOW_TRACKING_PASSWORD=[dagshubpwd] \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=[your dagshub uri]

export MLFLOW_TRACKING_USERNAME=[dagshubusername]

export MLFLOW_TRACKING_PASSWORD=[dagshubpwd]

```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with below access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: [uri]

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = [uri]

    ECR_REPOSITORY_NAME = [repo-name]


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
opensource.org/licenses/mit-license