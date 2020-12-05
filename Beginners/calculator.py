def calculator(num1,num2,operator):
    n1=int(num1)
    n2 =int(num2)
    if operator == "+":
        return n1+n2
    elif operator == "-":
        return n1-n2
    elif operator == "*":
         return n1*n2
    elif operator == "/":
        return n1/n2

print("*********************")
print("* SIMPLE CALCULATOR *")
print("*********************")
num1=input("Enter number 1:")
num2=input("Enter number 2:")
operator=input("Enter Operator(+,-,*,/)")
if operator != "+" and operator != "-"  and operator != "*"  and operator != "/" :
    print("Operation not allowed!!")
    print("Operator allowed: +,-,*,/")
else:
    print("The result of "+num1+operator+num2+"="+str(calculator(num1,num2,operator)))


