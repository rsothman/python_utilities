def can_attack(attacker_pos, victim_pos, n):
    x_attacker, y_attacker = attacker_pos
    x_victim, y_victim = victim_pos
    if x_attacker == x_victim or y_attacker == y_victim:
        return True
    if x_attacker - x_victim == y_attacker -y_victim:
        return True
    return False


def any_can_attack(cur_soln, n):
    if len(cur_soln) < 2:
        return False
    if any([can_attack(cur_soln[attacker], cur_soln[-1], n)
            for attacker in range(len(cur_soln) -1)]):
        return True
    else:
        return False


def place_queen(soln, n):
    for i in range(n):
        column = len(soln)
        item_pos = (i, column)
        soln.append(item_pos)
        if not any_can_attack(soln, n):
            if len(soln) == n:
                print(soln)
            else:
                place_queen(soln, n)
        soln.pop()
# n = 4
# place_queen(list(), n)
# result:
#
# [(1, 0), (3, 1), (0, 2), (2, 3)]
# [(1, 0), (3, 1), (2, 2), (0, 3)]
# [(2, 0), (0, 1), (3, 2), (1, 3)]
# [(2, 0), (1, 1), (3, 2), (0, 3)]
# [(3, 0), (0, 1), (2, 2), (1, 3)]
# [(3, 0), (1, 1), (0, 2), (2, 3)]
# [(3, 0), (2, 1), (1, 2), (0, 3)]