# %% General Function - Look for distinct Characters
from typing import Tuple

def find_marker(s: str, length: int = 4) -> Tuple[str,int]:
    """Finds the marker in the sequence s"""
    start = 0
    while (len(set(s[start:start+length])) != len(s[start:start+length]) and start+length<len(s)):
        start += 1
    return s[start:start+length], start+length

# %% Part 1
def part1():
    with open("input.txt", 'r') as f:
        s,chars = find_marker(f.read(), 4)
        print(f"- Marker: {s}\n- Characters proccessed: {chars}")

# %% Part 2


def part2():
    with open("input.txt", 'r') as f:
        s,chars = find_marker(f.read(), 14)
        print(f"- Marker: {s}\n- Characters proccessed: {chars}")

# %%

if __name__ == '__main__':
    print(f"{5*'-'}> Part 1 <{5*'-'}")
    part1()
    print(f"{5*'-'}> Part 2 <{5*'-'}")
    part2()
# %%
