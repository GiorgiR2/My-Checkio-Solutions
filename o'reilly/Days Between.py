from datetime import date


def days_diff(date1, date2):
    a, b, c = date1
    a0, b0, c0 = date2
    days = str(date(a0, b0, c0)-date(a, b, c))
    if days == '0:00:00':
        return 0
    return abs(int(days.split()[0]))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
