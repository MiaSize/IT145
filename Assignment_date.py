#without
def isPhoneNumber(text):
    if len(text) != 10:
        return False
    for i in range(0,2):
        if not text[i].isdecimal():
            return False
    if text[2] != '/':
        return False
    for i in range(3,5):
        if not text[i].isdecimal():
            return False
    if text[5] != '/':
        return False
    for i in range(6,10):
        if not text[i].isdecimal():
            return False
    return True

print('The date is 11/08/2021:')
print(isPhoneNumber('11/08/2021'))
print('The date is 11/3/2021')
print(isPhoneNumber('11/3/2021'))

#with
import re

phoneNumRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
mo = phoneNumRegex.search('The date is 11/08/2021')
if mo is not None:
    print('Date found:', mo.group())
else:
    print('none')