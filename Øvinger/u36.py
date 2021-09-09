''' Jaok. I guess we're doing this?
REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'''
import time
import hjelpere as u

UKE = 36
DEBUG = True


def test_opg(crib: dict) -> None:
    """Så dette er _litt_ mer komplisert enn det
    øvingen legger tilrette for. ..eller hva som er hensiktsmessig."""
    timing, errlog = {}, []
    for oppgave in crib:
        start = time.time()
        call = oppgave[0]
        print(call.__name__+'\t', end='')
        for problem in oppgave[1]:
            try:
                assert call(*problem[0:-1]) == problem[-1]
            except AssertionError:
                if DEBUG is True:
                    errlog.append(
                        # as an aside - this unwrap is stupid
                        f'F {call.__name__}\t{call(*problem[0:-1])}' +
                        f' != {problem[-1]}')
                    print('F', end='')
                else:
                    print('F', end='')
            else:
                print('.', end='')
            finally:
                timing[call.__name__] = (time.time()-start)
        print()  # Force newline.
    if errlog != []:
        for log in errlog:
            print(log)
    if DEBUG is True:
        print(timing)


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
    """REEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    Does it with-a smoothbrain math"""
    h, m, s = 0, 0, 0
    h = int(num/60/60)
    m = int(num/60 - h*60)
    s = int(num - h*60*60 - m*60)
    return (h, m, s)


def o8_2(num: int) -> tuple:
    """REEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    Does it with a loopeti-loop"""
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
    ovinger = [o1, o2, o3, o4, o5, o6, o7, o8, o8_2, o9, o10]
    oppgaver = [
        [(30, 10, 40), (-30, 10, -20), (0, 0, 0)],
        [(3, 9, 27), (-30, 10, -300), (0, 9, 0)],
        [(3, 9, 10, 120), (-30, 10, 4, -80), (2, 9, 3, 33)],
        [(5, 6, 7, 8, -26), (0, 0, 7, 8, -56), (5, 6, -7, 8, 86)],
        [(2.00, 12.5664), (100.64, 31819.3103), (150.00, 70685.7750)],
        [(5, 6, 7, 8, (5, 8)), (3, 0, 7, 8, (0, 8)), (5, 6, -7, 8, (-7, 8))],
        [(10, 85, 70.833), (2, 92, 15.333), (22, 67, 122.833)],
        [(556, (0, 9, 16)), (1, (0, 0, 1)), (140153, (38, 55, 53))],  # o8
        [(556, (0, 9, 16)), (1, (0, 0, 1)), (140153, (38, 55, 53))],  # o8_2
        [(500, 35.0, 12.286), (2254, 124.4, 18.119), (4554, 464.6, 9.802)],
        [(30, 60), (110, 220), (7, 14)]
    ]

    test_opg(zip(ovinger, oppgaver))
