import zlib
from functools import wraps

def compression_middleware(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        b_request = zlib.decompress(request)
        b_responce = func(b_request, *args, **kwargs)
        return zlib.compress(b_responce)
    return wrapper


def encryption_middleware(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        b_responce = func(request, *args, **kwargs)
        return b_responce
    return wrapper