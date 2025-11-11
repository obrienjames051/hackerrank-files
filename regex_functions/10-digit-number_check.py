import re

pattern = r"^[789]\d{9}$"
# ^: start of the string
# [789]: first digit must be 7, 8, or 9
# \d{9} exactly 9 digits after the first one
# $ end of the string
result = []

n = int(input())

for _ in range(n):
    number = input()
    if re.match(pattern, number): #this checks to see if 'number' has a 'match' following 'pattern'
        result.append("YES")
    else:
        result.append("NO")

for res in result:
    print(res)