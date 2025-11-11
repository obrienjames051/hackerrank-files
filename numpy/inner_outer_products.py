import numpy as np

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

print(np.inner(A, B)) # the inner product is the sum of the elements after the dot product has been performed
print(np.outer(A, B)) # the outer product returns a matrix built from the two inputs. The first line would be a_1b_1, a_1b_2, ..., a_1b_n