def checkio(first, second):
    var = (first + ',' + second).split(',')
    answer = []
    answer_n = 0
    for i in var:
        n = var.count(i)
        if n > answer_n and n > 1:
            answer_n = n
            answer = [i]
        elif n == answer_n and i not in answer:
            answer.append(i)
    answer = sorted(answer)
    return ','.join(answer)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
