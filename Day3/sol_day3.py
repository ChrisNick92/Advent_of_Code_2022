# %%
from typing import List, Tuple

def priority(s: str) -> int:
    """Returns the priority of letter s"""
    return ord(s) - ord('a') + 1 if s.islower() else \
        ord(s) - ord('A') + 27
# %%
# Part 1
with open('input.txt') as f:
    print(sum([priority(list(set(s[:len(s)//2]) & set(s[len(s)//2:])).pop()) for s in f.read().split("\n")]))
    

# %%
# Part 2
def make_triples(s: List[str]) -> List[List[str]]:
    return [s[i:i+3] for i in range(0,len(s),3)]
# %%
with open('input.txt') as f:
    triples = make_triples(f.read().split("\n"))
    print(sum([priority(list(set(s[0]) & set(s[1]) & set(s[2])).pop()) for s in triples]))
        
# %%
