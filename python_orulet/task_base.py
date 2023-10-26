# ALL FUNCTION RETURN SOMETHING!

def circleArea(radius):
    # Write a Python function that calculates the area of a circle based on the radius entered by the user.
    return radius ** 2 *3.14

def nameReverse(name):
    # Write a Python function that accepts the user's full name in hungarian style and prints them in reverse order with a space between them.
    a = name.split()
    return a[1] + " " + a[0]

def easyMath(n):
    # Write a Python function that accepts an integer (n) and computes the value of n+nn+nnn.
    return n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))

def difference(num1,num2):
    # Write a Python function to calculate the difference between a two given number.

    if num1>num2:
        return num1-num2
    else:
        return num2-num1

def bmiIndex(weight, height):
    # Write a Python function to calculate the body mass index.
    return weight / height ** 2

def digitsSum(number):
    # Write a Python function to calculate sum of digits of a number.
    aa = 0
    for i in str(number):
        aa += int(i)
    return aa

def sortThree(a,b,c):
    # Write a Python function to sort three integers without using conditional statements and loops (return list!).
    maxN = max([a, b, c])
    minN= min([a, b, c])
    midN= a + b + c - minN - maxN
    return [minN, midN, maxN]

def bePositive(li):
    # Write a Python function to filter positive numbers from a list (return list!).
    poz=[]
    for i in li:
        if i > 0:
            poz.append(i)
    return poz

def decimalToBinary(decimalNum):
    # Write a Python function to convert an integer (decimal) to binary (return string!).
    res = ""
    
    while decimalNum != 0:
        mod = decimalNum % 2
        res + str(mod)
        decimalNum = int(decimalNum / 2)
    return res[::-1]


def decimalToHexa(decimalNum):
    # Write a Python function to convert decimal to hexadecimal (return string!).
    return 0
