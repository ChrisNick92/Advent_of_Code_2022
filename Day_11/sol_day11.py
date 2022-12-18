# %%
from collections import deque
import re

r = re.compile(r'(\d+)')

class monkey():
    
    def __init__(self, id: int):
        self.items = None
        self.id = id
        self.oper_type = None
        self.oper_const = None
        self.test_const = None
        self.monkeys = {True: None, False: None}
        self.inspections = 0
        self.monkey_true = None
        self.monkey_false = None
    
    def operation(self, old: int) -> int:
        if self.oper_type == 'Special':
            return old * old
        elif self.oper_type == '*':
            return old*self.oper_const
        elif self.oper_type == '+':
            return old + self.oper_const
    
    def test(self, new: int) -> int:
        return new % self.test_const
            
def initialize_monkeys(file: str = 'input.txt'):
    monkeys = []
    with open(file) as f:
        s = f.read().split("\n\n")
        for i,info in enumerate(s):
            m = monkey(id = i)
            info = info.split("\n")[1:]
            for line in info:
                line = line.strip()
                if line.startswith("Starting"):
                    items = list(map(int, re.findall(r,line)))
                    m.items = deque(items)
                elif line.startswith("Operation"):
                    try:
                        oper_const = list(map(int, re.findall(r,line)))
                        m.oper_const = oper_const[0]
                        if '*' in line:
                            m.oper_type = '*'
                        else:
                            m.oper_type = '+'
                    except:
                        m.oper_type = 'Special'
                elif line.startswith("Test"):
                    test_const = list(map(int, re.findall(r,line)))
                    m.test_const = test_const[0]
                elif line.startswith("If true"):
                    true_id = list(map(int, re.findall(r,line)))
                    m.monkeys[True] = true_id[0]
                elif line.startswith("If false"):
                    false_id = list(map(int, re.findall(r,line)))
                    m.monkeys[False] = false_id[0]
            monkeys.append(m)
    for m in monkeys:
        m.monkey_true = monkeys[m.monkeys[True]]
        m.monkey_false = monkeys[m.monkeys[False]]
    return monkeys
# %%
def part1(file: str = 'input.txt', rounds: int = 20):
    monkeys = initialize_monkeys(file)
    for round in range(rounds):
        for m in monkeys: # Each monkey takes turn
            while m.items:
                item = m.operation(m.items.popleft()) // 3
                m.inspections += 1
                r = m.test(item)
                if r == 0:
                    m.monkey_true.items.append(item)
                else:
                    m.monkey_false.items.append(item)
    # Find the product of two monkeys with highest inspections
    insp = []
    for m in monkeys:
        insp.append(m.inspections)
    insp = sorted(insp, reverse=True)
    return insp[0]*insp[1]

def part2(file: str = 'input.txt', rounds: int = 10000):
    monkeys = initialize_monkeys(file)
    for round in range(rounds):
        for m in monkeys: # Each monkey takes turn
            while m.items:
                item = m.operation(m.items.popleft())
                m.inspections += 1
                r = m.test(item)
                if r == 0:
                    m.monkey_true.items.append(m.test_const)
                else:
                    m.monkey_false.items.append(r)
    # Find the product of two monkeys with highest inspections
    insp = []
    for m in monkeys:
        insp.append(m.inspections)
    insp = sorted(insp, reverse=True)
    return insp[0]*insp[1]
            
# %%
if __name__ == '__main__':
    print(f"Part 1 Answer: {part1('sample.txt')}\nPart 2 Answer: {part2('sample.txt')}")
# %%
