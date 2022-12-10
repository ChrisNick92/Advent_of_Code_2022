# %%
from typing import Tuple, Optional, Set

point = Tuple[int,int]

class small_rope():
    def __init__(self, head: Optional[point],
                 tail: Optional[point] = None):
        self.head = head
        self.tail = tail

class rope():
    def __init__(self, length: int = 2):
        self.length = length
        self.knots = [(0,0) for _ in range(length)] # [head_pos,...,tail_pos]
        self.tail_moved = False
    
    def update(self, head_move: Tuple[int, int]):
        self.knots[0] = head_move
        for i in range(self.length-1):
            front, back = self.knots[i], self.knots[i+1]
            if front != back and not self.condition(back, front):
                self.knots[i+1] = self.move_knot(back, front)
                if i+1 == self.length-1: # Tail moved
                    self.tail_moved = True
            else:
                break
    
    def condition(self, new_pos: point, front_knot: point) -> bool:
        return (manhattan_dist(new_pos , front_knot) == 1) or\
            ((new_pos[0]-front_knot[0])**2 + (new_pos[1]-front_knot[1])**2 == 2)
    
    def move_knot(self, curr_knot: point,
                    front_knot: point) -> point:
        x,y = curr_knot
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1),
                    (-1,-1), (1,-1)] # [East (E), West (W), North (N), South (S), NE, NW, SW, SE]
        for i,j in directions:
            x_prime, y_prime = x+i, y+j
            if self.condition((x_prime,y_prime), front_knot):
                return x_prime, y_prime

        
def move_head(curr_head_pos: point, move: str) -> point:
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
        
def track_tail(length: int = 2) -> Set[point]: # Length of rope
    r = rope(length=length)
    visited = set()
    
    for move, steps in moves():
        for step in range(steps):
            r.update(move_head(r.knots[0], move))
            if r.tail_moved:
                visited.add(r.knots[-1])
                r.tail_moved = False
    return visited
            
    

# %%

if __name__ == '__main__':
    print(f"- Part 1: {len(track_tail(length=2))}")

# %%
