# %%
from typing import List, Tuple
import math

inf = math.inf

point = Tuple[int,int]

def get_grid(file: str = 'input.txt') -> List[str]:
    with open(file) as f:
        grid = [list(s) for s in f.read().split("\n")]
    return grid

def get_starting_position(grid: List[str]) -> point:
    for j,row in enumerate(grid):
        for i, col in enumerate(row):
            if col == 'S':
                return i,j
            
def get_grid_shape(grid: List[str]) -> point:
    return  len(grid), len(grid[0][:]) # rows cols
            
def is_legal_move(grid: List[str], grid_shape: point,
                  direction: point, curr_pos: point) -> bool:
    (M,N), (x,y), (i,j) = grid_shape, curr_pos, direction
    k,l = x+i, y+j
    if 0<= k < N and 0 <= l < M:
        next_elev = ord('z') if grid[l][k] == 'E' else ord(grid[l][k])
        curr_elev = ord('a') if grid[y][x] == 'S' else ord(grid[y][x])
        return True if next_elev-curr_elev <= 1 else False

def get_next_moves(grid: List[str], grid_shape:point,
                   curr_point:point, parent_point: point) -> List[point]:
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    moves = []
    for v in directions:
        next_move = curr_point[0]+v[0], curr_point[1]+v[1]
        if next_move != parent_point and is_legal_move(grid, grid_shape, v, curr_point):
            moves.append(next_move)
    return moves

def shortest_path_length(grid: List[str], grid_shape: point,
                         curr_point: point, parent_point: point) -> float:
    if grid[curr_point[0]][curr_point[1]] == 'E':
        return 0
    moves = get_next_moves(grid, grid_shape, curr_point,
                           parent_point)
    if not moves: # dead end
        return inf
    path_lengths = []
    print(f"Current pos: {curr_point}, moves: {moves}")
    while moves:
        next_move = moves.pop()
        path_lengths.append(1+shortest_path_length(grid,grid_shape,next_move,curr_point))
    return min(path_lengths)

def part1(file: str = 'input.txt') -> int:
    grid = get_grid(file)
    grid_shape = get_grid_shape(grid)
    starting_pos = get_starting_position(grid)
    return shortest_path_length(grid, grid_shape, starting_pos, None)

# %%
s = part1()
# %%
