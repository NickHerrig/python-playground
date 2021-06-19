from functools import wraps

def coroutine(func):
    """primes 'func' coroutine"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer
