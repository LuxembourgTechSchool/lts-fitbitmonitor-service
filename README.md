# LTS Fitbit Monitor Service

This web application shows how to do a simple web service that serves predictions based on a previously trained model.
This application is meant to be modified to your needs.

**Note:** Trained models are not provided.

# Example API Calls:

Examples using [httpie](https://httpie.org):

    http POST localhost:8080/insurance/predict steps=900 calories=1900 floors=2 minutes_sitting=1300 minutes_of_slow_activity=40 minutes_of_moderate_activity=10 minutes_of_intense_activity=100 calories_activity=200 distance=10

    http POST localhost:8080/insurance/predict steps=900 calories=2900 floors=2 minutes_sitting=1300 minutes_of_slow_activity=40 minutes_of_moderate_activity=10 minutes_of_intense_activity=100 calories_activity=200 distance=10

    http POST localhost:8080/insurance/predict steps=900 calories=2900 floors=2 minutes_sitting=1300 minutes_of_slow_activity=40 minutes_of_moderate_activity=10 minutes_of_intense_activity=100 calories_activity=200 distance=0

# Getting Started (DEV)

Create a virtual environment using Python 3:

    python -m venv venv3

Activate the environment:

    source venv3/bin/activate

Install dependencies:

    pip install -r requirements.txt

## Run the server:

### Option A: Using Flask

    flask run

## Option B: Using Waitress

    waitress-serve app:create_app