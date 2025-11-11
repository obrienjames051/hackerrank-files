import re
import email.utils

valid = []
pattern = r'^[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
# ^[a-zA-Z] - first character must be a letter
# [\w.-]* - any following characters must be letters, numbers, or . - _
# [a-zA-Z]{1,3} - any letter and have length 1 to 3

n = int(input())

for i in range(n):
    line = input()
    name, address = email.utils.parseaddr(line) #this takes a string and returns it as a tuple e.g. Name <email@domain.com> becomes (Name, email_address)
    match = re.search(pattern, address)
    if match:
        valid.append(email.utils.formataddr((name, address))) #takes a tuple and returns a formated string e.g. (Name, email_address) becomes Name <email@domain.com>

for i in range(len(valid)):
    print(valid[i])