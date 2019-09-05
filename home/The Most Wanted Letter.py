def checkio(text: str) -> str:
    answer = str
    number = 0
    ab = 'abcdefghijklmnopqrstuvwxyz'
    for i in text.lower():
        if i in ab:
            if text.lower().count(i) > number:
                number, answer = text.lower().count(i), i
            elif text.lower().count(i) == number:
                answer += i
    if len(answer) > 0:
        answer = ''.join(sorted(answer))[0]
    return answer


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
