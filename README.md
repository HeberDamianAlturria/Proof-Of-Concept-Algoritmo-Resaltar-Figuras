# Entendiendo el problema:

Notemos que tenemos un board, al cuál podemos representar de la siguiente manera:

```
r r y g y r
r r g y y y
b b b b b b
g g g g g b
r g b g r r
r y y y y b
```

Donde tenemos que `r` es `red`, `y` es `yellow`, `b` es `blue` y `g` es `green`.

Nosotros queremos encontrar las figuras que tengamos definidas dentro del `board`. Donde deben cumplirse las siguientes propiedades para que una figura sea válida.

1. En el board los elementos que conforman una figura deben ser todos del `mismo color`. A continuación veremos un ejemplo para entender este comportamiento:

   - Ejemplo de una figura que satisface esta condición:

     Si tengo que una figura definida como:

     ```
     * *
     * *
     ```

     Es decir que la figura es un cuadrado.

     Y tengo en el board la siguiente figura:

     ```
     r r  ...
     r r  ...
     . .
     . .
     . .
     ```

     Entonces esa figura sería válida, ya que son todos `red`.

   - Ejemplo de una figura que NO satisface esta condición:

     Si tengo que una figura definida como:

     ```
     * *
     * *
     ```

     Es decir que la figura es un cuadrado.

     Y tengo en el board la siguiente figura:

     ```
     r r  ...
     y r  ...
     . .
     . .
     . .
     ```

     Entonces esa figura NO sería válida, ya que hay `tres red y uno yellow`, por lo que no son todos de un mismo color.

2. Ninguno de sus bordes laterales está en contacto con otra del mismo color. A continuación veremos ejemplos de este caso:

   - Ejemplo de una figura que satisface esta condición:

     Si tengo la siguiente figura:

     ```
     * *
     * *
     ```

     Es decir que la figura es un cuadrado.

     Y tengo en el board la siguiente figura:

     ```
     r r y ...
     r r g ...
     y b g
     . .
     . .
     ```

     Entonces sus componentes conexos de color rojo serían:

     ```
     r r
     r r
     ```

     Entonces notemos que los cuatro `r` forman un cuadrado perfecto, ya que los colores que están a sus bordes son distintos.

   - Ejemplo de una figura que NO satisface esta condición:

     Si tengo la siguiente figura:

     ```
     * *
     * *
     ```

     Es decir que la figura es un cuadrado.

     Y tengo en el board la siguiente figura:

     ```
     r r r ...
     r r g ...
     y b g
     . .
     . .
     ```

     Entonces sus componentes conexos de color rojo serían:

     ```
     r r r
     r r
     ```

     Entonces notemos que los cuatro `r` NO forman un cuadrado, por lo que la figura sería incorrecta.


# Algoritmo para obtener las componentes conexas.

## Objetivo de este algoritmo:

El objetivo de este algoritmo es en base al `board`, obtener para `cada color` las componentes conexas que están presentes en dicho board. Es decir que toma como argumento un board y retornará un arreglo de las componentes conexas. Por una cuestión de simpleza, las componentes conexas será una submatriz del board, compuesta de 3-uplas que tendrán primero el color, luego el row en el board y luego el column en el board que tiene la pieza.

Por ejemplo, si tengo el siguiente board:

```
r r y g y r
r r g y y y
b b b b b b
g g g g g b
r g b g r r
r y y y y b
```

Entonces, esperaría que mi algoritmo devuelva algo como:

```
[
  [
    [('r', 0, 0), ('r', 0, 1)], 
    [('r', 1, 0), ('r', 1, 1)]
  ],
  [[('r', 0, 5)]],
  [
    [('r', 4, 0)], 
    [('r', 5, 0)]
  ],
  [[('r', 4, 4), ('r', 4, 5)]],
  [[('g', 0, 3)]],
  [[('g', 1, 2)]],
  [
    [('g', 3, 0), ('g', 3, 1), ('g', 3, 2), ('g', 3, 3), ('g', 3, 4)],
    [None, ('g', 4, 1), None, ('g', 4, 3), None]
  ],
  [
    [('b', 2, 0), ('b', 2, 1), ('b', 2, 2), ('b', 2, 3), ('b', 2, 4), ('b', 2, 5)],
    [None, None, None, None, None, ('b', 3, 5)]
  ],
  [[('b', 4, 2)]],
  [[('b', 5, 5)]],
  [[('y', 0, 2)]],
  [
    [None, ('y', 0, 4), None],
    [('y', 1, 3), ('y', 1, 4), ('y', 1, 5)]
  ],
  [[('y', 5, 1), ('y', 5, 2), ('y', 5, 3), ('y', 5, 4)]],
]
```

