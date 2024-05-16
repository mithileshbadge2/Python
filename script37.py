# p1
import re
str = 'an apple a day keeps doctor away'
# listA = re.findall(r'a[\w]*',str)
listA = re.findall(r'\ba[\w]*',str)
print(listA)

# p2
import re
str = 'The meeting will be conducted on 1st and 11th of this month'
# listB = re.findall(r'\b\d[\w]*',str)
listB = re.findall(r'\b\d[\d]*',str)
print(listB)

# p3
import re