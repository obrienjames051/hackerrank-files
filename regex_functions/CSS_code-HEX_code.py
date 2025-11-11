import re #this program takes a CSS input and extracts all the valid HEX codes

matches = []
pattern = r'#(?:[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})(?=;|,|[^(]*\))'
# (?: ... ) - non-capturing group. Same as ( ... ) but you can't call each element by match.group(1)
# [0-9A-Fa-f]{6} - a string of these characters that is 6 characters long
# | - or
# (? ... ) - positive lookahead - the match must be followed by this pattern, but don't include it in the match
# ;|[^(]*\) - ; or , or [^(]* zero or more characters that are not ( then followed by a ) with \)
# above means it's a match if it's followed by ; or , or it's followed by a string of any length of any characters that ends with ) and doesn't contain (

n = int(input())

for _ in range(n):
    CSS = input()
    find = re.findall(pattern, CSS) # finds every part of CSS that matches pattern
    for match in find:
        matches.append(match)

for i in range(len(matches)):
    print(matches[i])