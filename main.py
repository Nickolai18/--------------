from update import update
from render import render
from attack import attack
from viewMap import viewMap
pos = [5,2]
enemy = [5,1]
enemyHealth = 3
capth = str(input("Хотите стандартный размер карты?(да/нет)"))
if capth == 'нет':
    print("Введите размер карты")
    size = int(input())
else:
    size = 10
map = render(size, pos, enemy)

viewMap(map, size)

while True:
    print("Input a - left")
    print("Input d - right")
    print("Input w - up")
    print("Input s - down")
    if map[pos[0]][pos[1] - 1] == "e" or map[pos[0]][pos[1] + 1] == "e" or map[pos[0] - 1][pos[1]] == "e" or map[pos[0] + 1][pos[1]] == "e":
        print("Input e - attack")
    move = str(input())
    print("\033[H\033[J", end="")
    if move == 'e':
        if enemyHealth == 0:
            map[enemy[0]][enemy[1]] = "x"
        else:
            enemyHealth -= 1
            print(enemyHealth)
            attack(map, size, pos, enemy, enemyHealth)
    else:
        update(move, map, size, pos)
# pos = [1,1]
# health = 10
# armor = 5
# gg = {pos: [1,1], health: 10, armor: 5}
# print("Input 1 - up")
# print("Input 2 - down")
# print("Input 3 - left")
# print("Input 4 - right")
# move = int(input())
# match move:
#     case 1:
#         pos[1] = pos[1] + 1
#         render(5, pos)
#     case 2:
#         pos[1] = pos[1] - 1
#         render(5, pos)
#     case 3:
#         pos[0] = pos[1] - 1
#         render(5, pos)
#     case 4:
#         pos[0] = pos[1] + 1
#         render(5, pos)
