from .user import *

def all():
    result = []
    models = [user]

    for m in models:
        result += m.__all__
    return result

__all__ = all()