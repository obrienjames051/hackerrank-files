import re

pattern = r"(?<=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])[aeiouAEIOU]{2,}(?=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])"
s = input()

matches = re.findall(pattern, s)

if matches: # this finds all cases where there are multiple vowels in a row with consonants on either side
    for m in matches:
        print(m)
else:
    print(-1)