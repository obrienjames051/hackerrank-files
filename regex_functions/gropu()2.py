import re

pattern = r'([A-Za-z0-9])\1{1,}'
m = re.search(pattern, input())
# this searches the input for a repeated character and stores that group in m. e.g. 111

if m:
    print(m.group(1))
# .group() would return the full match '111'. .group(1) returns just '1' because the brackets in the regex code only allow for one character
# if there were multiple brackets like (\w+)@(\w+).(\w+) then there would be 3 groups
else:
    print("-1")