# p1
import re
str = 'an apple a day keeps doctor away'
# listA = re.findall(r'a[\w]*',str)
listA = re.findall(r'\ba[\w]*',str)
print(listA)

# p2
import re
str = 'The meeting will be conducted on 10th and 30th of this month'

# p3
# listB = re.findall(r'\b\d[\w]*',str)
listB = re.findall(r'\b\d[\d]*',str)
print(listB)

# p4
import re
str = "one two three four five six seven 8 9 10"
listC = re.findall(r'\b\w{4}\b',str)
print(listC)

# listC = re.search(r'\b\w{5}\')