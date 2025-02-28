from update import update
from render import render
from attack import attack
pos = [3,3]
enemy = [4,5]
size = 10
render(size, pos, enemy)
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
