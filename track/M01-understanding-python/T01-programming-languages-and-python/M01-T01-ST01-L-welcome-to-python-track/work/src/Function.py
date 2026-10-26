# To add 2 numbers
def add():
    a=10
    b=20
    c=a+b
    print(c)
add()
    # output - 30

## To find the square
def square():
    n = 5
    res = n*n
    print(res)
square()
    # output - 25
    
# To find the largest of 3 numbers
def largest():
    a = 56
    b = 84
    c = 11
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
largest()
    #output - 84

# To find even no
def even():
    n = 89
    if n%2==0:
        print("Even")
    else:
        print("Odd")
even()
    # output - odd

# To greet a name
def greet():
    name = 'Nandhu'
    print("Hello",name)
greet()
    # output - Hello Nandhu

####----- Differnt types of functions--------
# eg1 - for square function
# 1. no input, no output
def square():
    n=5*5
    print(n)
square()
    # output - 25

# 2. no input, output
def square():
    n=5*5
    return n
print(square())
    # output - 25

# 3. input, no output
def square(n):
    print(n*n)
square(4)
    # output - 16   

# 4. input, output
def square(n):
    return n*n
res = square(6)
print(res)
    # output - 36

# eg2 - for even function

# 1. no input, no output
def even():
    n = 38
    if n%2==0:
        print("Even")
    else:
        print("Odd")
even()
    # output - even

# 2. no input, output
def even():
    n = 46
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(even())
    # output - even
    
# 3. input, no output
def even(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
even(89)
    # output - odd

# 4. input, output
def even(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(even(667))
    # output - odd
