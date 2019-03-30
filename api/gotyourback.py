from flask import Blueprint, request, jsonify, abort
import logging 

import csv
import datetime

bp = Blueprint('gotyourback', __name__, url_prefix='/wegotyourback')

@bp.route('/gyro', methods=['POST'])
def gyro():
    data = request.get_json(force=True)

    filename = datetime.datetime.now().strftime('data/%Y%M%d-%H%M:%S-gyro.csv')
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        for d in data['gyro']:
            print(d)
            writer.writerow([
                d['timestamp'],
                d['x'],
                d['y'],
                d['z']
            ])
        logging.info("Gyro Data saved to {}".format(filename))

    return jsonify( {'message': 'Data saved successfully'} )



