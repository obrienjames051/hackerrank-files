#list comprehension
fruits = ["apple", "mango", "banana", "orange", "kiwi"]

newlist = [x for x in fruits if "a" in x]
# much shorter way of writing a new list from an existing list using a condition

print(newlist)

# general formula = [expression for value in iterable if condition]