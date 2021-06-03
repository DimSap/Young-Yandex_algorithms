
s = [float(input()) for i in range(3)]

if any([1 if s[i] <= 0 else 0 for i in range(3)]):
    print('NO')

else:
    result = 'YES'
    for i in range(3):
        if s[i] >= s[i-1] + s[i-2]:
            result = 'NO'
    print(result)



