import math

import sys

print(" 1. Convert fraction to decimal \n 2. CountDown using for loops \n 3. Exponentials \n 4. Numbers divisible by 2")

Choice = input("Select one of the above choices")
choice = int(Choice) # convert user input to integer

#NUMBER 1
if(choice == 1):
    for i in range(2, 11):
        list = [1 / i]
        x = 0
        print("1/" + str(i) + " is " + str(float(list[x])))


#NUMBER 2
elif(choice == 2):
    User = input("Enter a number")
    User2 = int(User)
    i = 0

    if (User2 < 0):
        print("Enter a positive number")

    while (i <= User2):
        if (User2 >= 0):
            print(User2)
            User2 = User2 - 1

#NUMBER 3
elif(choice == 3):
    Base = input("Please input base")
    Exp = input("Please input exponent")

    base = int(Base)
    exp = int(Exp)

   # result = base**exp
    result = math.pow(base,exp)

    print(str(base) + "^" + str(exp) + " is " + str(result))

#NUMBER 4
elif(choice == 4):
    Input = input("Enter a number divisible by 2")
    UserInput = int(Input)

    while (UserInput % 2 != 0):
        Input2 = input("So close! enter another number")
        number = int(Input2)
        if (number % 2 == 0):
            print("Congratulations " + str(number) + " is divisible by 2")
            sys.exit()

    while (UserInput % 2 == 0):
        print("Congratulations! " + str(UserInput) + " is divisible by 2")
        sys.exit()


else:
    print("Invalid input")