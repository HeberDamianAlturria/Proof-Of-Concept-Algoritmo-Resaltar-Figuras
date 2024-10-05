import numpy as np
from typer import colors, style, echo

CELL_COLORS = {
    'R': colors.RED,
    'G': colors.GREEN,
    'B': colors.BLUE,
    'Y': colors.YELLOW
}

def print_highlighted_board(board: np.ndarray, figures_map: dict):
    """Imprime el tablero con las figuras resaltadas."""
    # Resaltar en mayúsculas las celdas que pertenecen a figuras válidas
    for figure_type, components in figures_map.items():
        for component in components:
            for subarray in component:
                for cell in subarray:
                    if cell is not None and len(cell) == 3:  # Verificar que la celda no sea None
                        color, r, c = cell
                        board[r, c] = color.upper()  # Resaltar en mayúsculas

    # Imprimir el tablero con las figuras resaltadas
    for row in board:
        formatted_row = '  '.join(
            [style(str(cell), fg=CELL_COLORS.get(cell, colors.WHITE)) for cell in row]
        )
        echo(formatted_row)
    echo()  # Línea vacía al final