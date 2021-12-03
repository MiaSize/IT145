
import re

sevenRegex = re.compile(r'\w\w\w\w\w\w\w')
print(sevenRegex.findall('You are wearing googles.'))
