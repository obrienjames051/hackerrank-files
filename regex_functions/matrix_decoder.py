import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0]) #rows
m = int(first_multiple_input[1]) #columns

matrix = []
decoded = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for i in range(m):
    for j in range(n):
        decoded.append(matrix[j][i])

joint = ''.join(decoded)

cleaned = re.sub(r'(?<=\w)[^A-Za-z0-9]+(?=\w)', ' ', joint)

# (?<= ... ) means only match something if it is preceded by ...  \w means alphanumeric characters
# (?<=\w) - positive lookbehind - means there must be an alphanumeric character before the thing we match
# [^A-Za-z0-9]+ means match anything not in the brackets, + means one or more
# (?=\w) - positive lookahead - only match something if it is followed by \w

print(cleaned)