def long_repeat(line):
    old = ''
    ans = 0
    answers = []
    for i in line:
        if i == old:
            ans += 1
        else:
            answers.append(ans)
            ans = 1
        old = i
    print(answers)
    for i in answers:
        if i > ans:
            ans = i
    return ans

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
