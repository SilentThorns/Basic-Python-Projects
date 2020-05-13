import random
array = ["r", "p", "s"]
random = random.randrange(0, 2)
opprps = array[random]
print(opprps)
rps = input("Rock, paper, scissors?: ")
userrps = rps[0]
lose = "you lose!"
win = "you win!"
draw = "draw!"
while userrps == 's' or 'S':
    if opprps == 'p':
        print(win)
        exit()
    elif opprps == 'r':
        print(lose)
        exit()
    else:
        print(draw)

while userrps == 'p' or 'P':
    if opprps == 'r':
        print(win)
        exit()
    elif opprps == 's':
        print(lose)
        exit()
    else:
        print(draw)
        exit()

while userrps == 'r' or 'R':
    if opprps == 's':
        print(win)
        exit()
    elif opprps == 'p':
        print(lose)
        exit()
    else:
        print(draw)
        exit()
