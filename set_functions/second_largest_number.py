# this takes a series of numbers and outputs the second largest
n = int(input())
arr = list(map(int, input().split()))

unique = list(set(arr))
unique.sort(reverse=True)

print(unique[1])