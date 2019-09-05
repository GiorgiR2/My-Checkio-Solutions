def fastest_horse(horses: list) -> int:
    winner = [0 for i in range(len(horses))]
    horses = [[float(ii.replace(':', '.')) for ii in horses[n]] for n, i in enumerate(horses)]
    for i in horses:
        winner0 = i.index(min(i))
        winner[winner0] += 1
    return winner.index(max(winner)) + 1

if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([['1:13', '1:26', '1:11']]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
