a, b, c = [int(input()) for i in range(3)]
if c < 0:
    print('NO SOLUTION')
else:
    if a == 0:
        print('NO SOLUTION') if c*c != b else print('MANY SOLUTION')
    else:
        ans = (c*c - b)/a
        print(int(ans)) if ans == int(ans) else print('NO SOLUTION')