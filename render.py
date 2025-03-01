def render(size, pos, enemy):
    s = []
    x = pos[0]
    y = pos[1]
    xE = enemy[0]
    yE = enemy[1]
    for i in range(0, size):
        s.append([])
        for j in range(0, size):
            if i == 0 or i == (size - 1):
                s[i].append('#')
            else:
                if j == 0 or j == (size - 1):
                    s[i].append('#')
                elif i == x and j == y:
                    s[i].append('@')
                elif i == xE and j == yE:
                    s[i].append('e')
                else:
                    s[i].append(' ')
    return s
