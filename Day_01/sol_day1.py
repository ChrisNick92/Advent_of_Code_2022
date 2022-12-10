# %%
import pandas as pd

d = {'Calories': [], 'Elf_ID': []}

with open('input.txt') as f:
    for id,s in enumerate(f.read().split("\n\n")):
        values = list(map(lambda x: int(x), s.split('\n')))
        d['Calories'] += values
        d['Elf_ID'] += len(values)*[id+1]

df = pd.DataFrame(d).groupby(by = 'Elf_ID').sum()


# %%
# Part 1
print(f"Max calories: {int(df.max())}")

# %%
# Part 2
df.sort_values(by = 'Calories', ascending=False,
               inplace=True)
print(f"Top three: {int(df.iloc[:3].sum())}")

# %%