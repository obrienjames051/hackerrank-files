def split_and_join(line):
    line = line.split(" ") #splits a string at all spaces, line becomes a list
    line = "-".join(line) #joins the list elements with hyphens in between
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)