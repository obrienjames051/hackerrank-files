from itertools import combinations

n = input()
letters = input().split() # takes an input of characters and splits into a list
k = int(input())
combos = list(combinations(letters, k)) # combinations outputs all possible combinations of k indices. If k=2 it produces all pairs

count_a = sum(1 for combo in combos if 'a' in combo) # counts how many combinations contain the letter 'a'
probability = count_a / len(combos)

print(probability)