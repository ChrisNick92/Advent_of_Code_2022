# %%
from typing import Tuple,List

ListOfTuples = List[List[Tuple[int,int]]] # Pairs of intervals
IntervalsStr = List[List[str]]

def contains(I: Tuple[int,int], J: Tuple[int,int]) -> bool:
    """ Return True if either I contains J or J contains I """
    return True if ((I[0]>=J[0] and I[1]<=J[1]) or \
        (J[0]>=I[0] and J[1]<=I[1])) else False

def intersection(I: Tuple[int,int], J: Tuple[int,int]) -> bool:
    """ Return True if I,J have a non empty intersection """
    return False if (I[0] > J[1] or I[1] < J[0]) else True
        
def make_intervals(s: IntervalsStr) -> ListOfTuples:
    intervals = []
    for i in range(0,len(s),2):
        pairs = []
        for pair in s[i:i+2]:
            pairs.append((int(pair[0]), int(pair[1])))
        intervals.append(pairs)
    return intervals
# %% Part 1


with open('input.txt') as f:
    s = []
    for y in f.read().split("\n"):
        for x in y.split(","):
            s.append(x.split("-"))
    intervals = make_intervals(s)
    print(sum([contains(I,J) for I,J in intervals]))

# %% Part 2

with open('input.txt') as f:
    s = []
    for y in f.read().split("\n"):
        for x in y.split(","):
            s.append(x.split("-"))
    intervals = make_intervals(s)
    print(sum([intersection(I,J) for I,J in intervals]))

# %%
