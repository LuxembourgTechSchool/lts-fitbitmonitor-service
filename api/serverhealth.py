from flask import Blueprint, jsonify

bp = Blueprint('health', __name__, url_prefix='/health')

@bp.route('')
def health():
    return jsonify({'status': 'OK'})