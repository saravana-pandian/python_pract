from math import *
is_male = True
def practise(c_name):
    coad = (5, 20)
    n1 = 20
    n2 = 80
    n = n1 + n2
    print(c_name.isupper())
    print(len(c_name))
    print(" ________ ")
    print("|   " + c_name.upper() + "    |")
    print("|   " + c_name.upper() + "    |")
    print("|   " + c_name.lower() + "    |")
    print("|   " + c_name + "    |")
    print("|________|")
    print(c_name[5])
    print(sqrt(36))
    print(n)
    print(coad[0])
    print(coad[1])
def los(hello):
    return hello*hello*hello
def ifstat():
    if is_male:
        print("You are Male")
    else:
        print("You Arw Female")
print("Hello angel, dharshini")
def calc():
    print("basic calculator")
    x = float(input("Enter the number"))
    y = input("Enter the operator")
    z = float(input("Enter the num2"))
    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "/":
        print(x / z)
    elif y == "*":
        print(x * z)
    else:
        print("Unnkonown Operator")
def nameloop():
    for letter in "Saravana":
        print(letter)
def library():
    MonthConversion = {
        "jan": "January",
        "feb": "February",
        "mar": "March",
        "apr": "April",
        "may": "May",
        "jun": "June",
        "jul": "July",
        "aug": "August",
        "sep": "September",
        "oct": "October",
        "nov": "November",
        "dec": "December",
    }
    print(MonthConversion["nov"])

def guess():
    secret = "rat"
    g = ""
    gc = 0
    gl = 3
    og = False
    while g != secret and not(og):
        if gc < gl:
            g = input("Guess The animal name : ")
            gc += 1
        else:
            og = True
    if og:
        print("You lose")
    else:
        print("You win")
practise("Python")
print(los(5))
ifstat()

nameloop()
library()
guess()
calc()