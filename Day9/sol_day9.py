# %%
from typing import Tuple, Optional

class rope():
    def __init__(self, head: Optional[Tuple[int,int]],
                 tail: Optional[Tuple[int,int]] = None,
                 prev_move: Optional[str] = None):
        self.head = head
        self.tail = tail
        
def make_move(curr_head_pos: Tuple[int,int], move: str):
    if move == 'L':
        return curr_head_pos[0]-1, curr_head_pos[1]
    elif move == 'D':
        return curr_head_pos[0], curr_head_pos[1]-1
    elif move == 'U':
        return curr_head_pos[0], curr_head_pos[1] + 1
    else: # move == 'R'
        return curr_head_pos[0] + 1, curr_head_pos[1]

def moves(file: str = 'input.txt'):
    with open(file) as f:
        for line in  f:
            move, steps = line.rstrip("\n").split(' ')
            yield move, int(steps)

def manhattan_dist(x,y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

def move_tail(head_pos: Tuple[int,int], tail_pos: Tuple[int,int]):
    condition_met = (manhattan_dist(head_pos,tail_pos) == 1) or \
        ((head_pos[0]-tail_pos[0])**2 + (head_pos[1]-tail_pos[1])**2 == 2) or\
            head_pos == tail_pos
    return True if not condition_met else False
        
def part1():
    r = rope(head=(0,0), tail= (0,0)) # Starting position
    visited = {(0,0)}
    
    for move,steps in moves():
        for step in range(steps):
            curr_head_pos = r.head
            r.head = make_move(r.head, move) # Head moves
            if move_tail(r.head, r.tail): # Move Tail if not opposite moves occur
                r.tail = curr_head_pos # Tail follows
                visited.add(r.tail)
    return visited

# %%

if __name__ == '__main__':
    visited = part1()
    print(f"- Part 1: {len(visited)}")

# %%
