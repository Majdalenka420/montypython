import random

cast_prvni = ["zmoklá", "vychytralá", "paranoidní","retardovaná","patetická","jehněčí","vyšitá","studená","sovětská",]
cast_druha = ["ryba","kudla","fretka","unie","řeka","terasa","armáda","vrásečnice","police"]

print("Generátor nadávek!")

while True:
    input("Stiskni enter pro vygenerování")
    print()
    print(f"Jsi {random.choice(cast_prvni)} {random.choice(cast_druha)}!")
    print()
    print()
