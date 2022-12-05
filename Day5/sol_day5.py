# %%
""" Idea: Every crate can be represented as a stack """
import itertools
import re
p = re.compile(r'\d+') # Find digits in a string
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

def part1(stack_dict):
    with open('input.txt') as f:
        for line in itertools.islice(f,10,None,1):
            t = list(map(int, p.findall(line)))
            for j in range(t[0]):
                stack_dict[t[2]].push(stack_dict[t[1]].pop())

# %%
def part2(stack_dict):
    with open('input.txt') as f:
        for line in itertools.islice(f,10,None,1):
            t = list(map(int, p.findall(line)))
            crates = [stack_dict[t[1]].pop() for _ in range(t[0])]
            for crate in crates[::-1]:
                stack_dict[t[2]].push(crate)

def write_results():
    f = open('results.txt', 'w')
    f.write("Initial Stack States\n\n")
    stack_dict = initialize_stacks()
    for q in stack_dict.values():
        f.write(str(q) + "\n")
    f.write("\n\n")
    f.write(f"{5*'-'}> Part 1 <{5*'-'}\n")
    part1(stack_dict=stack_dict)
    f.write("Final State:\n")
    for q in stack_dict.values():
        f.write(str(q)+"\n")
    s = ""
    for q in stack_dict.values():
        s += q.pop()
    f.write(f"\nAnswer: {s}\n")
    f.write("\n\n")
    f.write(f"{5*'-'}> Part 2 <{5*'-'}\n")
    stack_dict = initialize_stacks()
    part2(stack_dict=stack_dict)
    f.write("Final State:\n")
    for q in stack_dict.values():
        f.write(str(q)+"\n")
    s = ""
    for q in stack_dict.values():
        s += q.pop()
    f.write(f"\nAnswer: {s}\n")
    f.close()
                

# %%

def main():
    # Part 1
    stack_dict = initialize_stacks()
    part1(stack_dict=stack_dict)
    s = ""
    for q in stack_dict.values():
        s += q.pop()
    print(f"Answer for Part1: {s}")
    # Part 2
    s = ""
    stack_dict = initialize_stacks()
    part2(stack_dict=stack_dict)
    for q in stack_dict.values():
        s += q.pop()
    print(f"Answer for Part2: {s}")

if __name__ == '__main__':
    main()
    # write_results()
