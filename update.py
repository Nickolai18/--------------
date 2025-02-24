from render import render
def update(move, size, pos, enemy):
    match move:
        case 'a':
            if pos[1] == 1 or pos[1] == (size - 1):
                print("Ты не можешь двигаться в ту сторону")
                render(size, pos, enemy)
            else:
                pos[1] = pos[1] - 1
                render(size, pos, enemy)
        case 'd':
            if pos[1] == 1 or pos[1] == (size - 2):
                print("Ты не можешь двигаться в ту сторону")
                render(size, pos, enemy)
            else:
                pos[1] = pos[1] + 1
                render(size, pos, enemy)
        case 'w':
            if pos[0] == 1 or pos[0] == (size - 1):
                print("Ты не можешь двигаться в ту сторону")
                render(size, pos, enemy)
            else:
                pos[0] = pos[0] - 1
                render(size, pos, enemy)
        case 's':
            if pos[0] == (size - 2):
                print("Ты не можешь двигаться в ту сторону")
                render(size, pos, enemy)
            else:
                pos[0] = pos[0] + 1
                render(size, pos, enemy)
