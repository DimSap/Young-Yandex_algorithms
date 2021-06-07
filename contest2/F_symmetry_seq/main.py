def len_of_add_seq(seq):
    len_of_seq_to_add = len(seq) - 1
    for i in range(len(seq)):
        if seq[i] == seq[len_of_seq_to_add]:
            len_of_seq_to_add -= 1
        else:
            len_of_seq_to_add = len(seq) - 1

    return len_of_seq_to_add + 1

def add_seq_to_sym(seq, len_of_add_seq):
    ans = []
    for i in range(len_of_add_seq - 1, -1, -1):
        ans.append(str(seq[i]))
    return ans


N = int(input())
seq = list(map(int, input().split()))

len_of_seq = len_of_add_seq(seq)
print(len_of_seq)
if len_of_seq != 0:
    add_seq = add_seq_to_sym(seq, len_of_seq)
    print(' '.join(add_seq))
