import numpy as np

print("**** Calculadora ****")

menu = int(input(">> Menu de opciones: \n 1 Suma \n 2 Resta \n 3 Multiplicación \n 4 División \n 5 Raíz \n 6 Exponente \n 7 Salir \n"))

while menu != 7:
    respuesta = "s"
    if menu == 1:
        print("(+) Suma de números")
        while respuesta == "s" or respuesta == "S":
            num1 = input("Ingresa el primer número ->")
            num2 = input("Ingresa el segundo número ->")
            resultado = int(num1) + int(num2)
            print("El resultado de la suma es:", resultado)
            respuesta = input("Desea realizar otra suma? [s/n]")
            
    elif menu == 2:
        print("(-) Resta de números")
        while respuesta == "s" or respuesta == "S":
            num1 = input("Ingresa el primer número ->")
            num2 = input("Ingresa el segundo número ->")
            resultado = int(num1) - int(num2)
            print("El resultado de la resta es:", resultado)
            respuesta = input("¿Desea realizar otra resta? [s/n]")
    
    elif menu == 3:
        print("(*) Multiplicación de números")
        while respuesta == "s" or respuesta == "S":
            num1 = input("Ingresa el primer número ->")
            num2 = input("Ingresa el segundo número ->")
            resultado = int(num1) * int(num2)
            print("El resultado de la multiplicación es:", resultado)
            respuesta = input("¿Desea realizar otra multiplicación? [s/n]")
            
    elif menu == 4:
        print("(/) División de números")
        while respuesta == "s" or respuesta == "S":
            num1 = input("Ingresa el primer número ->")
            num2 = input("Ingresa el segundo número ->")
            resultado = int(num1) / int(num2)
            print("El resultado de la división es:", resultado)
            respuesta = input("¿Desea realizar otra división? [s/n]")
    
    elif menu == 5:
        print("(r) Raíz de un número")
        while respuesta == "s" or respuesta == "S":
            num1 = int(input("Ingresa un número ->"))
            raiz = np.sqrt(num1)
            print("La raíz es:", raiz)
            respuesta = input("¿Desea realizar otra raíz? [s/n]")
 
    elif menu == 6:
        print("(ex) Exponente de un número")
        while respuesta == "s" or respuesta == "S":
            num1 = input("Ingresa el número base ->")
            num2 = input("Ingresa el valor de la potencia ->")
            exponente = np.power(int(num1), int(num2))
            print("La resultado es:", exponente)
            respuesta = input("¿Desea realizar otro cálculo? [s/n]")
            
    else:
        print(">>>>>>>>>> ¡¡¡ Por favor selecciona un número del menú !!!")
    menu = int(input(">> Menu de opciones: \n 1 Suma \n 2 Resta \n 3 Multiplicación \n 4 División \n 5 Raíz \n 6 Exponente \n 7 Salir \n"))
 
