import os
#CALCULADORA
def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

opc=" "
opc2=" "
while opc!='d':
    os.system("cls")
    opc2='s'
    num1 = int(input("Ingrese un numero : "))
    num2 = int(input("Ingrese otro numero : "))
    print("Elige una operación aritmética")
    while(opc2!="n"):
        print("a)Suma")
        print("b)Resta")
        print("c)Multiplicación")
        print("d)Salir")
        opc=input("opción = ")
        if opc=='a':
            print("El resultado de la suma es : ", suma(num1, num2))
        elif opc=='b':
            print("El resultado de la resta es : ", resta(num1, num2))
        elif opc=='c':
            print("El resultado de la multiplicación es : ", mult(num1, num2))
        elif opc=='d':
            #print("Saliendo...")
            opc2='n'
        else:
            print("La opción es inválida")
        if opc=='d':
            print("saliendo...")
            #opc2='n'
        else:
            opc2 = input("¿Volver a resolver una operación?(s/n) : ")

    #if opc=='d':


