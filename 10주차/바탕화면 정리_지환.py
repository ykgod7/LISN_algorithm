# 초기
def solution(wallpaper):
    lux, luy, rdx, rdy = -1, -1, -1, -1
    
    for (i, line) in enumerate(wallpaper):
        if line.find('#') > -1:
            for (j, letter) in enumerate(line):
                if letter == '#':
                    if lux == -1:
                        lux = i
                        luy = j
                        rdx = i + 1
                        rdy = j + 1
                    else:
                        rdx = i + 1
                        if j < luy:
                            luy = j
                        elif j >= luy and j >= rdy:
                            rdy = j + 1
                                    
    return [lux, luy, rdx, rdy]

# 수정본
def solution(wall):
    a, b = [], []
    
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == '#':
                a.append(i)
                b.append(j)
                
                                    
    return [min(a), min(b), max(a) + 1, max(b) + 1]