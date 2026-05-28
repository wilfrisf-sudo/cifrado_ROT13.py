texto = input("Ingrese texto: ").lower()

alfabeto = "abcdefghijklmnopqrstuvwxyz"
resultado = ""

for letra in texto:

    if letra in alfabeto:

        posicion = alfabeto.index(letra)

        nueva_posicion = posicion + 13

        if nueva_posicion >= 26:
            nueva_posicion = nueva_posicion - 26

        resultado += alfabeto[nueva_posicion]

    else:
        resultado += letra

print("Resultado:", resultado)