## Explicación del algoritmo:

A continuación explicaré las partes del algoritmo destinadas a obtener las componentes conexas de todos los colores:

1. La función `find_all_color_components`. Esta función toma como argumento el board y va a retornar un arreglo de componentes conexas. Se define de la siguiente forma:

    ```python
    def find_all_color_components(board: np.ndarray) -> list:
        all_connected_components = []

        for color in ["r", "g", "b", "y"]:
            filtered_board = filter_board_by_color(board, color)
            components = find_connected_components(filtered_board, color)
            all_connected_components.extend(components)  # Agregar todas las componentes a una lista
        
        return all_connected_components
    ```

    Notemos que por cada color vamos a realizar los pasos de filtrar el board por colores, y luego buscaremos sus componentes conexas.

2. La función `filter_board_by_color`. Esta función toma como argumento el board y el color y retorna el board pero solamente con los elementos del `color`. Se define como:

    ```python
    def filter_board_by_color(board: np.ndarray, color: str) -> np.ndarray:
        return np.where(board == color, board, None)
    ```

    Notemos que vamos a dejar en el board solamente los elementos que sean del `color`, pero los que NO los reemplazaremos por `None`.

3. La función `find_connected_components`. El objetivo de esta función es 

    ```python
    def find_connected_components(filtered_board: np.ndarray, color: str) -> list:
        rows, cols = filtered_board.shape

        visited = np.zeros((rows, cols), dtype=bool)  # Matriz de visitados
        components = []

        for row in range(rows):
            for col in range(cols):
                if filtered_board[row, col] is not None and not visited[row, col]:
                    # Realiza DFS para obtener la componente conexa
                    component = depth_first_search(filtered_board, visited, row, col, color)
                    components.append(component)

        return components
    ```

    Notemos que esto lo que hará será iterar sobre el board ya filtrado (es decir que tiene un solor color). Y lo que haremos será obtener las componentes conexas de cada parte, por más que hayan partes que estén separadas. Retornaremos un arreglo de cada componente conexa.

4. La función `depth_first_search`. Esta es la función más importante, ya que nos permitirá obtener una submatriz de 3-uplas que me permitirá definir la componente conexa.

    ```python
    def depth_first_search(filtered_board: np.ndarray, visited: np.ndarray, row: int, col: int, color: str):
        rows, cols = filtered_board.shape

        # Lista para almacenar las posiciones del componente conexo
        connected_component = []
        stack = [(row, col)]  # Pila de nodos por visitar

        min_row, max_row = row, row
        min_col, max_col = col, col

        while stack:
            row, col = stack.pop()

            if visited[row, col]:
                continue

            visited[row, col] = True

            # Agregar la posición a la componente
            connected_component.append((row, col))

            # Actualizamos los límites para definir el subarreglo
            min_row = min(min_row, row)
            max_row = max(max_row, row)
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            # Revisar vecinos (arriba, abajo, izquierda, derecha)
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + i, col + j

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if filtered_board[new_row, new_col] == color and not visited[new_row, new_col]:
                        stack.append((new_row, new_col))

        # Crear un subarreglo del tamaño correcto
        subarray_rows = max_row - min_row + 1
        subarray_cols = max_col - min_col + 1
        subarray = np.full((subarray_rows, subarray_cols), None)

        # Poner los elementos de la componente en el subarreglo
        for r, c in connected_component:
            subarray[r - min_row, c - min_col] = (color, r, c)

        return subarray
    ```

    Notemos que este algoritmo lo que hará será iterar el algoritmo clásico de DFS, pero orientado a matrices, pero con la principal diferencia de que va a guardar los mayores y menores valores de `row` y `column`, para poder crear la submatriz luego.

# Algoritmo para obtener las componentes conexas.
