from math import factorial
import hjelpere as u

__UKE__ = 41


def o1():
    for phenotype in ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']:
        print(phenotype)


def o2():
    alkaline_earth_metals = [
        [4, 9.012],  # "beryllium"
        [12, 24.305],  # "magnesium"
        [20, 40.078],  # "calcium"
        [38, 87.62],  # "strontium"
        [56, 137.327],  # "barium"
        [88, 226]  # "radium"
    ]

    def o2_sub1():  # fug
        for metal in alkaline_earth_metals:
            for properties in metal:
                print(f'{properties[0]}\n{properties[1]}\n')

    number_and_weight = [pair for metal in alkaline_earth_metals for pair in metal]
    print(number_and_weight)


def o3(rat_1: list, rat_2: list) -> None:
    """You are given two lists, rat_1 and rat_2, that contain the daily weights of
    two rats over a period of ten days. Assume the rats never have exactly
    the same weight."""

    # Sliter hvis len(rat_1) != len(rat_2)
    for _ in enumerate(zip(rat_1, rat_2)):
        if _[1][0] > _[1][1]:
            print(f'Rat 1 weighed more than rat 2 on day {_[0]+1}')
        else:
            print(f'Rat 1 weighed less than rat 2 on day {_[0]+1}')

    # Sliter hvis len(rat_1) eller len(rat_2) != 10
    for i in range(10):
        if rat_1[i] > rat_2[i]:
            print(f'Rat 1 weighed more than rat 2 on day {i+1}')
        else:
            print(f'Rat 1 weighed less than rat 2 on day {i+1}')


def o4():
    for line in range(7):
        print('T'+'T'*line)


def o5():
    for line in reversed(range(7)):
        print(' '*int(round(line/2))+''+'T'*(7-line))


@u.fprint()
def o6(numbers: list) -> list:
    """Write a function that finds a maximum value and a minimum value in
    the list without using in-build functions max, min. Return a list with
    both values: [minValue, maxValue]"""
    minmax = [0, 0]
    for number in numbers:
        if number < minmax[0]:
            minmax[0] = number
        if number > minmax[1]:
            minmax[1] = number
    return minmax


@u.fprint()
def o7(number: int) -> int:
    """Write a function that counts the total number of digits it the number
    without using len method"""
    # Because fuck you, that's why :)
    return list(enumerate([*str(number)]))[-1][0] + 1


@u.fprint()
def o8(number) -> int:
    """Write a function that reverses a given integer number."""
    return int(str(number)[::-1])


@u.fprint()
def o9(number: int) -> int:
    """Write a function that finds a factorial of a given number"""
    fac = 1
    for _ in range(1, number+1):
        fac *= _
    return fac


def o10(number: int) -> bool:
    """Write a python program to check given number is prime or not (only for
    positive numbers)"""
    pass


if __name__ == '__main__':
    o8(1234)
