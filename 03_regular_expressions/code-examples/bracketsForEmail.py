import re

email = 'email codezoners-2@artech.cc for help'

## find email address
match = re.search(r'[\w-]+@[\w.]+', email)

if match: print 'example 1 -> I found: ', match.group()
else: print 'example 1 -> not found'
