import random

max=1
min=6

print("Heres your roll!",end=" ")
print(random.randint(max,min))

yesno = input("Reroll? Y/N: ")

while yesno == 'Y' or yesno== 'y':
    pass
    print("Heres your roll!",end=" ")
    print(random.randint(max,min))
    yesno = input("Reroll? Y/N: ")
    print("Heres your roll!",end=" ")
while yesno == 'N' or yesno == 'n':
    pass
    print("Goodbye! ")
    exit()
while yesno != 'N' or yesno != 'n':
    pass
    print("Invalid! ",end="")
    yesno = input("Reroll? Y/N: ")
    while yesno == 'Y' or yesno== 'y':
        pass
        print(random.randint(max,min))
        yesno = input("Reroll? Y/N: ")
        print("Heres your roll!",end=" ")
    while yesno == 'N' or yesno == 'n':
        pass
        print("Goodbye! ")
        exit()
