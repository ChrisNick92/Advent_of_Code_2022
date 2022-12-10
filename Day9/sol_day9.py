# %%
from typing import Tuple, Optional

class small_rope():
    def __init__(self, head: Optional[Tuple[int,int]],
                 tail: Optional[Tuple[int,int]] = None):
        self.head = head
        self.tail = tail
        
def move_head(curr_head_pos: Tuple[int,int], move: str) -> Tuple[int,int]:
    if move == 'L':
        return curr_head_pos[0]-1, curr_head_pos[1]
    elif move == 'D':
        return curr_head_pos[0], curr_head_pos[1]-1
    elif move == 'U':
        return curr_head_pos[0], curr_head_pos[1] + 1
    else: # move == 'R'
        return curr_head_pos[0] + 1, curr_head_pos[1]

def move_knot(curr_knot: Tuple[int,int], front_knot: Tuple[int,int]) -> Tuple[int,int]:
    x,y = curr_knot
    z,w = front_knot
    directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1),
                  (-1,-1), (1,-1)] # [East (E), West (W), North (N), South (S), NE, NW, SW, SE]
    for i,j in directions:
        x_prime, y_prime = x+i, y+j
        if condition((x_prime,y_prime), front_knot):
            return x_prime,y_prime
        
def condition(new_pos: Tuple[int,int], front_knot: Tuple[int,int]) -> bool:
    return (manhattan_dist(new_pos , front_knot) == 1) or\
        ((new_pos[0]-front_knot[0])**2 + (new_pos[1]-front_knot[1])**2 == 2)

def moves(file: str = 'input.txt'):
    with open(file) as f:
        for line in  f:
            move, steps = line.rstrip("\n").split(' ')
            yield move, int(steps)

def manhattan_dist(x,y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
def part1():
    r = small_rope(head=(0,0), tail= (0,0)) # Starting position
    visited = {(0,0)}
    
    for move,steps in moves():
        for step in range(steps):
            curr_head_pos = r.head
            r.head = move_head(r.head, move) # Head moves
            if r.head != r.tail and not condition(r.tail, r.head): # Move tail
                r.tail = curr_head_pos # Tail follows
                visited.add(r.tail)
    return visited

# %%

if __name__ == '__main__':
    visited = part1()
    print(f"- Part 1: {len(visited)}")

# %%
