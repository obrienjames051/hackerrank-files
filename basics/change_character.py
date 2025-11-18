def mutate_string(string, position, character):
    # Replace the character at the exact position using slicing.
    # Using str.replace() replaces the first matching character anywhere in
    # the string, not necessarily the one at `position`.
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)