from render import render
def attack(size, pos, enemy):
    if enemy[0] == (pos[0] - 1) and enemy[1] == (pos[1]):
        print('3456')
        if (enemy[0] + 1) != 0:
            render(size, pos, enemy)
        else:
            enemy[0] = enemy[0] - 1
            render(size, pos, enemy)
    elif enemy[0] == (pos[0] + 1) and enemy[1] == (pos[1]):
        print('456')
        if (enemy[0] - 2) != size:
            render(size, pos, enemy)
        else:
            enemy[0] = enemy[0] - 1
            render(size, pos, enemy)
    elif enemy[0] == (pos[0]) and enemy[1] == (pos[1] - 1):
        print('56')
        if (enemy[1] + 1) != 0:
            render(size, pos, enemy)
        else:
            enemy[1] = enemy[1] - 1
            render(size, pos, enemy)
    elif enemy[0] == (pos[0]) and enemy[1] == (pos[1] + 1):
        print('6')
        if (enemy[1] - 2) != size:
            render(size, pos, enemy)
        else:
            enemy[1] = enemy[1] + 1
            render(size, pos, enemy)