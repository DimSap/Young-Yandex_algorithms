note = list(map(int, input().split()))

note1_size = note[:2]
note2_size = note[2:]

min_S = 1000*2000
dim1 = 1000
dim2 = 1000

for i in range(2):
    for j in range(2):
        tmp_dim1 = max(note1_size[i], note2_size[j])
        tmp_dim2 = note1_size[i-1] + note2_size[j-1]
        tmp_S = tmp_dim2*tmp_dim1
        print(tmp_dim1, tmp_dim2, tmp_S)

        if tmp_S < min_S:
            dim1, dim2, min_S = tmp_dim1, tmp_dim2, tmp_S

print(dim1, dim2)