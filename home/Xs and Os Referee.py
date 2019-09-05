from typing import List

def checkio(game_result: List[str]) -> str:
    answer = 'D'
    side = list(zip(game_result[0], game_result[1], game_result[2]))
    sidee = []
    for i in side:
        sidee.append(''.join(i))
    crossed0 = game_result[0][0], game_result[1][1], game_result[2][2]
    crossed1 = game_result[0][2], game_result[1][1], game_result[2][0]
    crossed = [''.join(crossed0), ''.join(crossed1)]
    result = game_result + sidee + crossed
    for i in result:
        if i[0] == i[1] and i[0] == i[2]:
            answer = i[0]
    if answer != '.':
        return answer
    else:
        return 'D'

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
