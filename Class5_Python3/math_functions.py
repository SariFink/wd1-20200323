def digit_cutter(number: float, digits: int):
    return int(number*(10**digits))/(10.**digits)


# GUARD:
if __name__ == '__main__':
    print(digit_cutter(123456789.234567890, 2))
    print(digit_cutter(123, 2))
    print(digit_cutter(0.000003, 2))