from . import utils_bp
from datetime import datetime


@utils_bp.app_template_filter('human_time')
def human_time(dt):
    return datetime.strftime(dt, '%a, %b %Y %H:%M:%S')


@utils_bp.app_template_filter('in_seconds')
def in_seconds(dt):
    return datetime.timestamp(dt)
