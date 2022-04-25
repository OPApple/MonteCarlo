from multiprocessing.connection import wait
import random
from typing import Counter
def eq(xy):
    global counter
    if xy[0]**2 + xy[1]**2 < 1:
        counter += 1

while True:

    try:  
        randoms = []
        counter = 0

        try:
            UPBound = int(input("Anna simulaation tarkkuus (kokonaisluku > 0)\n"))
            
            if UPBound < 1:
                raise Exception
        except Exception:
            print(("\n\nAnna jokin kokonaisluku > 0\n\n"))
            continue

        print("\n\n")


        for i in range (1, UPBound):
            randoms.append([random.randrange(0, 1001)/1000, random.randrange(0, 1001)/1000])
            

        for i in range (0, randoms.__len__()):
            eq(randoms[i])
            
        N = counter/UPBound
        print(N)
        print("pi on noin ", 4*N, "\n\n")
        print("***********************************************************************************************************\n\n")
    except ValueError:
        print("\n\nAnna jokin kokonaisluku > 0\n\n")
        continue




