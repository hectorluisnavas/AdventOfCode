import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def measure_time(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Function: %r took %2.4f seconds.' % (func.__name__, end - start))
        return result
    return measure_time