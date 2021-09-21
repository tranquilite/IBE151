import hjelpere as u
import datetime

__UKE__ = 38


def warm_up():
    name, age = '', 0
    year = datetime.date.today().year
    while True:
        try:
            name = input('Please enter your name: ')
            age = int(input('Please enter your age'))
            if age == 0:
                raise ValueError  # Super lazy. *Super*
        except ValueError:
            print('Nuh-Uh. Age\'s a number')
        else:
            if age >= 100:
                print(f'Hi, {name}. {year} I guess?')
            else:
                print(f'Hi, {name}! You\'re born in {year-age}, ' +
                      f'and you\'ll reach 100 years in {(year-age)+100}')


@u.fprint
def even_or_odd(x):
    return 'Even' if x % 2 == 0 else 'Odd'


@u.ask_input(query=('Please enter a number',), types=(int,))
@u.fprint(silent=True)
def positive_negative_or_zero(inputs):
    return 'Negative' if inputs < 0 else 'Positive' if inputs > 0 else 'Zero'


def display_number_01():
    """Oh fug. The number of lines is too damn high"""
    numbers = [0, 0, 0]
    for _ in range(0, 3):
        while True:
            try:
                numbers[_] = int(input(f'Enter the {_+1}. number: '))
            except ValueError:
                print('Nuh-Uh')
            else:
                break
    numbers = sorted(numbers)+sorted(numbers)[::-1]
    for num in numbers:
        print(num, end=' ')


def display_number_02():
    """Oja. Oppgaven bryr seg ikke om midterste tallet..."""
    numbers = [0, 0, 0]
    for _ in range(0, 3):
        numbers[_] = int(input(f'Enter the {_+1}. number: '))
    nums = (max(numbers), min(numbers))
    print(*nums, *nums[::-1])


@u.ask_input(query=('Enter a number', ), types=(int, ))
def weekdays(inputs):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday', 'Not a weekday']
    print(days[inputs-1 if inputs in range(0, 8) else 7])


@u.ask_input(query=('Enter a word',), types=(str,))
def passord(inputs):
    word, passord = inputs, 'abcdefgh'
    print('Yay' if word == passord else
          'Wrong length' if len(word) != len(passord) else 'Nah')


def net_salary():
    gross_salary = int(input('Salary: '))
    kids = int(input('Number of dependents: '))
    net_salary = gross_salary*(0.95 if (gross_salary < 20_000 or kids >= 3) else 0.8)
    print(net_salary)


@u.ask_input(query=('Enter angle',)*3, types=(int,)*3)
def valid_triangle(inputs):
    angles = inputs
    print('Triangle' if sum(angles) == 180 else 'Not a real triangle')


@u.ask_input(query=('Enter course points', )*3, types=(int, )*3)
def grade_calculator(inputs):
    """Om en halvtime har jeg glemt _alt_ jeg gjorde her"""
    grades, buckets = inputs, [*'AABCDF'][::-1]  # Double A - The cheesy fix
    grade_avg = sum(grades)//3
    grade_idx = int(1 + (grade_avg-60) * 0.1) if grade_avg in range(60, 101) else 0
    print(f'Point average {grade_avg}, graded {buckets[grade_idx]}')


@u.ask_input(query=('Player 1', 'Player 2'), types=(str, str))
def rock_paper_scissors(inputs):
    play, weak = ('R', 'P', 'S'), ('P', 'S', 'R')
    hand1, hand2 = inputs[0][0].upper(), inputs[1][0].upper()
    result = 'Tie' if hand1 == hand2 else 'Player ' + \
        ('2' if hand2 == weak[play.index(hand1)] else '1') + ' wins'
    print(result)
    return


if __name__ == '__main__':
    rock_paper_scissors()
    pass
