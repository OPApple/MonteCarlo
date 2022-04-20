import random

loop = True


while loop == True:
    #Käyttäjä syöttää luvun
    N = input("Anna jokin kokonaisluku:\n")
    N = int(N)

    randoms = []

    #Lisätään satunnaisia kokonaislukuja listaan
    for i in range(2, N):
        randoms.append(random.randint(2, int(N/2)))
        
    #Muutetaan lista dictionaryksi, jotta saadaan tuplat pois
    randoms = list(dict.fromkeys(randoms))

    for i in range(0, len(randoms)):
        




