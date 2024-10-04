import numpy as np

def filter_board_by_color(board: np.ndarray, color: str) -> np.ndarray:
    return np.where(board == color, board, None)

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

def find_all_color_components(board: np.ndarray) -> list:
    all_connected_components = []

    for color in ["r", "g", "b", "y"]:
        filtered_board = filter_board_by_color(board, color)
        components = find_connected_components(filtered_board, color)
        all_connected_components.extend(components)  # Agregar todas las componentes a una lista
    
    return all_connected_components
