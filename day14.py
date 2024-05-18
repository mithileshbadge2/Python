first_name = "mithilesh"
q1 = first_name.upper()
print(q1)


last_name = "BADGE"
q2 = last_name.lower()
print(q2)

last_name = "vedant"
q3 = last_name.capitalize()
print(q3)


# program 1

city = "PUNE"
q4 = city.isupper()
print(q4)

city2 = "Nagpur"
q5 = city2.islower()
print(q5)

info = "1232a43243244"
q6 = info.isdigit()
print(q6)

info = "abc"
q7 = info.isalpha()
print(q7)

info = "a"
q8  = info.isalnum() 
print(q8)

# program 3
city = "i am learning js"
q9 = city.replace("js","python")
print(q9)


info = ["monty","badge","9168076805"]
q10 = "@".join(info)
print(q10)

fruit = "apple"
q11 = fruit.endswith('le')
q12 = fruit.endswith('e')
q13 = fruit.startswith('a')
q14 = fruit.startswith('ap')
print(q11)
print(q12)
print(q13)
print(q14)

str = " goa "
print(len(str))

# q15 = str.lstrip()
# print(q15)
# print(len(q15))

# q16 = str.rstrip()
# print(q16)
# print(len(q16))

q17 = str.strip()
print(q17)
print(len(q17))


city = "wardha"
# 0  1  2  3  4   5
# w  a  r  d  h   a
q18 = city.index("d")
print(q18)