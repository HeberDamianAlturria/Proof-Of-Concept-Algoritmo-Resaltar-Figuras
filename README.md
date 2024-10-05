# ¿Por qué esta prueba de conceptos existe?

La idea de esta prueba de conceptos es entender como sería la idea para poder implementar el algoritmo de resaltar figuras del juego `El Switcher`. Si bien, luego se tendrá que ver como adaptar el código a las necesidades del backend, las ideas del algoritmo son lo importante de esta prueba de conceptos.

# El CLI.

Para poder entender de manera más visual los algoritmos que vamos a utilizar para resolver el problema, hay distintos comandos que se encargan de representar los resultados del algoritmo de una manera amigable.

## Los boards.

Los boards tendrán que se un archivo que definirá cada color con `r para red`, `g para green`, `y para yellow` y `b para blue`, y donde el board tendrá que ser de 6 filas y 6 columnas, y donde cada color debe aparecer 9 veces. Un ejemplo de board válido sería:

```
g g r r y g
g r r b y y
b b b g y b
y y g g g b
r r y r r r
b y g y b b
```

## Comandos.

A continuación explicaré los comandos que tiene este CLI:

- `connected-components`: Este comando se encarga de mostar para cada color las componentes conexas que tiene en el board. Dicho comando deberá tener pasado un path hacia un archivo txt de un board. A continuación veremos un ejemplo de como usarlo:

    ```bash
    python .\src\main.py connected-components .\boards\example_1.txt
    ```

- `show-figures`: Este comando se encarga de mostrar todas las figuras enconcantradas en el board. Más específicamente, lo que hará será separar cada componente conexa con el tipo de figura con la que matchea y lo representará de una manera cómoda. A continuación veremos un ejemplo de como utilizarlo:

    ```bash
    python .\src\main.py show-figures .\boards\example_1.txt
    ```

- `highlight-board`: Este comando se encarga de resaltar en el board todas las figuras encontradas que son válidas y que nosotros hemos definido. A continuación veremos un ejemplo de como utilizarlo:

    ```bash
    python .\src\main.py highlight-board .\boards\example_1.txt
    ```

# Entendiendo el problema a resolver.

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

El objetivo de este algoritmo es en base al `board`, obtener para `cada color` las componentes conexas que están presentes en dicho board. Es decir que toma como argumento un board y retornará un arreglo de las componentes conexas. Por una cuestión de simpleza, las componentes conexas será una submatriz del board, compuesta de 3-uplas que tendrán primero el color, luego el row en el board y luego el column en el board que tiene la pieza. Obviamente, cada componente conexa solamente estará representada por elementos de un mismo color.

Por ejemplo, si tengo el siguiente board:

```
r r y g y r
r r g y y y
b b b b b b
g g g g g b
r g b g r r
r y y y y b
```

Entonces, esperaríamos que el algoritmo devuelva algo como:

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

## Idea básica del algoritmo.

Vamos a tomar como arguemento el board y vamos a hacer lo siguiente:

1. Creamos una lista vacía donde guardaremos nuestras componentes conexas.
2. Por cada color existente en el board, vamos a:
    1. Filtrar el board por ese color.
    2. Vamos a iterar el board ya filtado por el color y vamos a ir aplicando `DFS` para obtener sus componentes conexas, las cuales guardaremos en la lista de componentes conexas.

A grandes rasgos, eso es lo que hará nuestro algoritmo.

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

3. La función `find_connected_components`. El objetivo de esta función es ir aplicando sucesivamente el algoritmo `DFS` para obtener todas las componentes conexas del board filtrado por color. Se define como:

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

    Notemos que esto lo que hará será iterar sobre el board ya filtrado (es decir que tiene un solo color). Y lo que haremos será obtener las componentes conexas de cada parte, por más que hayan partes que estén separadas. Retornaremos un arreglo de cada componente conexa.

4. La función `depth_first_search`. Esta es la función más importante, ya que nos permitirá obtener una submatriz de 3-uplas que me permitirá definir la componente conexa. El código sería:

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

# Algoritmo para obtener la componentes conexas que son figuras válidas.

## Objetivo de este algoritmo.

El objetivo de este algoritmo es obtener un diccionario de figuras, donde el key será el nombre de la figura y el value será un arreglo de componentes conexas que satisfacen la forma que tiene la figura. 

A continuación veremos un ejemplo sencillo:


Por ejemplo, si tengo el siguiente board:

```
r r y g y r
r r g y y y
b b b b b b
g g g g g b
r g b g r r
r y y y y b
```

Entonces, la lista de componentes conexas sería:

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

Y si tengo definido como figuras las siguientes:

- Un `Cube` de la forma:

    ```
    [
      ["*", "*"],
      ["*", "*"],
    ]
    ```

- Un `Zeta` de la forma:

    ```
    [
      [None, "*", "*"],
      ["*", "*", None],
    ]
    ```

- Un `Short T` de la forma:

    ```
    [
      [None, "*", None],
      ["*", "*", "*"],
    ]
    ```

Entonces, esperaría que mi algoritmo en este caso devolviera algo como:

