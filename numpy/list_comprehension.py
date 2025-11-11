import numpy as np

n = int(input())
A = np.array([list(map(float, input().split())) for _ in range(n)])

print(round(np.linalg.det(A), 2)) # rounds the value to 2 d.p.