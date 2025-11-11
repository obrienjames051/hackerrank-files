import re

# this takes an input and returns True or False depending on whether it is a valid roman numeral
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

print(bool(re.match(regex_pattern, input())))