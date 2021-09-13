def fprint(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        if isinstance(ret, list):
            for _ in ret:
                print(_)
        else:
            print(f'>{func.__name__} {ret}')
        return ret
    return wrapper
