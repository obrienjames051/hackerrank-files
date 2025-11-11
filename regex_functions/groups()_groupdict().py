#A groups() expression returns a tuple containing all the subgroups of the match.
import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
m.groups()
# > ('username', 'hackerrank', 'com')


#A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
m.groupdict()
# > {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}