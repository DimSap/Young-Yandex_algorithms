def is_constant(seq):
    for i in range(len(seq)-1):
        if seq[i] != seq[i+1]:
            return 0
    return 1

def is_ascending(seq):
    for i in range(len(seq)-1):
        if seq[i] >= seq[i+1]:
            return 0
    return 1

def is_weakly_ascending(seq):
    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]:
            return 0
    return 1

def is_descending(seq):
    for i in range(len(seq)-1):
        if seq[i] <= seq[i+1]:
            return 0
    return 1

def is_weakly_descending(seq):
    for i in range(len(seq)-1):
        if seq[i] < seq[i+1]:
            return 0
    return 1

def sequence_type(seq):
    if is_constant(seq):
        return 'CONSTANT'
    elif is_ascending(seq):
        return 'ASCENDING'
    elif is_weakly_ascending(seq):
        return 'WEAKLY ASCENDING'
    elif is_descending(seq):
        return 'DESCENDING'
    elif is_weakly_descending(seq):
        return 'WEAKLY DESCENDING'
    else:
        return 'RANDOM'

seq = []
flag = True
while flag:
    a = float(input())
    if a == -2000000000:
        flag = False
    else:
        seq.append(a)

print(sequence_type(seq))