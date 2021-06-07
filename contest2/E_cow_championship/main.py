def get_vasya_score(seq):
    first_score = seq[0]
    vasya_score = 0
    for i in range(1, len(seq) - 1):
        if seq[i] > first_score:
            first_score = seq[i]
            vasya_score = 0
        elif (seq[i] % 5 == 0 and seq[i] % 2 == 1) and \
              seq[i+1] < seq[i] and \
              seq[i] >= vasya_score:
            vasya_score = seq[i]
    return vasya_score

def cov_championship(seq, vasya_score):
    if vasya_score == 0:
        return 0
    else:
        ans = 1
        for score in seq:
            if score > vasya_score:
                ans += 1
        return ans

N = int(input())
seq = list(map(int, input().split()))

vasya_score = get_vasya_score(seq)
print(cov_championship(seq, vasya_score))

