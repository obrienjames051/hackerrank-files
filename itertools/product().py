from itertools import product

K, M = map(int, input().split())

lists = []
for _ in range(K):
    data = list(map(int, input().split())) # the map function turns the string input into integers
    lists.append(data[1:]) # [1:] means take everything from index 1 onwards as the first index is just the length of the list

all_combos = product(*lists) # the * takes each element from the list lists giving product() K elements to work with
# the product() function returns all possible combinations when taking one from each element

max_value = 0
for combo in all_combos:
    value = sum(x**2 for x in combo) % M # applies each possible combination to the equation
    max_value = max(max_value, value) #alters the max value if a greater one is found

print(max_value)