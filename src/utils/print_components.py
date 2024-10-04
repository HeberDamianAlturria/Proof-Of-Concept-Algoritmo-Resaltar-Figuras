import numpy as np
from typer import colors, style, echo

def convert_to_dict(components: list) -> dict:
    """Convierte una lista de componentes a un diccionario con los colores como llave."""
    components_dict = {}
    for component in components:
        color = components[0][0]

        for i, j in np.ndindex(component.shape):
          if component[i, j] is not None:
              color, _, _ = component[i, j]  # primer elemento no None
              break

        if color not in components_dict:
            components_dict[color] = []

        components_dict[color].append(component)
    return components_dict
  
def print_components(components: list, board_shape: tuple):
    components_map = convert_to_dict(components)
    rows, cols = board_shape
    for color, components in components_map.items():
        # Colorear el nombre del color y el número de componentes
        header = style(f"Color: {color} ({len(components)} components)", colors.BRIGHT_YELLOW, bold=True)
        echo(header)
        
        for i, component in enumerate(components, start=1):
            # Título de cada componente con color
            component_title = style(f"  Component {i}:", colors.CYAN, bold=True)
            echo(component_title)
            
            # Crear una matriz vacía para esta componente
            matrix = np.full((rows, cols), None)
            
            # Recorrer el array de la componente
            for subarray in component:
                for cell in subarray:
                    if cell is not None and len(cell) == 3:  # Verificar que la celda no sea None y tenga los valores correctos
                        _, r, c = cell
                        
                        # Verificar que las coordenadas estén dentro de los límites del tablero
                        if 0 <= r < rows and 0 <= c < cols:
                            matrix[r, c] = color
            
            # Imprimir la matriz de la componente
            for row in matrix:
                # Usar colores para las celdas
                formatted_row = '  '.join([style(str(cell), colors.GREEN) if cell is not None else style('.', colors.RED) for cell in row])
                echo(formatted_row)
            echo()  # Línea vacía para separar las componentes
        echo()  # Línea vacía para separar colores
