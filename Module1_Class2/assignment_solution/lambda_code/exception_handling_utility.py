from functools import wraps
import traceback

def try_except_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Error in function {func.__name__} - {e}")
            print(traceback.format_exc())
            raise
    return wrapper