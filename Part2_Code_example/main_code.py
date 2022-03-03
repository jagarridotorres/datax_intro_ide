
from add_and_exp import function_add_and_exp

results = []
for i in range(0, 2):
    for j in range(0, 3):
        e = function_add_and_exp(i, j)
        results.append(e)

print('Results:', results)
