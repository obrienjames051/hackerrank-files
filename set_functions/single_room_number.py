K = int(input())
room_numbers = list(map(int, input().split())) #takes an input of lots of room numbers
s = set()
a = set()

for i, item in enumerate(room_numbers): #this function runs through room_numbers and adds them to the set s, if it is already in s then it adds it a
    if item in s:
        a.add(item)
    elif item not in s:
        s.add(item)

s.difference_update(a) #this then compares s and a and removes any overlap, leaving the one room with only one entry
print(sum(s))