from .auth import auth_bp
from .main import qa_bp
from .ajax import ajax_bp

all_bp = [auth_bp, qa_bp, ajax_bp]
