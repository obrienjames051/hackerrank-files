import re

result = []
n = int(input())

for _ in range(n):
    number = input()

    chunks = number.split('-')
    invalid = False #just used to help skip the outer loop if the inner loop catches something

    if len(chunks) != 1: #this only runs if the number is split by '-', otherwise it skips it
        for i in chunks:
            if len(i) != 4: #checks to make sure each groups has exactly 4 digits
                result.append("Invalid")
                invalid = True
                break
        if invalid:
            continue

    number = ''.join(chunks)

    if not re.fullmatch(r"^[456]\d{15}$", number): #checks that it starts with 4, 5, or 6 and 16 characters long
        result.append("Invalid")
        continue

    if re.findall(r"(\d)\1{3,}", number):
        result.append("Invalid")
        continue

# (/d) - 'capture' any digit and hold it/remember it
# \1 - backreference, it means the exact same text matched by the capturing group
# {3,} - repeat the previous token 3 times

    result.append("Valid")


for res in result:
    print(res)