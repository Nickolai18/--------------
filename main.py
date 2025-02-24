from update import update
from render import render
from attack import attack
pos = [8,2]
enemy = [8,1]
size = 10
render(size, pos, enemy)
print("Первый Commit")
print("Второй Commit")
while True:
    print("Input a - left")
    print("Input d - right")
    print("Input w - up")
    print("Input s - down")
    if enemy[0] == (pos[0] - 1) and enemy[1] == (pos[1]) or enemy[0] == (pos[0] + 1) and enemy[1] == (pos[1]):
        print("Input e - attack")
    elif enemy[0] == (pos[0]) and enemy[1] == (pos[1] - 1) or enemy[0] == (pos[0]) and enemy[1] == (pos[1] + 1):
        print("Input e - attack")
    move = str(input())
    if move == 'e':
        attack(size, pos, enemy)
    else:
        update(move, size, pos, enemy)
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
