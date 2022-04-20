from logging import exception
import random

loop = True


while loop == True:
    check = True

    try:
        #Käyttäjä syöttää luvun
        N = input("\nAnna jokin positiivinen kokonaisluku:\n")
        N = int(N)

        try:
            if N <= 0:
                raise Exception("Annettu luku ei ole positiivinen kokonaisluku")
        except Exception:
            print("Ei Positiivinen")
            continue
        #Testataan perustapaukset (kun N/2 < 2, mikä aiheuttaa ongelmia satunnaislukujen valinnassa)
        if N == 2 or N == 3 or N == 5:
            check = False
            
        if N == 4:
            check = False
            alkuluku = False

        randoms = []
        alkuluku = True

        
        if check == True:
            #Lisätään satunnaisia kokonaislukuja listaan
            for i in range(2, N):
                randoms.append(random.randint(2, int(N/2)))
                
            #Muutetaan lista dictionaryksi, jotta saadaan tuplat pois
            randoms = list(dict.fromkeys(randoms))

            for i in range(0, len(randoms)):
                if N % randoms[i] == 0:
                    alkuluku = False
        
        if alkuluku == False:
            print("Ei alkuluku")
        else:
            print("Alkuluku")
    except ValueError:
        print("En.")
        continue



