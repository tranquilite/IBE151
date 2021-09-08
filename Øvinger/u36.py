''' Jaok. I guess we're doing this?
REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'''
import hjelpere as u

UKE = 36
DEBUG = True

def test_opg(crib: dict) -> None:
    for oppgave in crib:
        call = crib[oppgave][0]
        print(oppgave+' ', end='')
        for problem in crib[oppgave][1]:
            try:
                #print(problem[0:-1])
                assert call(*problem[0:-1]) == problem[-1]
            except AssertionError as e:
                if DEBUG is True:
                    print(f'\nF {call(*problem[0:-1])} != {problem[-1]}')
                else:
                    print('F', end='')
            else:
                print('.', end='')
        print()


def o1(num1: int, num2: int) -> int:
    return num1 + num2


def o2(num1: int, num2: int) -> int:
    return num1 * num2


def o3(num1: int, num2: int, num3) -> int:
    return (num1 + num2) * num3


def o4(num1: int, num2: int, num3: int, num4: int) -> int:
    return num1 * num2 - num3 * num4


def o5(radius: float) -> float:
    return round(3.14159 * radius**2, 4)


def o6(a: int, b: int, c: int, d: int) -> tuple:
    return (min(a, b, c, d), max(a, b, c, d))


def o7(spent: int, trip: int) -> float:
    return round(spent*trip/12, 3)


def o8(num: int) -> tuple:
    """REEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"""
    h, m, s = 0, 0, 0
    while num != 0:
        s += 1
        num -= 1
        if s == 60:
            m += 1
            s = 0
        if m == 60:
            h += 1
            m = 0
    return (h, m, s)


def o9(dis: int, used: float) -> float:
    return round(dis/used, 3)


def o10(time: int) -> int:
    """takes time in min"""
    speed_ratio = 2
    return time * speed_ratio


if __name__ == '__main__':
    oppgaver = {
        'o1': [o1, [(30, 10, 40), (-30, 10, -20), (0, 0, 0)]],
        'o2': [o2, [(3, 9, 27), (-30, 10, -300), (0, 9, 0)]],
        'o3': [o3, [(3, 9, 10, 120), (-30, 10, 4, -80), (2, 9, 3, 33)]],
        'o4': [o4, [(5, 6, 7, 8, -26), (0, 0, 7, 8, -56), (5, 6, -7, 8, 86)]],
        'o5': [o5, [(2.00, 12.5664), (100.64, 31819.3103), (150.00, 70685.7750)]],
        'o6': [o6, [(5, 6, 7, 8, (5, 8)), (3, 0, 7, 8, (0, 8)), (5, 6, -7, 8, (-7, 8))]],
        'o7': [o7, [(10, 85, 70.833), (2, 92, 15.333), (22, 67, 122.833)]],
        'o8': [o8, [(556, (0, 9, 16)), (1, (0, 0, 1)), (140153, (38, 55, 53))] ],
        'o9': [o9, [(500, 35.0, 12.286), (2254, 124.4, 18.119), (4554, 464.6, 9.802)]],
        'o10': [o10, [(30, 60), (110, 220), (7, 14)]]
    }

    test_opg(oppgaver)
