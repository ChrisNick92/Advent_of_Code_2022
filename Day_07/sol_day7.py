# %%
""" Represent the filesystem as a tree
 where leaves are the files and empty directories 
"""
from typing import Tuple

class directory():
    def __init__(self, dir_name: str):
        self.subdirectories = {}
        self.size = 0
        self.name = dir_name
        self.parent_dir = None

# %%
def track_filesystem(ROOT_DIR: directory):
    current_dir = ROOT_DIR
    with open("input.txt") as f:
        for line in f:
            match line.rstrip("\n").split(" "):
                case ['dir', dir_name]: # Append subdirectory
                    current_dir.subdirectories[dir_name] = directory(dir_name)
                    current_dir.subdirectories[dir_name].parent_dir = current_dir
                case [file_size, *others] if file_size.isdigit():
                    current_dir.size += int(file_size)
                case ['$', 'cd', '..']: # Go to parent
                    current_dir = current_dir.parent_dir
                case ['$', 'cd', dir_name] if dir_name != '/':
                    current_dir = current_dir.subdirectories[dir_name]

def calculate_subdir_sizes(dir: directory) -> directory:
    if dir.subdirectories: # If there are other subdirectories use recursion
        for sub_dir in dir.subdirectories.values():
            calculate_subdir_sizes(sub_dir)
            dir.size += sub_dir.size
    if dir.name == '/':
        return dir
    
def part1(dir: directory, UPPER_BOUND: int = 100000) -> int:
    total_sum = dir.size if dir.size <= UPPER_BOUND else 0
    if dir.subdirectories:
        for sub_dir in dir.subdirectories.values():
            total_sum += part1(sub_dir, UPPER_BOUND=UPPER_BOUND)
    return total_sum

import math

def part2(dir:directory, unused_space: int,
          update_space: int = 30000000) -> Tuple[directory, int]:
    dir_query = (dir, unused_space+dir.size-update_space) if \
        (unused_space+dir.size-update_space) >= 0 else (dir, math.inf)
    if dir.subdirectories:
        for sub_dir in dir.subdirectories.values():
             sub_query = part2(sub_dir, unused_space)
             dir_query = dir_query if dir_query[1] < sub_query[1] else sub_query
    return dir_query


if __name__ == '__main__':
    # Track filesystem
    ROOT_DIR = directory('/')
    track_filesystem(ROOT_DIR=ROOT_DIR)

    # Calculate directory sizes
    ROOT_DIR = calculate_subdir_sizes(ROOT_DIR)
    
    # Part 1
    print(f"- Part 1 Answer: {part1(ROOT_DIR)}")
    
    # Part 2
    DISK_SPACE = 70000000
    FREE_SPACE = DISK_SPACE - ROOT_DIR.size
    dir,_ = part2(ROOT_DIR, FREE_SPACE)
    print(f"- Part 2 Directory: {dir.name}, Space: {dir.size}")
