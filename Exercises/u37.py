import hjelpere as u

__UKE__ = 37


# Oppgave 1
def skriv_ting(x: int = 3, y: int = 12.5) -> None:
    stmt = [
        f'The rabbit is {x}.',
        f'The rabbit is {x} years old.',
        f'{y} is average.',
        f'{y} * {x}',
        f'{y} * {x} is {x*y}'
    ]
    for _ in stmt:
        print(_)
    return None


# Oppgave 2
def flyttall_printer() -> None:
    while True:
        try:
            print(float(input()))
        except ValueError:
            print('Ai. Funker bare med tall, as. Prøv igjen.')
        else:
            break
    return None


# Oppgave 3
def repeat(s: str, n: int) -> str:
    """Return s repeated n times; if n is negative, return the empty string

    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    ''
    >>> repeat('no', -2)
    ''
    >>> repeat('yesnomaybe', 3)
    'yesnomaybeyesnomaybeyesnomaybe'
    """
    if isinstance(s, str):  # eh. Hvorfor ikke.
        return s*n
    else:
        return ''


# Oppgave 4
def wat() -> None:
    # latskapen, as
    stmt = 'I\'m a programmer. I can count\nOne\nTwo\nThree'
    print(stmt)


# Oppgave 5
def is_string_empty(string: str) -> bool:
    """Takes a string and returns True if string is empty, false if not, *or*
    if an invalid argument was given."""
    if isinstance(string, str):  # GET REKT, 0
        return not bool(string)

    return False


# Oppgave 6
@u.fprint
def o6_runner() -> list:
    """Eh. Trengte at det passet inn i resten"""

    def format_string(value: str, separator: str, end: str) -> str:
        """Takes a string and composes it in a two-clause statement with
        formatting given by
        separator: Separates the two clauses.
        end: Terminates the statement."""
        # Det mellomrommet er et irritasjonsmoment..
        stmt = f'This\'s a string value: `{value}`{separator}' + \
            f'Its length is {len(value)}{end}'
        return stmt

    return [format_string('Test', x, y) for x, y in
            zip(['\n', '!', '...', '?'], ['!', '?', '...'])]


# Oppgave 7
def antatt_forutsigbarhet() -> None:
    """Se Week 37.pdf"""
    try:
        assert (True and not False) is True, 1  # Sann
        # " True and not false " vil generere en NameError
        # sånn off the top of my dome.
        assert (True or True and False) is True, 3  # Sann
        assert (not True or not False) is True, 4
        assert (True or 0) is True, 4  # Sann; 0 er False
        assert (52 < 52.3) is True, 5  # Sann
        assert (1+52 < 52.3) is False, 6  # False
        assert (4 != 4.0) is False, 7  # Usann. Numerisk dritt.
    except AssertionError as e:  # JA JEG SA JEG IKKE VILLE MEN SE PÅ MEG NÅÅÅÅ
        print(f'Lol på deg @ {e}')
        return False
    else:
        return True


# Oppgave 8
def o8(full: bool, empty: bool) -> bool:
    #return full ^ empty  # Medium sized Oof-menu, hold the garlic
    return not ( full and empty )


# Oppgave 9
@u.fprint
def reverse_string(string: str) -> str:
    return string[::-1]


# Oppgave 10
def slicer_slices_1(streng: str) -> str:
    """Venter på avklaring fra studass
    Avklaring på siste sats uteblir. Fra hvilken streng skal lengden vurderes?
    Alt 1 - Strengoperasjon. Slicer ut *mellom* og fjerner.
    10 bytecodes, men ene er CALL_METHOD"""
    if len(streng) > 2:
        return streng.replace(streng[2:-2], '')
    return ''


def slicer_slices_2(streng: str) -> str:
    """Alt 2" - More schneidmaschine. 
    Slicer to første, to siste og komponerer
    12 bytecodes"""
    if len(streng) > 2:
        return streng[:2] + streng[-2:]
    return ''


if __name__ == '__main__':
    # ... skrive tester her ble mer ork.
    # UwU
    pass
