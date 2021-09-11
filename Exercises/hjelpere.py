def fprint(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        print(f'>{func.__name__} {ret}')
        return ret
    return wrapper
