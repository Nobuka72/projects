while True:
    print("1-Add")
    print("2-substract")
    print("3-multipication")
    print("4-division")
    print("5-remainder")
    try:
        option=int(input("choose an operation(between 1to5): "))
    except ValueError:
        print("invalid input. please enter a number between 1 and 5.")
        continue
    
    if option == 5:
        print("Exiting calculator. Goodbye!")
        break

    if option not in [1,2,3,4,5]:
        print("Invalid option! Please choose between 1-5.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered!")
        continue

    print("you have selected option ", option)

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
    print("the calculated result is: ", result)

if __name__ == "__main__":
    main()






    
      
