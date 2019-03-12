from flask import Flask
from waitress import serve
from logging.config import dictConfig

from sklearn.externals import joblib

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
            'filename': 'logs/app.log',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})

# Models
insurance_grade_model = joblib.load('model/model.joblib').set_params(n_jobs=1)

def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    from api import serverhealth
    app.register_blueprint(serverhealth.bp)

    from api import insurance
    app.register_blueprint(insurance.bp)

    app.logger.info('App has been created.')

    return app

