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


###-----local and global variables----

c=50      # global variable
def add():
    a=10    # local variable
    b=20    # local variable
    print(a+b)  # output - 30
add()
print(c)   #output - 50
##print(a)   #error

# converting local to global
c=50      # global variable
def add():
    global a
    a=10    # global variable
    b=20    # local variable
    print(a+b)  # output - 30
add()
print(c)   #output - 50
# print(a)   #output - 10


# giving importance to local variable
x = 100     # global
def demo():
    x = 20     # local
    print(x)   #output - 20
demo()
print(x)    #output - 100

x=10
def display():
    print(x)
display()
print(x)

x=10
def display():
    print(x)
    # x=20
display()
x = 30
print(x)

##-----Function Overloading----

def add(a,b):
    print(a+b)
def add(a,b,c):
    print(a+b+c)
# add(10,20)     # output - error
add(10,20,30)  # 60

# To overcome the error we have
# 1. Default arguements
def add(a,b=0,c=0):
    print(a+b+c)
add(10)      # output - 10
add(10,20)   # output - 30
add(10,20,30)# output - 60
# add()        # output - error

# 2. Var-args (*args)
def add(*args):
    total = 0
    for i in args:
        total += i
    return total
print(add(10))      # output - 10
print(add(10,20))   # output - 30
print(add(10,20,30))# output - 60
print(add())        # output - 0 

def add(*args):
    print(sum(args))
add(10)      # output - 10
add(40,50,60)   # output - 30

# **kwargs
def display(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
display(name="Nandhida",age=22,gender="Female")
        # output - name Nandhida
        #          age 22
        #          gender Female

def display(**kwargs):
    print(f"Name is {kwargs.get('name')} ", end="")
    print(f"Age is {kwargs.get('age')} ", end="")
    print(f"Gender is {kwargs.get('gender')}")
display(name="Nandhida",age=22,gender="Female")    


##-----Recursive Function-----

# print numbers 1 to n
def display(n):
    if n == 0:
        return
    display(n-1)
    print(n)
display(5)

# print numbers n to 1
def display(n):
    if n == 0:
        return
    print(n)
    display(n-1)
display(5)

# to print factorial of a number
def fact(n):
    if n==0 or n ==1:
        return 1
    return n*fact(n-1)
print(fact(7))

# fibonacci series
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(4))

# first five fibonacci series
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
n=5
for i in range(n):
    print(fib(i),end=" ")
