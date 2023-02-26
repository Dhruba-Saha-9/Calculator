#input of numbers and operator
a=int(input("Enter a number : "))
b=input("Enter the operation (+,-,*,/,%,//,**) : ")
c=int(input("Enter next number : "))

#operation part
if b == "+":
    print(a+c)
elif b == "-":
    print(a-c)
elif b == "*":
    print(a * c)
elif b == "/":
    print(a/c)
elif b == "%":
    print(a % c)
elif b == "//":
    print(a//c)
elif b == "**":
    print(a**c)
else:
    print("Invalid Operation")


