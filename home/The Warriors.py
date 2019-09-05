class Warrior:
    health = 50
    attack = 5
    is_alive = True


class Knight(Warrior):
    health = 50
    attack = 7
    is_alive = True


def fight(unit_1, unit_2):
    hit = 0
    while unit_1.health > 0 and unit_2.health > 0:
        if hit % 2 == 1:
            unit_1.health -= unit_2.attack
        elif hit % 2 == 0:
            unit_2.health -= unit_1.attack
        hit += 1
    # print(unit_1.health, unit_2.health)
    if unit_1.health > 0:
        unit_1.is_alive = True
        unit_2.is_alive = False
    else:
        unit_1.is_alive = False
        unit_2.is_alive = True
    return unit_1.is_alive
    
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
