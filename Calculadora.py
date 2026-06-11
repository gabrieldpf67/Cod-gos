while 0 == 0:
    print ("1 = adição \n2 = subtração \n3 = multiplicação \n4 = resto\n5 = divisão\n6 = poténcia\n7 = raiz\n8 - porcentagem\n     [escolha uma operação]")
    a = input()
    if a == ("1"):
        b = int(input("escolha um numero   ="))
        c = int(input("escolha um numero   ="))
        print(c + b)
    elif a == ("2"):
        b = int(input("escolha um numero   ="))
        c = int(input("escolha um numero   ="))
        print(c - b)
    elif a == ("3"):
        b = int(input("escolha um numero   ="))
        c = int(input("escolha um numero   ="))
        print(c * b)
    elif a == ("4"):
        b = int(input("escolha um numero   ="))
        c = int(input("escolha um numero   ="))
        print(c % b)
    elif a == ("5"):
        b = int(input("escolha um numero   ="))
        c = int(input("escolha um numero   ="))
        print(c / b)
    elif a == ("6"):
        b = int(input("escolha um numero   ="))
        c = int(input("escolha um numero   ="))
        print(c ** b)
    elif a == ("8"):
        cleytom = float(input("Digite o valor ="))
        nume = float(input("Digite a porcentagem ="))
        print (cleytom * nume /100)
    elif a == "7":
        d = int(input("digite o valor da raiz  ="))
        print(d ** 0.5)
    elif a == ("9"):
        y = int(input())
        x = int(input())
        z = int(input())
        delta = (x ** 2) - (4 * y * z)
        print (delta)
        
        x1 = ((-1*x) + (delta ** 0.5)) / (2 * y)
        print (x1)
        
