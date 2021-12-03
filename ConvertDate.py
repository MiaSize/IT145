
import re

dateRegex = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)')
date = dateRegex.search('15-11-2021')
print(date.group(2)+'-'+date.group(1)+'-'+date.group(3))

#save the date and month and year in different varibles then change the format the groups print in
