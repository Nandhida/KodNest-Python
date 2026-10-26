#Arithemetic operators
print(3+3)    # 6
print(3-3)    # 0
print(3*3)    # 9
print(3/3)    # 1.0
print(3%3)    # 0
print(3**3)   # 27
print(10//3)  # 3

#comparison operators
print(11 ==11)      #True
print(11 != 10)     #True
print(11 > 10)      #True
print(10 < 11)      #True
print(11 >=10)      #True
print(11 <= 10)     #False

#Assignment Operator
a = 10
print(a)        #10
a += 10         #20
print(a)
a -= 10         #10
print(a)
a *= 10         #100
print(a)
a /= 10         #10.0
print(a)
a %= 10         #0.0
print(a)
a **= 10        #0.0
print(a)
a //= 10        #0.0
print(a)

#Logical operators
a = True
b = False
print(a and b)      #False
print(a or b)       #True
print(not b)        #True

a = (5 > 3) and (4 < 6) #True
a = (5 < 3) or (4 < 6)  #True
a = not (5 > 3)         #False

#identity operators
a = "python"
b = "Python"
print(a is b)       #False
print(a == b)       #False

a = "python"
b = "python"
print(a is b)       #True
print(a == b)       #True

a = [1,2,3]
b = [1,2,3]         #since tuples are mutable they are stored in differnt loc so their address are different
print(a is b)       #False
print(a == b)       #True

#Membership operators
a= 10
b = [1,2,3,4,5]
print(a in b)       #True
print(a not in b)   #False

#Bitwise Operators
a = 2
b = 3
print(a & b)    #2       #and          
print(a | b)    #3       #or
print(a ^ b)    #1       #xor
a = 5
print(~a)       #-6      #not
print(a >> b)   #0       #right shift
print(a << b)   #40      #left shift