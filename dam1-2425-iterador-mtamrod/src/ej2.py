"""
### **2. Generar una matriz regular con las dos diagonales marcadas**

Crea una función llamada `crear_matriz_diagonales` que reciba como argumento un número entero positivo `dimension`, que representa las dimensiones de una matriz cuadrada `n x n`. La función debe generar y devolver la matriz con las siguientes condiciones:

   1. Todas las celdas deben estar inicialmente rellenas con `0`.
   2. Las celdas de las **dos diagonales** (principal y secundaria) deben estar rellenas con `1`.

Se deben crear las siguientes funciones como mínimo:

   1. `crear_matriz_diagonales`: Retorna una matriz cuadrada con todas las celdas a 0, excepto las diagonales a 1.
   2. `generar_matriz_regular`: Retorna una matriz cuadrada con todos los valores por defecto a 0.
   3. `imprimir_matriz`: Imprime la matriz con los elementos separados por ",".

#### **Restricciones:**

- Solo se permite usar el bucle `for` para cualquier función del programa.
- Debes usar `join` para imprimir la matriz.

#### **Ejemplo de uso:**

```python
matriz = crear_matriz_diagonales(5)

# La matriz generada será:
# (
#   [1, 0, 0, 0, 1],
#   [0, 1, 0, 1, 0],
#   [0, 0, 1, 0, 0],
#   [0, 1, 0, 1, 0],
#   [1, 0, 0, 0, 1]
# )

imprimir_matriz(matriz)
```

#### **Salida esperada sería la siguiente:**
```
1, 0, 0, 0, 1
0, 1, 0, 1, 0
0, 0, 1, 0, 0
0, 1, 0, 1, 0
1, 0, 0, 0, 1
"""

def generar_matriz_regular(dimension: int, valor: str) -> list:
    matriz = []

    for _ in range(dimension):  
        trozo_matriz = []
        for _ in range(dimension):
            trozo_matriz.append(valor)
        matriz.append(trozo_matriz)
    
    return matriz

def crear_matriz_diagonales(dimension: int, valor_diagonal: str, valor_casilla: str) -> list:
   matriz = generar_matriz_regular(dimension, valor_casilla)
   i = 0
   j = -1
   for fila in matriz:
      fila[i] = valor_diagonal
      fila[j] = valor_diagonal
      i += 1
      j -= 1
   
   return matriz


def imprimir_matriz(matriz: list, separador: str):
   for fila in matriz:
      print(separador.join(map(str, fila)))

def main():
   matriz = crear_matriz_diagonales(5, "1", "0")
   imprimir_matriz(matriz, ", ")
   
if __name__ == "__main__":
   main()