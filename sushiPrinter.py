from random import randint
count=0
while True:
    a = randint(1,100)
    b = randint(1,30)
    count+=1
    print(" "*a+"🍣 "*b)
    if count == 100:
        for i in range(100):
            print("🍣", end="")
        count = 0
