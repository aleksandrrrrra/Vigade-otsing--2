print("*** ARVUDE MÄNG ***")
print()

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
        a = abs(int(input("Sisesta täisarv => "))) #pole )
        break
    except ValueError:
        print("See ei ole täisarv")

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a == 0:
    print("Nulliga pole midagi teha")
else:
    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrame kindlaks, mitu paaris- ja paaritut numbrit on arvus")
    print()
    c = b = a #Kasutatud määramisoperaatorit '=', mitte '=='
    paaris = paaritu = 0 #Kasutatud määramisoperaatorit '=', mitte '=='

    while b > 0:
        if b % 2 == 0:
            paaris += 1
        else:
            paaritu += 1
        b = b // 10

    print("Paariseid numbreid:", paaris)
    print("Paarituid numbreid:", paaritu)
    print()
    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörame* sisestatud arvu")
    print()
    
    b = 0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    
    print("*Pööratud* arv", b)
    print()
    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Kontrollime Siracuse hüpoteesi")
    print()

    while c != 1:
        if c % 2 == 0: #Kasutatud määramisoperaatorit '=', mitte '=='
            c = c // 2 #Kasutatud määramisoperaatorit '=', mitte '=='
        else:
            c = (3 * c + 1) // 2 #Kasutatud määramisoperaatorit '=', mitte '=='
        print(c, end=" ")

    print() #jutumärki ei olnud
    print("Hüpotees kehtib") #seal olid valed tsitaadid
