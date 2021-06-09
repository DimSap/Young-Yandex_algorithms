def triangle_freq(freqs, freq_comparison):
    left_boundary = 30
    right_boundary = 4000

    for i in range(1, len(freqs)):
        middle = (freqs[i-1] + freqs[i]) / 2
        if middle > max(left_boundary, right_boundary) or \
           middle < min(left_boundary, right_boundary):
            continue
        if freq_comparison[i] == 'closer':
            if middle >= freqs[i]:
                right_boundary = middle
            else:
                left_boundary = middle
        elif freq_comparison[i] == 'further':
            if middle >= freqs[i]:
                left_boundary = middle
            else:
                right_boundary = middle
    return (left_boundary, right_boundary)

n = int(input())
freqs = []
freqs.append(float(input()))
freq_comparison = ['None']
for i in range(n-1):
    input_str = input().split()
    freqs.append(float(input_str[0]))
    freq_comparison.append(input_str[1])
ans = triangle_freq(freqs, freq_comparison)
print(ans[0], ans[1])
