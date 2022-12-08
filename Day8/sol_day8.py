# %%
from typing import Tuple, Optional, List, Set

def read_data(file: str = 'input.txt'):
    with open(file, 'r') as f:
        for line in f:
            yield line.rstrip("\n")
            
def get_grid_shape():
    data = read_data()
    rows, cols = 1, len(next(data))
    for line in data:
        rows += 1
    return rows, cols

def get_row(num_row: int, file: str = 'input.txt',
             cols: int = 99) -> str:
    """Return the num_row row of grid"""
    f = open(file, 'r')
    f.seek((num_row-1) * (cols+1))
    s = f.readline()
    f.close()
    return s.rstrip("\n")

def get_col(num_col: int, file: str = 'input.txt',
            rows: int = 99) -> str:
    """Return the num_col col of grid"""
    f = open(file, 'r')
    s = ""
    for i in range(rows):
        f.seek(i*(rows+1) + (num_col-1))
        s += f.read(1)
    f.close()
    return s

def find_visible_trees(tree_heights: List, on_row: Optional[int] = None, 
                       on_col: Optional[int] = None) -> Set[Tuple[int,int]]:
    """Finds the visible trees in tree_heights list and returns their (i,j)
    coordinates on the grid
    """
    visible_trees = set()
    curr_height = 0
    N = len(tree_heights)
    for i, height in enumerate(tree_heights):
        if height > curr_height:
            curr_height = height
            visible_trees.add((on_row, i+1)) if on_row else visible_trees.add((i+1, on_col))
    curr_height = 0
    for i, height in enumerate(tree_heights[::-1]):
        if height > curr_height:
            curr_height = height
            visible_trees.add((on_row, N-i)) if on_row else visible_trees.add((N-i, on_col))
    
    return visible_trees

def part1():
    visible_trees = set()
    r,c = get_grid_shape() # rows,cols
    
    for row in range(1,r+1): # Scan grid per row
        s = get_row(num_row=row, cols=c)
        visible_trees |= find_visible_trees(list(map(int, list(s))))
    for col in range(1,c+1): # Scan grid per column
        s = get_col(num_col=col, rows = r)
        visible_trees |= find_visible_trees(list(map(int, list(s))))
    print(f"Number of visible trees: {len(visible_trees)}")
    

