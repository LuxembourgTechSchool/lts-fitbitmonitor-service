from flask import Blueprint, request, jsonify, abort

from app import insurance_grade_model as model

bp = Blueprint('insurance', __name__, url_prefix='/insurance')

fields = [
    'calories',
    'steps',
    'distance',
    'floors',
    'minutes_sitting',
    'minutes_of_slow_activity',
    'minutes_of_moderate_activity',
    'minutes_of_intense_activity',
    'calories_activity'
]

@bp.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    if set(fields) != data.keys():
        abort(500)

    x = []
    for field in fields:
        x.append( data[field] )

    prediction = model.predict([x]).tolist()

    return jsonify( {'prediction': prediction[0]} )
