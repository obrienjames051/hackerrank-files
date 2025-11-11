n = int(input())
s = set(map(int, input().split())) #splits the input into elements and adds them to a set
commands = int(input())

for _ in range(commands):
    x = input()
    if x == 'pop':
        s.pop() #removes an element. If set is defined by {} it removes from the left, if set is defined by ([]) it removes from the right
    elif x.startswith('remove'):
        z = x.split()
        s.remove(int(z[1])) #second portion of the input is a number wanting to be removed
    elif x.startswith('discard'):
        z = x.split()
        s.discard(int(z[1])) ##second portion of the input is a number wanting to be discarded

print(sum(s))