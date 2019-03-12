from flask import Flask
from waitress import serve
import os
from logging.config import dictConfig

from sklearn.externals import joblib

APPLICATION_LOG     = 'logs/app.log'
APPLICATION_MODEL   = 'model/model.joblib'

ENV_LOG = os.environ.get('APP_LOG')
if ENV_LOG:
    APPLICATION_LOG = ENV_LOG

ENV_MODEL = os.environ.get('APP_MODEL')
if ENV_MODEL:
    APPLICATION_MODEL = ENV_MODEL

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': APPLICATION_LOG,
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})

# Models
insurance_grade_model = joblib.load(APPLICATION_MODEL).set_params(n_jobs=1)

def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    from api import serverhealth
    app.register_blueprint(serverhealth.bp)

    from api import insurance
    app.register_blueprint(insurance.bp)

    app.logger.info('App has been created.')
    app.logger.info(' APPLICATION_LOG   : {}'.format(APPLICATION_LOG))
    app.logger.info(' APPLICATION_MODEL : {}'.format(APPLICATION_MODEL))

    return app

