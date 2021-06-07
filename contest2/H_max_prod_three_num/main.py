def first_three_max(max_1, max_2, max_3):
    if max_2 < max_3:
        max_3, max_2 = max_2, max_3
    if max_2 > max_1:
        max_2, max_1 = max_1, max_2
    if max_2 < max_3:
        max_2, max_3 = max_3, max_2
    return max_1, max_2, max_3


def three_max(seq):
    max_1, max_2, max_3 = first_three_max(seq[0], seq[1], seq[2])
    for i in range(3, len(seq)):
        if seq[i] > max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = seq[i]
        elif seq[i] > max_2:
            max_3 = max_2
            max_2 = seq[i]
        elif seq[i] > max_3:
            max_3 = seq[i]
    return (max_1, max_2, max_3)


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

def get_str_ans(ans):
    str_ans = []
    for num in ans:
        str_ans.append(str(num))
    return ' '.join(str_ans)

def max_prod(three_seq_max, two_seq_min):
    prod_of_max = three_seq_max[0] * three_seq_max[1] * three_seq_max[2]
    prod_of_twoMin_max = two_seq_min[0] * two_seq_min[1] * three_seq_max[0]
    prod_list = [prod_of_max, prod_of_twoMin_max]
    if max(prod_list) == prod_of_max:
        ans = get_str_ans(three_seq_max)
    else:
        ans = get_str_ans([two_seq_min[0], two_seq_min[1], three_seq_max[0]])
    return ans

seq = list(map(int, input().split()))
two_seq_min = two_min(seq)
three_seq_max = three_max(seq)

print(max_prod(three_seq_max, two_seq_min))
