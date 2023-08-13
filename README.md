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
A model that you desire to train can be added to the list of models in module - model_builder_[model_task].py <br>
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
To track experiments
[Documentation](https://mlflow.org/docs/latest/index.html)

#### Visualize and compare experiments
- mlflow ui

#### dagshub
Save experiments to remote server
[dagshub](https://dagshub.com/)

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=[your dagshub uri]

export MLFLOW_TRACKING_USERNAME=[dagshubusername]

export MLFLOW_TRACKING_PASSWORD=[dagshubpwd]

```

### AWS CICD with Github Actions
	#Steps
		1. Build docker image of the source code
		2. Push your docker image to ECR
		3. Launch Your EC2 
		4. Pull Your image from ECR in EC2
		5. Lauch your docker image in EC2

#### 1. Login to AWS console.

#### 2. Create IAM user
	IAM > user > add user > Attach policies directly >
	AmazonEC2ContainerRegistryFullAccess
	AmazonEC2FullAccess

	Go to created user > security credentials > create access keys > CLI > Download csv file

#### 3. Create ECR to store docker image
	ECR > Create a repository > repo name > create
	Copy repository uri and save it somewhere to be used later

#### 4. Create EC2 machine (Ubuntu) 
	EC2 > Launch instance > Name of instance > ubuntu > instance type
	create new key pair > name
	Allow https and http traffic from internet
	configure storage > launch instance
	click on instance id > security > security groups > edit inbound rules > custom tcp add your desired port (as in app.py)
	instance id > connect > terminal launched

#### 5. Install docker in EC2 machine
	#optional to update apt
	sudo apt-get update -y
	sudo apt-get upgrade
	#required
	curl -fsSL https://get.docker.com -o get-docker.sh
	sudo sh get-docker.sh
	sudo usermod -aG docker ubuntu
	newgrp docker
	
#### 6. Configure EC2 as self-hosted runner
    Github > repository > settings > actions > runners
	New self hosted runner > choose os > then run displayed command in EC2 one by one

	Name of runner in EC2 as self-hosted
	EC2 will be connected with github and will be listening for any changes to repository to trigger ci cd (see main.yaml)

#### 7. Setup AWS secrets at github
	Github > repository > settings > Secrets and variables > Actions > New repository secret

    AWS_ACCESS_KEY_ID= from downloaded csv file
    AWS_SECRET_ACCESS_KEY= from downloaded csv file
    AWS_REGION = [region]
    AWS_ECR_LOGIN_URI = [uri - that we copied in step 3]
    ECR_REPOSITORY_NAME = [ecr repo name]
	This is done so that github can connect to AWS ECR inorder to build and store the docker image


### Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
opensource.org/licenses/mit-license