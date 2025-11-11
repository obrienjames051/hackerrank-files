import numpy as np

n, m = map(int, input().split())
rows = []

for _ in range(n):
    row = list(map(int, input().split()))
    rows.append(row)

my_array = np.array(rows)

print(np.mean(my_array, axis=1)) # mean works out the mean across the specified axis
print(np.var(my_array, axis=0)) # var works out the variance across the specified axis
print(np.std(my_array, axis=None)) # std works out the standard deviation across the specified axis