from viewMap import viewMap


def update(move, map, size, pos):
    match move:
        case 'a':
            if map[pos[0]][pos[1] - 1] == "#" or map[pos[0]][pos[1] - 1] == "e":
                print("Ты не можешь двигаться в ту сторону")
                viewMap(map, size)
            else:
                map[pos[0]][pos[1] - 1], map[pos[0]][pos[1]] = map[pos[0]][pos[1]], map[pos[0]][pos[1] - 1]
                pos[1] = pos[1] - 1
                viewMap(map, size)
        case 'd':
            if map[pos[0]][pos[1] + 1] == "#" or map[pos[0]][pos[1] + 1] == "e":
                print("Ты не можешь двигаться в ту сторону")
                viewMap(map, size)
            else:
                map[pos[0]][pos[1] + 1], map[pos[0]][pos[1]] = map[pos[0]][pos[1]], map[pos[0]][pos[1] + 1]
                pos[1] = pos[1] + 1
                viewMap(map, size)
        case 'w':
            if map[pos[0] - 1][pos[1]] == "#" or map[pos[0] - 1][pos[1]] == "e":
                print("Ты не можешь двигаться в ту сторону")
                viewMap(map, size)
            else:
                map[pos[0] - 1][pos[1]], map[pos[0]][pos[1]] = map[pos[0]][pos[1]], map[pos[0] - 1][pos[1]]
                pos[0] = pos[0] - 1
                viewMap(map, size)
            # if pos[0] == 1 or pos[0] == (size - 1):
            #     print("Ты не можешь двигаться в ту сторону")
            #     render(size, pos, enemy)
            # else:
            #     pos[0] = pos[0] - 1
            #     render(size, pos, enemy)
        case 's':
            if map[pos[0] + 1][pos[1]] == "#" or map[pos[0] + 1][pos[1]] == "e":
                print("Ты не можешь двигаться в ту сторону")
                viewMap(map, size)
            else:
                map[pos[0] + 1][pos[1]], map[pos[0]][pos[1]] = map[pos[0]][pos[1]], map[pos[0] + 1][pos[1]]
                pos[0] = pos[0] + 1
                viewMap(map, size)
            # if pos[0] == (size - 2):
            #     print("Ты не можешь двигаться в ту сторону")
            #     render(size, pos, enemy)
            # else:
            #     pos[0] = pos[0] + 1
            #     render(size, pos, enemy)
