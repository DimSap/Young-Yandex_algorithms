def castle_if(brick, hole):
    min_1 = min(brick[0], brick[1])
    min_2 = max(brick[0], brick[1])
    if brick[2] < min_1:
        min_2 = min_1
        min_1 = brick[2]
    elif brick[2] < min_2:
        min_2 = brick[2]

    if min_1 > min(hole) or min_2 > max(hole):
        return 'NO'
    else:
        return 'YES'


A, B, C, D, E = [float(input()) for i in range(5)]
print(castle_if([A, B, C], [D, E]))
