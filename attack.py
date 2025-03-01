from viewMap import viewMap


def attack(map, size, pos, enemy, enemyHealth):
    if enemy[0] == (pos[0] - 1) and enemy[1] == (pos[1]):
        print('3456')
        if map[enemy[0] - 1][enemy[1]] == "#":
            viewMap(map, size)
        else:
            map[enemy[0]][enemy[1] - 1], map[enemy[0]][enemy[1]] = map[enemy[0]][enemy[1]], map[enemy[0]][enemy[1] - 1]
            enemy[0] = enemy[0] - 1
            viewMap(map, size)
    elif enemy[0] == (pos[0] + 1) and enemy[1] == (pos[1]):
        print('456')
        if map[enemy[0] + 1][enemy[1]] == "#":
            print("Враг от тебя не убежит")
            viewMap(map, size)
        else:
            map[enemy[0] + 1][enemy[1]], map[enemy[0]][enemy[1]] = map[enemy[0]][enemy[1]], map[enemy[0] + 1][enemy[1]]
            enemy[0] = enemy[0] - 1
            viewMap(map, size)
    elif enemy[0] == (pos[0]) and enemy[1] == (pos[1] - 1):
        print('56')
        if map[enemy[0]][enemy[1] - 1] == "#":
            print("Враг от тебя не убежит")
            viewMap(map, size)
        else:
            map[enemy[0]][enemy[1] - 1], map[enemy[0]][enemy[1]] = map[pos[0]][enemy[1]], map[enemy[0]][enemy[1] - 1]
            enemy[1] = enemy[1] - 1
            viewMap(map, size)
    elif enemy[0] == (pos[0]) and enemy[1] == (pos[1] + 1):
        print('6')
        if map[enemy[0]][enemy[1] + 1] == "#":
            print("Враг от тебя не убежит")
            viewMap(map, size)
        else:
            map[enemy[0]][enemy[1] + 1], map[enemy[0]][enemy[1]] = map[enemy[0]][enemy[1]], map[enemy[0]][enemy[1] + 1]
            enemy[1] = enemy[1] + 1
            viewMap(map, size)
