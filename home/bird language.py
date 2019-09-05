VOWELS = "aeiouy"


def translate(phrase):
    answer, old, skip = '', '', 0
    for n, i in enumerate(phrase):
        if skip > 0:
            skip -= 1
            continue
        if i not in VOWELS:
            answer += i
        try:
            if i in VOWELS and [i, i] == [phrase[n+1], phrase[n+2]]:
                answer += i
                old, skip = i, 2
            elif i in VOWELS and phrase[n+1] == i and i != old:
                answer += i
                old = i
        except:
            pass
    return answer


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
