regex_integer_in_range = r"^[1-9]\d{5}$"	# this checks that it is between 100000 and 999999
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"	# this checks that there are not repeated numbers 2 apart i.e. 121345
# (? ... ) means look ahead and catches everything, even if they overlap
# the second \d means separated by a digit

import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)