# a module is basically a file containing a set of functions to include in your application.
#there are core pythn modules, modules you can install using the pip packet manager,
#(including Django) as well as custom modules

# using import

from datetime import date # (OR) import datetime
today = date.today()      # today = datetime.date.today
print(today)              # print(today)

from time import time
timetoday = time()
print(timetoday)

# pip module
'''
from camelcase import CamelCase
c = CamelCase()
print(c.hump("harsh dwivedi"))
'''
# using valodator
from validator import validate_email
email = "harsh@dwivedi.com"
if validate_email(email):
    print("Email is valid")
else:
    print("invalid Email")


















