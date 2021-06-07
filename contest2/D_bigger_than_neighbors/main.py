def bigger_than_neighbors(seq):
    ans = 0
    for i in range(1, len(seq)-1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            ans += 1
    return ans

seq = list(map(int, input().split()))
print(bigger_than_neighbors(seq))