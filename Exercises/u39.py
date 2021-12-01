import calendar as cal
import math
import hjelpere as u

__UKE__ = 39


def o1():
    v1 = math.floor(-2.8)
    v2 = abs(round(-4.3))
    v3 = math.ceil(math.sin(34.5))
    print(v1, v2, v3)


@u.fprint()
def o2(a, b, alpha):
    return (a*b*math.sin(alpha))/2


@u.fprint()
def o3(i):
    v1 = math.cos(2*i)
    v2 = -2*math.sin(2*i)
    v3 = -4*math.cos(2*i)
    return (v1, v2, v3)


@u.fprint()
def o4():
    print(dir(cal), '\n')
    for _ in range(2021, 2025):
        if cal.isleap(_):
            print(_, 'is a leap year')
            break
    leap_year = []
    for _ in range(2000, 2051):
        if cal.isleap(_):
            leap_year.append(_)


if __name__ == '__main__':
    o1()
    o2(a=7, b=(4*math.sqrt(3)), alpha=(math.pi/3))
    o3(math.pi)
    o4()
