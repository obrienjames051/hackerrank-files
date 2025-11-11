
english = set(map(int, input().split()))
french = set(map(int, input().split()))

students = english.union(french) 
#union merges the two sets and removes duplicates 
# i.e. 1 2 3 merged with 2 3 4 would give 1 2 3 4
# A.union(B) is the same as writing A|B

students = english.intersection(french)
#creates a new set containing only values present in both sets 
# i.e. 1 2 3 and 2 3 4 would be 2 3
# A.intersection(B) is the same as writing A&B

students = english.difference(french) 
#creates a new set using the values in the first taking out overlap with the second 
# i.e. 123 and 234 becomes 1
# A.difference(B) is the same as writing A-B

students = english.symmetric_difference(french) 
#creates a new set containing all values from both that don't overlap 
# i.e. 123 and 345 would be 1245
# A.symmetric_difference(B) is the same as writing A^B

#-----------------------------------------------------------------------------------------------

A = set("abcde")
B = set("abCDE")

A.update(B) 
#this adds all elements from B to A. A becomes a b c d e C D E

A.intersection_update(B) 
#keeps only the elements found in both. A becomes a b

A.difference_update(B) 
#removes elements that overlap. A becomes c d e

A.symmetric_difference_update(B) 
#keeps the elements that are found in either set but not both. A becomes c d e C D E