# %%
from typing import Tuple, Optional, List, Set

def read_data(file: str = 'input.txt'):
    with open(file, 'r') as f:
        for line in f:
            yield line.rstrip("\n")
            
def get_grid_shape(file: str = 'input.txt'):
    data = read_data(file)
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
    curr_height = -1
    N = len(tree_heights)
    for i, height in enumerate(tree_heights):
        if height > curr_height:
            curr_height = height
            visible_trees.add((on_row, i+1)) if on_row else visible_trees.add((i+1, on_col))
    curr_height = -1
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
        visible_trees |= find_visible_trees(list(map(int, list(s))), on_row=row)
    for col in range(1,c+1): # Scan grid per column
        s = get_col(num_col=col, rows = r)
        visible_trees |= find_visible_trees(list(map(int, list(s))), on_col=col)
    return visible_trees
    
    
def write_visible_trees(visible_trees: set, grid_shape: Tuple[int,int],
                        file = 'output.txt'):
    f = open(file, 'w')
    lines = []
    r,c = grid_shape
    for row in range(r):
        s = ""
        for col in range(c):
            s += '*' if (row+1, col+1) in visible_trees else ' '
        s += '\n'
        lines.append(s)
    f.writelines(lines)
    f.close()

def scenic_score(tree_coordinates: Tuple[int,int],
                 grid_shape: Tuple[int,int]) -> int:
    (i,j), (M,N) = tree_coordinates, grid_shape
    
    row = list(map(int, get_row(num_row= i)))
    col = list(map(int, get_col(num_col=j)))
    tree_height = row[j-1]
    
    left,right,top,down = 0,0,0,0
    # I know the following looks bad
    step = 1
    d = {'Left_Max': True, 'Right_Max': True, 
         'Top_Max': True, 'Down_Max': True}
    
    while condition(i,j,M,N,step):
        if d['Left_Max'] and j-step >=1:
            if row[j-step-1] >= tree_height:
                left += 1
                d['Left_Max'] = False
            else:
                left +=1
        if d['Down_Max'] and i+step <= M:
            if col[i+step -1] >= tree_height:
                down += 1
                d['Down_Max'] = False
            else:
                down += 1
        if d['Top_Max'] and i-step >= 1:
            if col[i-step -1] >= tree_height:
                top += 1
                d['Top_Max'] = False
            else:
                top +=1
        if d['Right_Max'] and j+step <= N:
            if row[j+step -1] >= tree_height:
                right +=1
                d['Right_Max'] = False
            else:
                right += 1
        step += 1
    
    return left*top*right*down

def condition(i,j,M,N,step):
    return i+step <= M or i-step >= 1 or j+step <= N or j-step >= 1


def part2():
    M,N = get_grid_shape()
    m = 0
    for i in range(1,M+1):
        for j in range(1, N+1):
            m = max(m, scenic_score((i,j), (M,N)))
    return m

# %%

if __name__ == '__main__':
    
    visible_trees = part1()
    m = part2()
    # write_visible_trees(visible_trees, get_grid_shape(),
    #                     file = 'VisibleTrees.txt')
    print(f"Part 1 Answer: {len(visible_trees)}")
    print(f"Part 2 Answer: {m}")
