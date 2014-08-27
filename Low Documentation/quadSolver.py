print ("Welcome to the simple positive quadratic solver.")
print ("To start you'll need a polynomial in thefollowing format: x^2 + bx + c")


b = int(input("b:"))
c = int(input("c:"))

#find numbers that add to b and are factors of c
diff = 0
suber = b
while suber >= 0:
    diff = b - suber
    if diff*suber == c:
        break
    else:
        suber = suber - 1;
print(diff, suber)

print("( x +",diff,")( x +",suber,")")

#for the future
#print("(",a,"x +",diff,")( x +",suber,")")
