import random




y=random.randrange(1,10)

def run():
    x= int(input("číslo "))
    if x==y:
        print("ČÍSLO CORRECT")
    else:
        print('ne')
        run()

run()
