

def two_max(seq):
    max_1 = max(seq[0], seq[1])
    max_2 = min(seq[0], seq[1])
    for i in range(2, len(seq)):
        if seq[i] > max_1:
            max_2 = max_1
            max_1 = seq[i]
        elif seq[i] > max_2:
            max_2 = seq[i]
    return (max_1, max_2)


def two_min(seq):
    min_1 = min(seq[0], seq[1])
    min_2 = max(seq[0], seq[1])
    for i in range(2, len(seq)):
        if seq[i] < min_1:
            min_2 = min_1
            min_1 = seq[i]
        elif seq[i] < min_2:
            min_2 = seq[i]
    return (min_1, min_2)


def max_prod(two_seq_max, two_seq_min):
    prod_of_min = two_seq_min[0] * two_seq_min[1]
    prod_of_max = two_seq_max[0] * two_seq_max[1]
    if prod_of_min > prod_of_max:
        ans = str(min(two_seq_min)) + ' ' + str(max(two_seq_min))
    else:
        ans = str(min(two_seq_max)) + ' ' + str(max(two_seq_max))
    return ans

seq = list(map(int, input().split()))
two_seq_min = two_min(seq)
two_seq_max = two_max(seq)

print(max_prod(two_seq_max, two_seq_min))