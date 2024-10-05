import numpy as np
from collections import defaultdict
from connected_component_algorithm import find_all_color_components
from models.figures import get_all_figures


def extract_figures_from_board(board: np.ndarray) -> dict:
    """Encuentra todas las figuras en el tablero y retorna un diccionario de figuras agrupadas por tipo."""
    all_connected_components = find_all_color_components(board)

    figures_by_type = defaultdict(list)

    for component in all_connected_components:
        for figure in get_all_figures():
            if figure.matches_any_rotation(component):
                figures_by_type[figure.type_name].append(component)

    return figures_by_type
