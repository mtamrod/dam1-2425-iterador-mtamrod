"""

### **1. Recorrer una lista con un iterador**

Crea una función llamada `recorrer_con_iterador` que cumpla con las siguientes condiciones:

   1. Reciba como argumento una lista de elementos.
   2. Use un **iterador** para recorrer los elementos de la lista.
   3. Concatene los elementos en una cadena de caracteres con el formato:
      ```
      "elemento1 - elemento2 - elemento3 - ... - elementoN."
      ```
   4. Devuelva la cadena resultante.

#### **Restricciones:**

- No se permite usar un bucle `for`. Debes utilizar un **iterador** con `iter()` y `next()`.

#### **Ejemplo de uso:**

```python
lista = ["Ana", "Juan", "Pedro", "Lucía"]
resultado = recorrer_con_iterador(lista)
print(resultado)
# Salida esperada:
# "Ana - Juan - Pedro - Lucía."

EJEMPLO USO PYTHON

```python
# Un iterable: una lista
numeros = [1, 2, 3]

# Obtenemos un iterador con iter()
iterador = iter(numeros)

# Usamos next() para avanzar
print(next(iterador))  # 1
print(next(iterador))  # 2
print(next(iterador))  # 3

# Cuando no hay más elementos, se lanza StopIteration
# print(next(iterador))  # Error: StopIteration

"""

def recorrer_con_iterador(lista: list) -> str:
    i = 0
    resultado = ""
    lista_iterada = iter(lista)
    while i != len(lista):
        if i == len(lista) - 1:
           resultado += next(lista_iterada)
        else:
            resultado += next(lista_iterada) + " - "

        i += 1    
    
    return resultado


def main():
    lista = ["Ana", "Juan", "Pedro", "Lucía"]
    resultado = recorrer_con_iterador(lista)
    print(resultado)

if __name__ == "__main__":
    main()