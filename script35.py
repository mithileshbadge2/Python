# p1
# only one occurence
import re
str = "man pan run pop"
result = re.search(r'm\w\w',str)
# print(result.group())
if result:
    print(result.group())

# p2
# gives all the occurences
str2 = "man ran sun fun rap map mate fate shape"
list2 = re.findall(r'm\w\w',str2)
print(list2)

# p3
str2 = "python is good language to learn"
q3 = re.match(r'p\w\w',str2)
# print(q3.group())
if q3:
    q3.group()


# p4
# \W --- non alpha - numeric
import re
str3 = "This ; is the : 'Core' python's book"
result = re.split(r'\W+',str3)
print(result)

# p5
str4 = "i am learning javascript"
q4 = re.sub(r"javascript","python",str4)
print(q4)


# re.search() # only one occurence
# re.findall()
# re.match()
# re.split()
# re.sub()