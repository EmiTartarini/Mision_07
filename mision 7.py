def DIVIDIR(divisor,dividendo):
    NumeroBase=dividendo
    Cociente=0

    while dividendo>=divisor:
        dividendo=dividendo-divisor
        Cociente+=1
    print (NumeroBase,"/", divisor, "=", Cociente, "y sobran", dividendo)

def Mayor():
    NumeroMasGrande=0
    Numero=0

    print ("Teclea una serie de números para encontrar el mayor.")

    Numero= int(input("-1 para salir]: "))

    if Numero != -1:
        while Numero != -1:
            if Numero >= 0:
                if numero >= NumeroMasGrande:
                    NumeroMasGrande = numero
            numero = int(input("Teclea -1 para salir]: "))
        print("El mayor es:", NumeroMasGrande)
        print()
    else:
        print("No hay valor")
        print()

def main():
    print("Ciclos While")
    print("Emiliano Tartarini Rodríguez")
    print("A01372663")
    print("Calcular")
    print("Encontrar el mayor")
    print("Salir")
    opcion = int(input("Teclea tu opción: "))

    while opcion != 3:
        if opcion < 1 or opcion > 3:
            print("ERROR")
            ("Ciclos While")
            print("Emiliano Tartarini Rodríguez")
            print("A01372663")
            print("Calcular")
            print("Encontrar el mayor")
            print("Salir")
            opcion = int(input("Teclea tu opción:"))

        elif opcion == 1:
            dividendo = int(input("dividendo:"))
            divisor = int(input("divisor:"))

            print("Ciclos While")
            print("Emiliano Tartarini Rodríguez")
            print("A01372663")
            print("Calcular")
            print("Encontrar el mayor")
            print("Salir")
            opcion = int(input("Teclea tu opción:"))

        elif opcion == 2:

            print("Misión 07.")
            print("Emiliano Tartarini Rodriguex")
            print("A01372663")
            print("Calcular")
            print("Encontrar")
            print("Salir")
            opcion = int(input("Teclea tu opción:"))

    print("ADIOS, NO VUELVA")

main()