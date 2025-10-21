import random

while True:
    x = 0
    l = []
    for x in range(1000):
        i = random.randint(1,2)
        if i == 1:
            l.append("Heads")
        else:
            l.append("Tails")

    h = 0
    t = 0
    for i in l:
        if i == "Heads": h+=1
        else: t+=1

    print("Out of 1000 coin flips,",h,"was Heads and", t, "was tails.")