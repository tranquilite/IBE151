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


@u.fprint
def positive_negative_or_zero():
    while True:
        try:
            num = int(input('Please enter a number: '))
        except ValueError:
            print('Nuh-Uh')
        else:
            return 'Negative' if num < 0 else 'Positive' if num > 0 else 'Zero'


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


def weekdays():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday', 'Not a weekday']
    num = int(input('Enter a number: '))
    print(days[num-1 if num in range(0, 7) else 7])


def passord():
    passord = 'abcdefgh'
    word = input('Enter word: ')
    print('Yay' if  word == passord else 
          'Too short' if len(word) != len(passord) else 'Nah')


def net_salary():
    gross_salary = int(input('Salary: '))
    kids = int(input('Number of dependents: '))
    net_salary = gross_salary*(0.95 if (gross_salary < 20_000 or kids >= 3) else 0.8)
    print(net_salary)


def valid_triangle():
    angles = [0, 0, 0]
    for _ in range(0, 3):
        angles[_] = int(input(f'Enter {_}. angle: '))
    print('Valid' if sum(angles) == 180 else 'Invalid')


def grade_calculator():
        grades = [0, 0, 0]
        buckets = [*'ABCDF'][::-1]
        for _ in range(0, 3):
            grades[_] = int(input(f'Enter {_}. course: '))
        grade_avg = sum(grades)//3
        grade_idx = int(1 + (grade_avg-60) * 4/40) if grade_avg in range(60, 101) else 0
        print(buckets[grade_idx])


if __name__ == '__main__':
    grade_calculator()
    pass
