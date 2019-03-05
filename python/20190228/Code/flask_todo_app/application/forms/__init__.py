from .auth import *

def all():
    result = []
    forms = [auth]

    for f in forms:
        result += f.__all__
    return result

__all__ = all()