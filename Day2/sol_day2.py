# %%
# Part 1
scores = {'AX': 4, 'AY': 8, 'AZ':3,
          'BX':1, 'BY':5, 'BZ':9,
          'CX':7, 'CY':2, 'CZ':6}

with open('input.txt') as f:
    print(sum([scores[s.replace(" ","")] for s in f.read().split("\n")]))
# %%

result_score = {'DRAW': 3, 'LOSE': 0 , 'WIN':6}
weights = {'A': 1, 'B': 2, 'C': 3}
tactic = {'Z': 'WIN', 'X': 'LOSE', 'Y': 'DRAW'}
corr = {'A': {'DRAW': 'A', 'LOSE': 'C', 'WIN': 'B'},
        'B': {'DRAW': 'B', 'LOSE': 'A', 'WIN': 'C'},
        'C': {'DRAW': 'C', 'LOSE': 'B', 'WIN': 'A'}}

with open('input.txt') as f:
    res = 0
    for s in f.read().split("\n"):
        i,j = tuple(s.split(" "))
        res += weights[corr[i][tactic[j]]] + result_score[tactic[j]]
print("Total score: ", res)
# %%
