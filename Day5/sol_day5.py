# %%
""" Idea: Every crate can be represented as a stack """
import itertools

class Stack():
    
    def __init__(self, id: int):
        self.stack_lst = []
        self.id = id 
    
    def pop(self):
        return self.stack_lst.pop()
    
    def push(self, item):
        self.stack_lst.append(item)
    
    def __len__(self):
        return len(self.stack_lst)
    
    def isEmpty(self):
        return True if self.__len__() == 0 else False
    
    def __str__(self):
        if self.isEmpty():
            print(f"{self.id}: [] (empty)")
        else:
            out = f"{self.id}: "
            if self.__len__() >= 1:
                for i in range(self.__len__()-1):
                    out += f"[{self.stack_lst[i]}]->"
            out += f"[{self.stack_lst[-1]}] (top)"
        return out

    def reverse_stack(self):
        reversed_stack = []
        while not self.isEmpty():
            reversed_stack.append(self.pop())
        self.stack_lst = reversed_stack

# Initialize Stacks
def initialize_stacks() -> dict:
    stack_dict = {}
    for i in range(1,10):
        stack_dict[i] = Stack(i)
    # Fill stacks
    with open('input.txt') as f:
        for line in itertools.islice(f,0,8):
            for id,col in enumerate(range(1,len(line),4)):
                if line[col].isalpha():
                    stack_dict[id+1].push(line[col])
    for s in stack_dict.values():
        s.reverse_stack()
    return stack_dict
# %% Part 1
stack_dict = initialize_stacks()

for s in stack_dict.values():
    print(s)

# %% Solving Part 1
import re 
p = re.compile(r'\d+') # find digits in a string

with open('input.txt') as f:
    for line in itertools.islice(f,10,None,1):
        t = list(map(int, p.findall(line)))
        for j in range(t[0]):
            stack_dict[t[2]].push(stack_dict[t[1]].pop())

# %% Print Final State of Stacks
for s in stack_dict.values():
    print(s)
# %% Part 2 - Just Push Crates in Reverse order

stack_dict = initialize_stacks()
for s in stack_dict.values():
    print(s)
# %%

with open('input.txt') as f:
    for line in itertools.islice(f,10,None,1):
        t = list(map(int, p.findall(line)))
        crates = [stack_dict[t[1]].pop() for _ in range(t[0])]
        for crate in crates[::-1]:
            stack_dict[t[2]].push(crate)
# %% Print Final State of Stacks
for s in stack_dict.values():
    print(s)

# %%
