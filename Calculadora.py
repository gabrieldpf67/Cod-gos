while 0 == 0:
    print ("1 = adição \n2 = subtração \n3 = multiplicação \n4 = resto\n5 = divisão\n6 = poténcia\n7 = raiz\n  [escolha uma operação]")
    a = input()
    if a == "7":
        d = int(input("digite o valor da raiz  ="))
        print(d ** 0.5)
        continue
    b = int(input("escolha um numero   ="))
    c = int(input("escolha um numero   ="))
    if a == ("1"):
        print(c + b)
    elif a == ("2"):
        print(c - b)
    elif a == ("3"):
        print(c * b)
    elif a == ("4"):
        print(c % b)
    elif a == ("5"):
        print(c / b)
    elif a == ("6"):
        print(c ** b)
