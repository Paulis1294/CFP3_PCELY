# #Nombre Completo: Paula Cely
# # Ejercicio 1
def suma_infinita(*args):
    return sum(args)

resultado = suma_infinita(121,21,21,21,1,21,21)
print(resultado)

#ejercicio 2
def masa_corporal(num1,num2):

    masa_corporal= num1/ (num2**2)
    return (masa_corporal)

num1 = int(input("ingrese su peso"))
num2 = float(input("ingrese su altura"))
resultado = masa_corporal(num1,num2)
print(resultado)

#Ejercicio 3 


numeros=1
suma=0
    for numeros in range (0,101):
        print(numeros)
    num=()
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print ("su numero es")
        
return(num)
print(numeros)
