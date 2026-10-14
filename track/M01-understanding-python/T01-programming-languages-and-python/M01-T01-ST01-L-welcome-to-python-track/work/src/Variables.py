#Variable - A name given to the memory location to access and store the data

name = "Nandhida"

print(name)
print(id(name))  #address of the variable
print(type(name)) # type of the variable

print("Hello python")
print("Thank you Python")

print("Hello python", end=" ")             #end=" " - to print the next string in the same line
print("Thank you Python")                  #end is the parameter

print("Hello python \nThank you Python")   #\n is an escape sequence character

print("Hello python", end=" - ") 
print("Thank you Python")

# My name is Nandhida and age is 22 
age = 22
print("My name is " + name + " and age is", age)

print("My name is " + name + " and age is "+ str(age))   #str() - type casting

# String formatting
print(f"My name is {name} and age is {age}")   #f string 