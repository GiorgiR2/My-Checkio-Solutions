from typing import List

def checkio(data: List[int]) -> [int, float]:
    data = sorted(data)
    l = len(data)
    if l % 2 == 1:
        answer = int((l-1)/2)
        answer = data[answer]
    else:
        a0 = int(l/2)
        a1 = int(l/2-1)
        answer = (data[a0]+data[a1])/2
    return answer

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("Coding complete? Click 'Check' to earn cool rewards!")
