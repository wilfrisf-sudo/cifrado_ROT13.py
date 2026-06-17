ALFABETO = "abcdefghijklmnopqrstuvwxyz"
DESPLAZAMIENTO_POR_DEFECTO = 13


def cifrar_letra(letra: str, desplazamiento: int = DESPLAZAMIENTO_POR_DEFECTO) -> str:
    """Cifra una sola letra usando el desplazamiento dado.

    Conserva si la letra era mayúscula o minúscula, y devuelve sin
    cambios cualquier carácter que no sea una letra del alfabeto.
    """
    es_mayuscula = letra.isupper()
    letra_min = letra.lower()

    if letra_min not in ALFABETO:
        return letra

    posicion = ALFABETO.index(letra_min)
    nueva_posicion = (posicion + desplazamiento) % len(ALFABETO)
    letra_cifrada = ALFABETO[nueva_posicion]

    return letra_cifrada.upper() if es_mayuscula else letra_cifrada


def cifrar_texto(texto: str, desplazamiento: int = DESPLAZAMIENTO_POR_DEFECTO) -> str:
    """Cifra un texto completo, letra por letra."""
    return "".join(cifrar_letra(c, desplazamiento) for c in texto)


def descifrar_texto(texto: str, desplazamiento: int = DESPLAZAMIENTO_POR_DEFECTO) -> str:
    """Descifra un texto que fue cifrado con el mismo desplazamiento."""
    return cifrar_texto(texto, -desplazamiento)


def main():
    texto = input("Ingrese texto: ")
    resultado = cifrar_texto(texto)
    print("Resultado:", resultado)


if __name__ == "__main__":
    main()
