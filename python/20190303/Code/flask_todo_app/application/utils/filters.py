from datetime import datetime
from  . import utils_bp

@utils_bp.app_template_filter('human_time')
def human_time(dt):
  return datetime.strftime(dt, '%a, %b %Y %H:%M:%S')