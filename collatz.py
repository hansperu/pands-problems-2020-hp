#ask user to enter a positive value (pedir al usuario que ingrese un valor positivo)
a = int(input("please enter a positive integer: "))

#if value entered is negative print "not a positive number" and stop (si el valor introducido es una impresion negativa "no es un número positivo" y se detiene)
while a < 0:
    print (a,"is not a positive number")
    break

#prints value of (a) when positive integer (imprime el valor de (a) cuando entero positivo)
while a > 0:
    print (a)
    break

#perform calculations until reaches 1 (realizar cálculos hasta llegar a 1)

while a > 1:

    if a % 2 == 0:
        a =  int(a/2)
        
    else:
        a = int((a*3)+1)

    print (a)