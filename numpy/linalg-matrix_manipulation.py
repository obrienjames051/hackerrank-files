import numpy as np
# linalg is a sub-module of numpy used for linear algebra

print(np.linalg.det([[1, 2], [2, 1]]))       #Output : -3.0
# works out the determinant of an array

vals, vecs = np.linalg.eig([[1 , 2], [2, 1]])
print(vals)                                      #Output : [ 3. -1.]
print (vecs)                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]
# works of the eigenvalue and right eigenvectors of a square array

print(np.linalg.inv([[1 , 2], [2, 1]]))       #Output : [[-0.33333333  0.66666667]
                                                #          [ 0.66666667 -0.33333333]]
#works out the inverse of a matrix