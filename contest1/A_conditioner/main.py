room, cond = map(int, input().split())
state = input()

if state == 'freeze':
    print(cond) if room > cond else print(room)
elif state == 'heat':
    print(cond) if room < cond else print(room)
else:
    print(cond) if state == 'auto' else print(room)