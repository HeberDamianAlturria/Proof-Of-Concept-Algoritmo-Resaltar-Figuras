from pathlib import Path
import typer
from utils.parse_board import parse_board
from utils.print_components import print_components
from connected_component_algorithm import find_all_color_components

app = typer.Typer()

@app.command()
def show_connected_components(board_path: Path):
    parsed_board = parse_board(board_path)
    all_connected_components = find_all_color_components(parsed_board)    
    print_components(all_connected_components, parsed_board.shape)

@app.command()
def show_figures(board_path: Path):
    parsed_board = parse_board(board_path)
    print(parsed_board)

if __name__ == "__main__":
    app()
