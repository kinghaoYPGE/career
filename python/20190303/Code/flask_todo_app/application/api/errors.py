from flask import jsonify, make_response
from . import api_bp

@api_bp.errorhandler(400)
def bad_request(error):
  return make_response(jsonify({'error': 'Bad Request'}), 400)

@api_bp.errorhandler(401)
def unauthorized(error):
  return make_response(jsonify({'error': 'Unauthorized'}), 401)

@api_bp.errorhandler(403)
def forbidden(error):
  return make_response(jsonify({'error': 'Forbidden'}), 403)

@api_bp.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error': 'Not found'}), 404)

@api_bp.errorhandler(500)
def internal_server_error(error):
  return make_response(jsonify({'error': 'Internal Server Error'}), 500)