```
{
  "Cube": [
    [
      [('r', 0, 0), ('r', 0, 1)],
      [('r', 1, 0), ('r', 1, 1)]
    ],
  ],
  "Short T": [
    [
      [None, ('y', 0, 4), None],
      [('y', 1, 3), ('y', 1, 4), ('y', 1, 5)]
    ],
  ],
}
```

Es decir que solamente se queda con las componentes conexas que forman una figura válida.

## Idea del algoritmo.

A continuación explicaré las ideas del algoritmo:

1. Creo un diccionario para almacenar los tipo de figuras como key y como value un arreglo de componentes conexas para ese tipo de figura.
2. Obtenemos todas las componentes conexas que tenga nuestro board.
3. Por cada componente conexa, vamos a iterar el arreglo de figuras que tengo y voy a hacer lo siguiente:
    1. Si se cumple que la componente conexa es igual a la figura en alguna de sus posibles rotaciones, entonces para el tipo de esta figura lo agrego a su arreglo correspondiente.

A grandes rasgos, esto es lo que haría el algoritmo.

## Explicación del algoritmo:

1. La definición de las figuras se hará de la siguiente manera:

    ```python
    import numpy as np


    class Figure:
        def __init__(self, type_name: str, matrix_figure: np.ndarray):
            self.matrix_figure = matrix_figure
            self.type_name = type_name

        def _to_binary(self, matrix: np.ndarray):
            """Convierte la matriz a una matriz binaria."""
            return np.where(matrix != None, 1, 0)

        def get_all_rotations(self):
            """Devuelve todas las rotaciones posibles de la figura (normal, 90°, 180°, 270°)."""
            rotations = [self.matrix_figure]  # Incluye la matriz original
            for k in range(1, 4):  # Rotar 90°, 180°, 270°
                rotated_matrix = np.rot90(self.matrix_figure, k=k)
                rotations.append(rotated_matrix)
            return rotations

        def matches_any_rotation(self, connected_component: np.ndarray):
            """Verifica si la matriz coincide con alguna rotación de la figura.
            Se abstrae del color de la componente conexa"""

            bin_connected_component = self._to_binary(connected_component)

            for rotation in self.get_all_rotations():
                if np.array_equal(self._to_binary(rotation), bin_connected_component):
                    return True
            return False


    class Cube(Figure):
        def __init__(self):
            type_name = "Cube"
            matrix_figure = np.array(
                [
                    ["*", "*"],
                    ["*", "*"],
                ]
            )
            super().__init__(type_name, matrix_figure)


    class Zeta(Figure):
        def __init__(self):
            type_name = "Zeta"
            matrix_figure = np.array(
                [
                    [None, "*", "*"],
                    ["*", "*", None],
                ]
            )
            super().__init__(type_name, matrix_figure)


    class ShortT(Figure):
        def __init__(self):
            type_name = "Short T"
            matrix_figure = np.array(
                [
                    [None, "*", None],
                    ["*", "*", "*"],
                ]
            )
            super().__init__(type_name, matrix_figure)


    def get_all_figures():
        return [Cube(), Zeta(), ShortT()]
    ```

    Notemos que la clase `Figure` es la clase padre, ya que contiene métodos que los hijos van a necesitar. En cambio, las clases hijas solamente definen las figuras que vamos a aceptar.

    Notese también que el método `matches_any_rotation` toma como argumento una componente conexa, sin embargo el color NO va a importar, sino que nos vamos a abstraer del color y vamos a comprobar la forma. Es por eso que vamos a convertir a matrices binarias tanto la figura como la componente conexa con el objetivo de comparar cómodamente.

2. La función `extract_figures_from_board`. Esta es la que finalmente se encarga de ver qué figuras del board son válidas y retornar un diccionario de las figuras agrupadas por tipo. Se define cómo:

    ```python
    def extract_figures_from_board(board: np.ndarray) -> dict:
        """Encuentra todas las figuras en el tablero y retorna un diccionario de figuras agrupadas por tipo."""
        all_connected_components = find_all_color_components(board)

        figures_by_type = defaultdict(list)

        for component in all_connected_components:
            for figure in get_all_figures():
                if figure.matches_any_rotation(component):
                    figures_by_type[figure.type_name].append(component)

        return figures_by_type
    ```

    Notemos que este algoritmo lo que hará será utilizar la función `find_all_color_components` que definimos previamente y que nos dará la lista de todas las componentes conexas que hay en el board. Y notemos que por cada componente conexa, vemos si se parece a alguna de las figuras que hemos definido.

# El código de esta prueba de conceptos.

Ya hemos mencionado los algoritmos más importantes que inspiraron esta prueba de conceptos y los que vamos a poder utilizar para resolver nuestro problema. Los demás elementos de código de esta prueba son para representar visualmente los ejemplos y poder demostrar los resultados obtenidos con estos algoritmos de una manera cómoda.

En nuestro proyecto tendremos que ver como adaptar estos algoritmos para que nos sean funcionales según las necesidades del backend, pero las ideas deberían ser las mismas.