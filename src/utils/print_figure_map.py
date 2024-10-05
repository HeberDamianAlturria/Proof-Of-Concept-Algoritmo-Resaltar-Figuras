import numpy as np
from typer import colors, style, echo


def print_figures_map(figures_map: dict, board_shape: tuple):
    rows, cols = board_shape

    for figure_type, components in figures_map.items():
        # Colorear el nombre de la figura y el número de componentes
        header = style(
            f"Figure Type: {figure_type} ({len(components)} components)",
            fg=colors.BRIGHT_YELLOW,
            bold=True,
        )
        echo(header)

        for i, component in enumerate(components, start=1):
            # Título de cada componente con color
            component_title = style(f"  Component {i}:", fg=colors.CYAN, bold=True)
            echo(component_title)

            # Crear una matriz vacía para esta componente
            matrix = np.full((rows, cols), None)

            # Recorrer la lista de celdas en la componente
            for row in component:
                for cell in row:
                    if (
                        cell is not None and len(cell) == 3
                    ):  # Verificar que la celda no sea None y tenga los valores correctos
                        color, r, c = cell

                        # Verificar que las coordenadas estén dentro de los límites del tablero
                        if not isinstance(r, int) or not isinstance(c, int):
                            echo(
                                style(
                                    f"Warning: Invalid coordinates {cell} in figure {figure_type}",
                                    fg=colors.RED,
                                )
                            )
                            continue

                        if 0 <= r < rows and 0 <= c < cols:
                            matrix[r, c] = color

            # Imprimir la matriz de la componente
            for row in matrix:
                # Usar colores para las celdas
                formatted_row = "  ".join(
                    [
                        (
                            style(str(cell), fg=colors.GREEN)
                            if cell is not None
                            else style(".", fg=colors.RED)
                        )
                        for cell in row
                    ]
                )
                echo(formatted_row)
            echo()  # Línea vacía para separar las componentes
        echo()  # Línea vacía para separar los tipos de figura
