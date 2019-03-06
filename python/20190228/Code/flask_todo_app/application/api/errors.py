from flask import jsonify

from . import api_bp

@api_bp.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400


@api_bp.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized'}), 401


@api_bp.errorhandler(403)
def forbidden(error):
    return jsonify({'error': 'Forbidden'}), 403


@api_bp.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404


@api_bp.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 404