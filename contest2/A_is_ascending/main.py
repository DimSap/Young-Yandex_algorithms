def is_ascending(seq):
    ans = "YES"
    for i in range(1,len(seq)):
        if seq[i] <= seq[i-1]:
            ans = "NO"
            return ans
    return ans

seq = list(map(int, input().split()))

print(is_ascending(seq))