from pathlib import Path
import numpy as np

def check_color_counts(board: np.ndarray):
    # Contar las ocurrencias de cada color
    unique, counts = np.unique(board, return_counts=True)
    color_counts = dict(zip(unique, counts))

    # Colores esperados
    expected_colors = {"r": 9, "g": 9, "b": 9, "y": 9}

    for color, expected_count in expected_colors.items():
        actual_count = color_counts.get(color, 0)  # Obtiene el conteo o 0 si no está en el tablero
        if actual_count != expected_count:
            raise ValueError(f"El tablero debe tener exactamente 9 '{color}' pero tiene {actual_count}")

def parse_board(board_path: Path) -> np.ndarray:
    with open(board_path, 'r') as file:
        lines = file.readlines()
        
        board = np.array([line.split() for line in lines])

        if (board.shape != (6, 6)):
            raise ValueError("El tablero debe ser de 6x6")

        check_color_counts(board)

        return board