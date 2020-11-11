try:

    def addition(x,y):
        return x+y
    def subtract(x,y):
        return x-y
    def multiplication(x,y):
        return x*y
    def division(x,y):
        return x/y
    num1=int(input("enter first number:"))
    num2=int(input("enter second nmber:"))

    print("selection operation:")
    print("1.addition")
    print("2.subtract")
    print("3.multiplication")
    print("4.division")
    print("0. exit")
    choice=input("enter choice(1/2/3/4/0):")

    if choice == '1':
        print(num1, " + ", num2, " = ", addition (num1,num2))

    elif choice == '2':
        print(num1, " - ", num2, " = ", subtract (num1,num2))
        
    elif choice == '3':
        print(num1, " * ", num2, " = ", multiplication (num1,num2))

    elif choice == '4':
        print(num1, " / ", num2, " = ", division(num1,num2))
    elif choice == '0':
        print("exit")
    else:
        print("invalid choice")


except (ZeroDivisionError,ValueError)as msg :
    print(msg)

