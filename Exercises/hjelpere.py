def fprint(silent=True):
    """fprint - Nå med muligheten til å holde mer kjeft
    :param silent - bool for å droppe unødvendige tilleggsmeldinger.
    :Funfact - Det er en feil her et sted. Se om du kan finne den ;)"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            if isinstance(ret, list):
                for _ in ret:
                    print(_)
            else:
                if silent is False:
                    print(f'>{func.__name__} {ret}')
                else:
                    print(ret)
            return ret
        return wrapper
    return decorator


def ask_input(*, query, types):
    """Er du lei av alle oppgavene som vil at du skal bruke evig mange input()?
    Look no further! Her er satan sjæl.
    :*query og types er påkrevd*
    :param query - tuple med setninger for input(<prompt>)
    :param types - tuple med ønsket type fra hver spørring.
        Må være like lang som query"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            inputs = []
            for _ in range(len(query) if len(query) == len(types) else 0):
                while True:
                    try:
                        sends = types[_](input(query[_] + ': '))
                    except ValueError:
                        print('Input is not valid. ',
                              f'Expected {types[_].__name__}')
                    else:
                        if len(query) == 1:
                            inputs = sends
                        else:
                            inputs.append(sends)
                        break
            return func(*args, **{'inputs': inputs, **kwargs})
        return wrapper
    return decorator
