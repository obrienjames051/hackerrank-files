def solve(s):
    names = s.split(' ') #splits the input into a list
    new = []
    for i in names:
        i = i.capitalize() #.capitalize() capitalises the first letter of the string
        new.append(i) #adds the capitalised version to a new list
    return ' '.join(new) #joins it all together back into one string

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)