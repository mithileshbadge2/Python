# for loop
for x in range(5):
    print(x)
for x in range(1,10):
    print(x)
for x in range(3):
    print('hello')
for x in range(1,11):
    print(x*2)
for x in range(2,21,2):
    print(x)
for x in range(1,11):
    print(x*4)
for x in range(4,41,4):
    print(x)
for x in range(1,11):
    print(x*5)
for x in range(5,51,5):
    print(x)
for x in range(50,4,-5):
    print(x)
for x in range(5,0,-1):
    print(x)
for x in range(100,9,-10):
    print(x)
for x in range(5):
    if x == 2:
        break
    print(x)
for x in range(6):
    if x == 5:
        break
    print(x)
for x in range(5):
    if x == 3:
        continue
    print(x)

# while loop
i1 = 2
while(i1 <= 3):
    print("hello")
    i1 = i1 + 1

i2 = 1
while(i2 <= 5):
    print(i2)
    i2 = i2 + 1

i3 = 5 #table of 5
while(i3 <= 50):
    print(i3)
    i3 = i3 + 5

i4 = 8
while(i4 <= 80):
    print(i4)
    i4 = i4 + 8

i5 = 50
while(i5 <= 500):
    print(i5)
    i5 = i5 + 50

i6 = 500
while(i6 >= 50):
    print(i6)
    i6 = i6 - 50

i7 = 40
while(i7 >= 4):
    print(i7)
    i7 = i7 - 4

# break and continue using while

i8 = 1
while(i8 <= 5):
    print(i8)
    if i8 == 3:
        break
    i8 = i8 + 1

i8 = 1
while(i8 <= 5):
    if i8 == 3:
        break
    print(i8)
    i8 = i8 + 1

i9 = 5
while(i9 >= 1):
    print(i9)
    if i9 == 3:
        break
    i9 = i9 - 1

i10 = 1
while(i10 <= 5):
    if i10 == 3:
        i10 = i10 + 1
        continue
    print(i10)




