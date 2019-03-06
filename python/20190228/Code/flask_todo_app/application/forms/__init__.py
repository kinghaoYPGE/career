from .auth import *
from .todo import *

def all():
    result = []
    forms = [auth, todo]

    for f in forms:
        result += f.__all__
    return result

__all__ = all()