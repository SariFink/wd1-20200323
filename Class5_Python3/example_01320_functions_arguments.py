import datetime


def print_greeting(name,x):
    print("Hello " + name)
    x+=10
    return x

output= print_greeting("Dude", 10)
output2=print_greeting("Franek",20)

print(output)
print(output2)

# oder hier noch Variante 2:

def adder(number_1):
    result = number_1 + 100
    return result

print(adder(50))


def adder_2(number_1, number_2):
    result = number_1 + number_2
    return result

print(adder_2(19, 122))

# hier ein weiteres beispiel:

def add_days_to_datetime(date_string, n_days):
    entered_datetime = datetime.datetime.strptime(date_string, "%d.%m.%Y %H:%M:%S")
    timeshift = datetime.timedelta(days=n_days)
    result_datetime = entered_datetime + timeshift
    return result_datetime

print(add_days_to_datetime("04.05.1990 09:50:10", 20000))


def hinter(number):
    if number > 10:
        return "Greater than 10"
    elif number < 2:
        return "Less than 2"
    else:
        return "Something between 2 and 10"

print(hinter(1))
print(hinter(3))
print(hinter(11))


def check_divisibility(number: int, divisor = 2) -> bool:
    retun (number % divisor) == 0

print(check_divisibility(10))
print(check_divisibility(10, 3))
