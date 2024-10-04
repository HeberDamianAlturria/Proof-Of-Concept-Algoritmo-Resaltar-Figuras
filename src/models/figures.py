import numpy as np


class Figure:
    def __init__(self, matrix_figure: np.ndarray):
        self.matrix_figure = matrix_figure

    def _to_binary(self, matrix: np.ndarray):
        """Convierte la matriz de la figura a una matriz binaria."""
        return np.where(matrix != None, 1, 0)

    def get_all_rotations(self):
        """Devuelve todas las rotaciones posibles de la figura (normal, 90°, 180°, 270°)."""
        rotations = [self.matrix_figure]  # Incluye la matriz original
        for k in range(1, 4):  # Rotar 90°, 180°, 270°
            rotated_matrix = np.rot90(self.matrix_figure, k=k)
            rotations.append(rotated_matrix)
        return rotations
    
    def matches_any_rotation(self, matrix: np.ndarray):
        """Verifica si la matriz coincide con alguna rotación de la figura."""
        bin_matrix = self._to_binary(matrix)

        for rotation in self.get_all_rotations():
            if np.array_equal(self._to_binary(rotation), bin_matrix):
                return True
        return False


class Cube(Figure):
    def __init__(self):
        matrix_figure = np.array(
            [
                ["*", "*"],
                ["*", "*"],
            ]
        )
        super().__init__(matrix_figure)


class Zeta(Figure):
    def __init__(self):
        matrix_figure = np.array(
            [
                [None, "*", "*"],
                ["*", "*", None],
            ]
        )
        super().__init__(matrix_figure)

class ShortT(Figure):
    def __init__(self):
        matrix_figure = np.array(
            [
                [None, "*", None],
                ["*", "*", "*"],
            ]
        )
        super().__init__(matrix_figure)

def get_all_figures():
    return [Cube(), Zeta(), ShortT()]