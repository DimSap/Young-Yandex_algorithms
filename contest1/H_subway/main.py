a, b, n, m = [int(input()) for i in range(4)]

max_first = n + (n+1) * a
min_first = n + (n-1) * a

max_second = m + (m+1) * b
min_second = m + (m-1) * b

if min_first > max_second or min_second > max_first:
    print(-1)
else:
    min_time = max(min_second, min_first)
    max_time = min(max_first, max_second)
    print(min_time, max_time)
