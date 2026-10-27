#-----If statements------
# Program 1: Check whether a number is positive
def positive(n):
    if n > 0:
        print("Positive") 
positive(5)
    # output = Positive

# Program 2: Check wheather a person is eligible to donate blood (Age >=18)
def eligible(age):
    if age>=18:
        print("Eligible") 
eligible(16)
    # output = (nothing bcz condition is false)

# Program 3 Check if the temperature is above 30 degree celcius and print hot day
def temperature(temp):
    if temp>30:
        print("Hot Day")
temperature(34)
    # output = Hot Day

# Program 4: Check wheather a student has attended 75% of the class
def attend(percent):
    if percent>75:
        print("Attended")
attend(87)
    # output = Attended


##-----If-else-------
# Program 5: Check wheather a no is even or odd
def even(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
even(17)
    # output = Odd

# Program 6: Check wheather a person is eligible to apply for driving licence
def dl(age):
    if age>=18:
        print("Eligible")
    else:
        print("Not Eligible")
dl(86)
    # output = Eligible

# Program 7: Check wheather a given year is a leap year
def year(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        print("Leap year")
    else:
        print("Not a Leap yeat")
year(1990)
    # output = Not a Leap year 

# Program 8: Compare two numbers and print the grater number
def greater(n1,n2):
    if n1>n2:
        print(n1)
    else:
        print(n2)
greater(15,54)
    # output = 54


#--------If-elif-else------------
# Program 9: Assign grades based on marks 
            # 90-100 : A
            # 80-89 : B
            # 70-79 : C
            # 60-69 : D
            # Below 60 : Fail
def grade(marks):
    if marks>=90 & marks<=100:
        print("A")
    elif marks>=80 & marks<=89:
        print("B")
    elif marks>=70 & marks<=79:
        print("C")
    elif marks>=60 & marks<=69:
        print("D")
    elif marks<60:
        print("Fail") 
grade(83)
    # output = A

# Program 10: Categorize electricity usuage
              # Above 500 -> High
              # 301-500 -> Medium
              # 101-301 -> Low
              # 0-100 -> Very Low
def electricity(usuage):
    if usuage > 500:
        print("High")
    elif usuage>=301 & usuage<=500:
        print("Medium")
    elif usuage>=101 & usuage<=300:
        print("Low")
    elif usuage>0 & usuage<=100:
        print("Very Low")
electricity(653)
    # output = High

# Program 11: Scholarship Eligibility
              # Marks >= 85
              # Family Income < 3lakh
def eligible(mark,income):
    if mark>=85 & income<300000:
        print("Eligible")
    else:
        print("Not Eligible")
eligible(67,250000)
    # output = Eligible

# Program 12: User login 
              # Username is correct
              # Passwward is correct
set_name="Nandhida"
set_passward="Welcome@1234"
username=input("Enter user name: ")
passward= input("Enter passward: ")
if set_name == username:
    print("Username is correct")
    if set_passward == passward:
        print("Passward is correct")
    else:
        print("Passward is incorrect")
else:
    print("Username is incorrect")
    # output = Username is correct
             # Passward is incorrect


##------Match-case---------------
# Prograam 13: Display weekday using numbers(1-7)
def weekday(day):
    match day:
        case 1: print("Monday")
        case 2: print("Tuesday")
        case 3: print("Wednesday")
        case 4: print("Thursday")
        case 5: print("Friday")
        case 6: print("Saturday")
        case 7: print("Sunday")
        case _ : print("Invalid")
weekday(5)
    # output = Friday

# Program 14: Display season based on month.case
              # Dec, Jan, Feb -> Winter
              # Mar, Apr, May -> Summer
              # Jun, Jul, Aug -> Monsoon
              # Sep, Oct, Nov -> Autumn
def season(month):
    match month:
        case "Dec" | "Jan" | "Feb": print("Winter")
        case "Mar" | "Apr" | "May": print("Summer")
        case "Jun" | "Jul" | "Aug": print("Monsoon")
        case "Sep" | "Oct" | "Nov": print("Autumn")
        case _ : print("Invalid")
season("Dec")
    # output = Winter


##---For Loop----
# Program 15: Print numbers from 1 to 20
def number(n):
    for i in range(n):
        print(i, end=" ")
    print()
number(20)
    # output = 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# Program 16: Print miltiplication table of a given number
def table(n):
    for i in range(1,11):
        res=n*i
        print(f"{n} x {i} = {res}")
table(5)
    # output = 5 table


#------While Loop-----
# Program 17: Print numbers from 10 to 1
def numbers(n):
    while n>=1:
        print(n, end=" ")
        n=n-1
    print( )
numbers(10)
    # output = 10 9 8 7 6 5 4 3 2 1

# Program 18: Find factorial of a number
def factorial(n):
    res=n
    while n>1:
        res=res*(n-1)
        n=n-1
    print(res)
factorial(5)
    # output = 120


#----Break statements----
# Program 19: Print numbers from 1 to 20 but stop at 15
def numbers(n):
    for i in range(1,n+1):
        print(i, end=" ")
        if i==15:
            break
    print( )
numbers(20)
    # output = 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

# Program 20: Search for a number in a list using break
n=[15,21,36,58,24,96,78,41,52,84,16,54]
target = 4
for i in n:
    if i==target:
        print("Found")
        break
print("Not Found")
    # output = Not Found


#----Continue statements----
# Program 21: Print numbers from 1 to 20 skipping multiples of 3
def numbers(n):
    for i in range(1,n+1):
        if i%3==0:
            continue
        print(i,end=" ")
    print( )
numbers(20)
    # output = 1 2 4 5 7 8 10 11 13 14 16 17 19 20

# Program 22: Print Odd numbers from 1 to 50
def numbers(n):
    for i in range(n):
        if i%2==0:
            continue
        print(i,end=" ")
    print()
numbers(51)
    # output = 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49


#----Functions----
# Program 23: Find the cube of a number
def cube(n):
    return n ** 3   # n*n*n, pow(n,3)
print(cube(3))
    # output = 27

# Program 24: Find the maximum of 2 numbers
def maximum(n1,n2):
    if n1>n2:
        print(n1)
    else:
        print(n2)
maximum(15,96)
    # output = 96

#----Pass----
# Program 25: create an empty function named display
def display():
    pass
display()
    # output = (nothings the func is empty)

# Program 26: create an empty class named student
class student():
    pass
    # output = (nothings the class is empty)
