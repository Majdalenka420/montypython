import random

cast_prvni = ["zmoklá", "vychytralá", "paranoidní","retardovaná","patetická","jehněčí","vyšitá","studená","sovětská",]
cast_druha = ["ryba","kudla","fretka","unie","řeka","terasa","armáda","vrásečnice","police"]

print("Generátor nadávek!")

while True:
    input("Stiskni enter pro vygenerování")
    print("")
    print("Jsi " + cast_prvni[random.randint(0, len(cast_prvni)-1)] + " " + cast_druha[random.randint(0, len(cast_druha)-1)] + "!")
    print("")
    print("")
