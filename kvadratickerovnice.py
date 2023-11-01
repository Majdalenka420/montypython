#Gabriel Hamrle + Magdalena Sperlova
a = int(input("Zadejte a z vyrazu ax2+bx+c"))
b = int(input("Zadejte b z vyrazu ax2+bx+c"))
c = int(input("Zadejte c z vyrazu ax2+bx+c"))

d = (b ** 2 - 4 * a * c)

if d == 0:
    print("1: ", -b / (2 * a))
    
elif d > 0:
    print("1: ", (-b + d**(1/2)) / (2 * a))
    print("2: ", (-b - d**(1/2)) / (2 * a))
    
elif d < 0:
    print("1: ", -b/(2*a), " + i",  (-d)**(1/2)/(2 * a))
    print("2: ", -b/(2*a), " - i",  (-d)**(1/2)/(2 * a))
