def checkio(data: str) -> bool:
    if len(data) >= 10:
        upper = 0
        lower = 0
        digit = 0
        for i in data:
            if i.isupper() and upper == 0:
                upper = 1
            elif i.islower() and lower == 0:
                lower = 1
            if i.isdigit() and digit == 0:
                digit = 1
        sum0 = upper + lower + digit
        if sum0 == 3:
            return True
    return False

# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
