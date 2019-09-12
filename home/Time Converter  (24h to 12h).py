def time_converter(time):
    hours, minutes = int(time[0:2]), time[2:]
    if hours > 12:
        time = str(hours-12) + minutes + " p.m."
    elif hours == 0:
        time = "12:00 a.m."
    elif hours < 10:
        time = time[1:] + " a.m."
    else:
        time = time + " p.m."
    return time


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
