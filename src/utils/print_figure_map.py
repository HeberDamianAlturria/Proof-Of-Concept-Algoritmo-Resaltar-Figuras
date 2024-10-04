import numpy as np
from collections import defaultdict
from typer import colors, style, echo

def print_figures_map(figures_map: dict):
    """Imprime el diccionario de figuras de forma ordenada y estilizada."""
    for figure_type, components in figures_map.items():
        # Estilo para el nombre de la figura
        header = style(f"Figure Type: {figure_type} ({len(components)} components)", fg=colors.BRIGHT_CYAN, bold=True)
        echo(header)

        for i, component in enumerate(components, start=1):
            # Título de cada componente con color
            component_title = style(f"  Component {i}:", fg=colors.MAGENTA, bold=True)
            echo(component_title)

            # Imprimir la representación de la componente
            for row in component:
                formatted_row = '  '.join([str(cell) if cell is not None else '.' for cell in row])
                echo(formatted_row)

            echo()  # Línea vacía para separar las componentes
        echo()  # Línea vacía para separar los tipos de figura
