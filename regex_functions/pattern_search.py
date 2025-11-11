import re

s = input()
k = input()

pattern = rf"(?={re.escape(k)})"

matches = re.finditer(pattern, s) # finds all overlapping matches of k in s

found = False
for match in matches:
    print((match.start(), match.start()+len(k)-1)) # outputs the start and end index of each match
    found = True

if not found:
    print("(-1, -1)")