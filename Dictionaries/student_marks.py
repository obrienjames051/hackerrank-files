n = int(input())
student_marks = {} #dictionary
for _ in range(n):
    name, *line = input().split() # splits the input into name, and a list of scores. The * means put everything else in a list
    scores = list(map(float, line)) # this stores that list of scores into 'scores' and turns the elements into floats
    student_marks[name] = scores # this adds the name and list of scores to the dictionary student_marks as a key-value pair
query_name = input()

average = sum(student_marks[query_name]) / 3 # searches for the 'key' in the dictionary, which takes the 'value' to use

print(f"{average:.2f}") # prints as 2 d.p.