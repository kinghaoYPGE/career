from flask import render_template
from . import utils_bp

@utils_bp.app_errorhandler(403)
def forbidden(error):
  return render_template('403.html'), 403

@utils_bp.app_errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

@utils_bp.app_errorhandler(500)
def internal_server_error(error):
  return render_template('500.html'), 500

