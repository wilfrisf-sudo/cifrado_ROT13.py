# Cifrado César (ROT13) en Python

Pequeño script en Python que implementa el **cifrado César**, con el caso particular de **ROT13** (desplazamiento de 13 posiciones) como configuración por defecto.

## ✨ Características

- Soporta mayúsculas y minúsculas, conservando el formato original del texto.
- Los números, espacios y símbolos se dejan sin modificar.
- Funciones independientes para **cifrar** y **descifrar**.
- Desplazamiento configurable: no estás limitado a 13, podés usar cualquier cifrado César.
- Código organizado en funciones, listo para importarse en otros scripts.

## 📦 Requisitos

- Python 3.6 o superior (no usa librerías externas).

## 🚀 Uso

### Desde la terminal

```bash
python cifrado_cesar.py
```

El programa te pedirá un texto y mostrará el resultado cifrado:

```
Ingrese texto: Hola Mundo
Resultado: Ubyn Zhaqb
```

### Como módulo en otro script

```python
from cifrado_cesar import cifrar_texto, descifrar_texto

mensaje = "Hola Mundo"
cifrado = cifrar_texto(mensaje)          # ROT13 por defecto
print(cifrado)                           # Ubyn Zhaqb

original = descifrar_texto(cifrado)
print(original)                          # Hola Mundo

# Con un desplazamiento distinto (cifrado César clásico)
cifrado_3 = cifrar_texto(mensaje, desplazamiento=3)
print(cifrado_3)                         # Krod Pxqgr
```

## 🧠 Cómo funciona

El cifrado César reemplaza cada letra del alfabeto por otra que se encuentra un número fijo de posiciones más adelante (el "desplazamiento"). Por ejemplo, con un desplazamiento de 13:

- `a` → `n`
- `b` → `o`
- `z` → `m`

Como ROT13 desplaza exactamente la mitad del alfabeto (26 letras / 2 = 13), aplicar la función dos veces sobre el mismo texto devuelve el mensaje original. Por eso `cifrar_texto` y `descifrar_texto` son intercambiables cuando se usa el desplazamiento por defecto.

ejemplo
<img width="352" height="191" alt="image" src="https://github.com/user-attachments/assets/0a584b81-6f7f-4167-be86-44994ee4246a" />

## 🔮 Posibles mejoras futuras

- Soporte para acentos y la letra "ñ".
- Recibir el texto y el desplazamiento como argumentos de línea de comandos.
- Interfaz gráfica o web simple.
- Tests automatizados con `unittest` o `pytest`.

## 📄 Licencia

Este proyecto es de uso libre para fines educativos.
