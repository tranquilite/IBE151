"""Jaok. I guess we're doing this?
REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"""

import hjelpere as u


__UKE__ = 35


@u.fprint
def o1() -> float:
    try:
        temp = 24
        temp = temp * 1.8 + 32
        assert temp == 75.2
    except AssertionError:
        return 'I GUESS DU IKKE ER LIKE FLINK I HODEREGNING SOM DU TRODDE'
    else:
        return temp


@u.fprint
def o2() -> str:
    """For each of the following expressions, in which order are the subexpressions evaluated?
    Check yourself using Python.
    6 * 3 + 7 * 4
    5 + 3 / 4
    5 -2 * 3 ** 4
    ... PEMDAS left to right..."""
    try:
        assert (6 * 3 + 7 * 4) == 46
        assert (5 + 3 / 4) == 5.75
        assert (5 - 2 * 3 ** 4) == -157
    except AssertionError:
        return 'LOOOOOOOOOOOL PÅ DEG'
    else:
        return 'jaok'


@u.fprint
def o3() -> str:
    """Calculations:
    Create a new variable x, and assign it the value 10.5.
    Create a new variable y, and assign it the value 4.
    Sum x and y, and make x refer to the resulting value.
    After this statement has been executed, what are the values of x and y?"""
    try:
        x = 10.5
        y = 4
        x = x + y
        assert x == 14.5
        assert y == 4
    except AssertionError:
        return 'Har du glemt noe?'
    else:
        return 'jaok'


def o4() -> list:
    """fuck it. Jeg er allerede investert.
    Which of the following expressions results in SyntaxErrors?"""
    expr = ['6 * -----8'
            '8 = people'  # ..denne.. DENNEEEEEE
            '((((4 ** 3))))'
            '(-(-(-(-5))))'
            '4 += 7 / 2'  # .. *kremt* .. og denne
            ]

    return expr


@u.fprint
def o5() -> str:
    """What is the result of following calculations?"""
    calc = ['((((6+4)*2)-10)//2)-4*2',
            '2 + 17 / 2 * 3',
            '5*2//3',
            '19 % 4 + 15 / 2 *3',
            '17 / 2 % 2 * 3**3',
            '2**3**2'
            ]
    crib = [-3, 27.5, 3, 25.5, 13.5]
    try:
        for exp in zip(calc, crib):
            assert eval(exp[0]) == exp[1]
    except AssertionError:
        return 'bleeeeeeeeh'
    else:
        return 'jaok'


if __name__ == '__main__':
    u35_ovingsoppgaver = [o1, o2, o3, o4, o5]
    for oppgave in u35_ovingsoppgaver:
        oppgave()
