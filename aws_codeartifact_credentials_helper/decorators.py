from functools import wraps

from . import get_logger


def try_except(message: str):
    def wrap(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                get_logger().error(message if message else 'Something went wrong', exc_info=e)

        return wrapper

    return wrap
