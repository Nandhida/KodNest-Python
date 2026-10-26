#Variable - A name given to the memory location to access and store the data

name = "Nandhida"

print(name)
    # Nandhida

print(id(name))  #address of the variable
    # 1883010552816

print(type(name)) # type of the variable
    # <class 'str'>

print("Hello python")
print("Thank you Python")
    # Hello python
    # Thank you Python

print("Hello python", end=" ")             #end=" " to print the next string in the same line
print("Thank you Python")                  #end is the parameter
    # Hello python Thank you Python

print("Hello python \nThank you Python")   #\n is an escape sequence character
    # Hello python
    # Thank you Python

print("Hello python", end=" - ") 
print("Thank you Python")
    # Hello python -Thank you Python

# My name is Nandhida and age is 22 
age = 22
print("My name is " + name + " and age is", age)
    # My name is Nandhida and age is 22

print("My name is " + name + " and age is "+ str(age))   #str() - type casting
    # My name is Nandhida and age is 22

# String formatting f string 
print(f"My name is {name} and age is {age}")   
    # My name is Nandhida and age is 22

a = 10
b = 20
c = 30

print(a+b+c)
    # 60

a,b,c = 5,10,15
print(a+b+c)
    # 30

a=b=c=10
print(a+b+c)
    # 30

a,b,c = "Abhi", "Nandha", "Monisha"
print (a + b + c)
    # AbhiNandhaMonisha

print(b)
    # Nandha

x,y,z = 30,4,8
print(x+z)
    # 38

print(a+str(x))
    # Abhi30

print(b + c)
    # NandhaMonisha

print(a, x)   #, by default takes single space
    # Abhi 30

#Dynamic Typing - assigning a datatype to the variable during runtime is called dynamic typing

