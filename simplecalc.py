                                # A SIMPLE CALCULATOR
print("1-Add")
print("2-substract")
print("3-multipication")
print("4-division")
print("5-remainder")

option=int(input("choose an operation: "))

print("you have selected option ", option)

if (option in [1,2,3,4,5]):
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))


    if (option==1):
        result=num1+num2
    elif (option==2):
        result=num1-num2
    elif (option==3):
        result=num1*num2
    elif (option==4):
        result=num1/num2
    elif (option==5):
        result=num1%num2
    print("the result is: ", result)

else: 
    print("invalid operations entered")







    
      
