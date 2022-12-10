# %%
import sys

cycles_to_check = {20, 60, 100, 140, 180, 220}

def instructions(file = 'input.txt'):
    with open(file) as f:
        for line in f:
            match line.rstrip("\n").split(" "):
                case ['noop']:
                    yield 'noop'
                case ['addx', val]:
                    yield 'addx', int(val)
# %%

def part1(file = 'input.txt'):
    result = 0
    X = 1
    cycles = 0
    
    for inst in instructions(file):
        if inst == 'noop':
            cycles +=1
            if cycles in cycles_to_check:
                result += X*cycles
        else:
            val = inst[1]
            cycles +=1
            if cycles in cycles_to_check:
                result += X*cycles
            cycles +=1
            if cycles in cycles_to_check:
                result += X*cycles
            X += val
    return result

def part2(input_file: str = 'input.txt', outfile: str  = 'rendered_img.txt'):
    X = 1 # Register
    cycles = 0
    pixel_pos = 0 
    f = open(outfile, 'w')
    for inst in instructions(input_file):
        if inst == 'noop':
            cycles +=1 # During cycle
            f.write("#") if pixel_pos in [X-1, X, X+1] else f.write(".")
            pixel_pos += 1
            if pixel_pos % 40 == 0:
                f.write("\n")
                pixel_pos = 0
        else:
            val = inst[1]
            cycles += 1 # During cycle
            f.write("#") if pixel_pos in [X-1, X, X+1] else f.write(".")
            pixel_pos += 1
            if pixel_pos % 40 == 0:
                pixel_pos = 0
            cycles += 1 # During cycle
            if pixel_pos % 40 == 0: 
                f.write("\n")
                pixel_pos = 0
            f.write("#") if pixel_pos in [X-1, X, X+1] else f.write(".")
            pixel_pos += 1
            if pixel_pos % 40 == 0:
                pixel_pos = 0
                f.write("\n")
            X += val
    f.close()
        
        

# %%

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = 'input.txt'
        
    print(f"- Part 1 Answer: {part1(file)}")
    part2(input_file=file)

# %%
