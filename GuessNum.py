import random
ans = random.randint(1,100)
print(ans)
val = int(input("Input guess: "))

while val != ans:
    if val>ans:
        pass
        print("High!")
        val = int(input("Input guess: "))
    elif val<ans:
        pass
        print("Low")
        val = int(input("Input guess: "))
while val == ans:
    pass
    print("Correct!")
    break
