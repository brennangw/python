#control flow variable
iterations = 100
loopCount = 0

#variables
a = 1
b = 1
placeholder = 0

#print initial state
print(a)
print(b)

while loopCount < iterations:
    placeholder = b
    b = a + b
    a = placeholder
    loopCount += 1;
    print(b)

