import numpy

n, m = map(int, input().split())

rows = [] # dummy list to make building the array easier

for _ in range(n):
    row = list(map(int, input().split()))
    rows.append(row)

my_array = numpy.array(rows) # converts list to a numpy array
# numpy arrays are easier to manipulate than lists as they require less code. They also use less computing power
# numpy arrays can hold any data type, but all entries must be the same type.

min = numpy.min(my_array, axis=1) # axis = 1 works with the rows in the matrix. axis = 0 works with the columns
max = numpy.max(min) # no axis or axis = none uses all the data points

print(max)