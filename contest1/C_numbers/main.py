numbers = [input() for i in range(4)]

for i in range(4):
    numbers[i] = numbers[i].replace('+7', '8')
    numbers[i] = numbers[i].replace('-', '')
    numbers[i] = numbers[i].replace('(', '')
    numbers[i] = numbers[i].replace(')', '')
    if numbers[i][0] != '8':
        numbers[i] = '8495' + numbers[i]

for num in numbers[1:]:
    if num == numbers[0]:
        print('YES')
    else:
        print('NO')
