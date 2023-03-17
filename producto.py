def multiplicar (a, b):

    if b==0:
        return 0
    elif b == 1:
        return a
    else:
        return a + multiplicar (a, b - 1)

if __name__ == "__main__":
    resultado = multiplicar(int(input("ingresa el primer numero que quieres multiplicar: ")),int(input("ingresa el segundo numero que quieres multiplicar: ")))
    print (resultado)
