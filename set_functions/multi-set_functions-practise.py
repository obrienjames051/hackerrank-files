int(input())
A = set(map(int, input().split())) #starting set
n = int(input())

for i in range(n):
    x = list(map(str, input().split())) #reads the operation wanting to be performed + the number of items in new set
    N = set(map(int, input().split())) #new set
    if x[0] == 'update':
        A.update(N)
    elif x[0] == 'intersection_update':
        A.intersection_update(N)
    elif x[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(N)
    elif x[0] == 'difference_update':
        A.difference_update(N)

print(sum(A))