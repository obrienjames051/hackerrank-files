import re

result = []

t = int(input())

for _ in range(t):
    UID = input().strip()

    if not re.fullmatch(r"[0-9A-Za-z]{10}", UID): #checks that it is alphanumeric and 10 characters long
        result.append("Invalid")
        continue

    if len(re.findall(r"[A-Z]", UID)) < 2: #checks that it has at least 2 uppercase characters
        result.append("Invalid")
        continue

    if len(re.findall(r"[0-9]", UID)) < 3: #checks that it has at least 3 digits
        result.append("Invalid")
        continue

    if len(set(UID)) != len(UID): #checks for repeating characters
        result.append("Invalid")
        continue

    result.append("Valid")


for res in result:
    print(res)