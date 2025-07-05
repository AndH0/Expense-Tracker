import random
print("Uhádni číslo!")
p_tip = 0
tip_max = 3
while p_tip < tip_max:
    tip = int(input("Hádaj číslo :"))
    p_tip += 1
    if tip == random.randint(1,3):
        print("Správne")
        break
else:
    print("Nesprávne")