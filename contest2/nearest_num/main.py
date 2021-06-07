def nearest_num(seq, x):
    ans = seq[0]
    min_distance = abs(x - ans)
    for i in range(1,len(seq)):
        distance = abs(x - seq[i])
        if distance < min_distance:
            ans = seq[i]
            min_distance = distance
    return ans

N = int(input())
seq = list(map(int, input().split()))
x = int(input())

print(nearest_num(seq, x))
