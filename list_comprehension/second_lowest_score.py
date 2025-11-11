students = [[input(), float(input())] for _ in range(int(input()))]
# takes initial input n for the range, followed by a students name and their respective score

second_lowest = sorted(set([score for name, score in students]))[1]
# makes a list of all scores, takes out duplicates and sorts them in ascending order. The [1] takes the second lowest

for name in sorted([name for name, score in students if score == second_lowest]):
    print(name)
# filters through the list of students and sorts/prints the name of all students who have the second-lowest score