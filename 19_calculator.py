# print("\t\t\t\t\t\t\WELCOME TO CALCULATOR\n")
num1= int(input("enter first num \n"))
num2= int(input("enter second num \n"))

print("choose a option \n 1. + \n 2. - \n 3. / \n 4. * \n")
choice= input("enter choice")

if choice == '+':
    print(f" addition of {num1} and {num2} is: ", num1 + num2)

elif choice=='-':
    print(f" subtraction of {num1} and {num2} is: ", num1 - num2)

elif choice=='/':
    print(f" dividion of {num1} and {num2} is: ", num1/ num2)

elif choice=='*':
    print(f" multiplication of {num1} and {num2} is: ", num1*num2)

else:
    print("choice is invalid")
    print("THANKYOU")