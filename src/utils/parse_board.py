from pathlib import Path
import numpy as np

def parse_board(board_path: Path) -> np.ndarray:
    with open(board_path, 'r') as file:
        lines = file.readlines()
        # Convert the board into a NumPy matrix
        return np.array([line.split() for line in lines])