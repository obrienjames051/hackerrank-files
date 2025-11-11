from itertools import groupby

# this demonstrates how the groupby() function works
# this takes an input and outputs how many of each consecutive characters there are in the form (g, k) where k is the character and g is the number
data = input()

result = [(int(len(list(g))), int(k)) for k, g in groupby(data)] # k=key is the value being grouped, g=group is the iterator counting consecutive occurrences
print(*result) # the * prints each element of the list, one after another with a space inbetween