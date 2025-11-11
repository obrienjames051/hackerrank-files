# .sub() and .end() return the indices of the start and end of the substring matched by the group

import re
m = re.search(r'\d+','1234')
m.end() # output: 4
# ^ matches the index after the final one as it is none inclusive
m.start() # output: 0
