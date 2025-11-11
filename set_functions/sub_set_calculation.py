outcomes = []

T = int(input())

for _ in range(T):
    number_A = int(input()) #number of elements in A
    A = set(map(int, input().split())) #the elements in A
    number_B = int(input())
    B = set(map(int, input().split()))
    C = set(B)
    C.update(A) #adds A to C
    if C == B: #if C is unchanged, then A is a subset of B
        outcomes.append("True")
    else: # if C is different to B, A is not a subset
        outcomes.append("False")

for i in range(len(outcomes)):
    print(outcomes[i])