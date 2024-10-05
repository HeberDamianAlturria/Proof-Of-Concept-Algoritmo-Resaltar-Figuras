from pathlib import Path
import typer
from utils.parse_board import parse_board
from utils.print_components import print_components
from utils.print_figure_map import print_figures_map
from utils.print_highlighted_board import print_highlighted_board
from connected_component_algorithm import find_all_color_components
from figures_algorithm import extract_figures_from_board

app = typer.Typer()

@app.command(name="connected-components", help="Mustra las componentes conexas del tablero")
def show_connected_components(board_path: Path):
    parsed_board = parse_board(board_path)
    all_connected_components = find_all_color_components(parsed_board)    
    print_components(all_connected_components, parsed_board.shape)

@app.command(name="show-figures", help="Muestra las figuras encontradas en el tablero")
def show_figures(board_path: Path):
    parsed_board = parse_board(board_path)
    figures_map = extract_figures_from_board(parsed_board)
    print_figures_map(figures_map, parsed_board.shape)

@app.command(name="highlight-board", help="Resalta en el tablero las figuras encontradas")
def highlight_figures_in_board(board_path: Path):
    parsed_board = parse_board(board_path)
    figures_map = extract_figures_from_board(parsed_board)
    print_highlighted_board(parsed_board, figures_map)    

if __name__ == "__main__":
    app()
