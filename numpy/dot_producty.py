import numpy as np

n = int(input())
A = np.array([list(map(int, input().split())) for _ in range(n)]) # creates an array using list comprehension
B = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.dot(A, B)) # determines the dot product of two matrices