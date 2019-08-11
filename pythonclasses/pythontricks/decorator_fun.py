import functools

def exclamation(func):
    @functools.wraps(func)
    def wrapper():
        original_func = func()
        modified_func = original_func + '!!!'
        return modified_func
    return wrapper


def period(func):
    @functools.wraps(func)
    def wrapper():
        original_func = func()
        modified_func = original_func + '...'
        return modified_func
    return wrapper


def allcap(func):
    @functools.wraps(func)
    def wrapper():
        original_func = func()
        modified_func = original_func.upper()
        return modified_func
    return wrapper

@allcap
@exclamation
@period
def helloworldfunc():
    """This functions returns the string 'hello world'"""
    return "hello world"

print(helloworldfunc())
print(helloworldfunc.__name__)
print(helloworldfunc.__doc__)
