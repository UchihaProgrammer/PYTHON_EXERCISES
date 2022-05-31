#Q - MAKE A CALCULATOR THAT CORRECTLY SOLVE THE PROBLEMS EXECPT THE FOLLOWING:-
# (i)45*3 = 555
# (ii)56+9 = 77
# (iii)56/6 = 4
# NOTE - IT SHOULD ALSO WORK IF YOU REVERSE THE FAULTY NUMBERS

# SOLUTION:-
num1 = int(input("Enter the first number: "))
operator = input("Enter '+' for addition, '-' for subtraction, 'x' for multiplication and '/' for division:-\n")
num2 = int(input("Enter the second number: "))

if num1==45 and operator=="x" and num2==3 or num1==3 and operator=="x" and num2==45:
    print("555")
elif num1==56 and operator=="+" and num2==9 or num1==9 and operator=="+" and num2==56:
    print("77")
elif num1==56 and operator=="/" and num2==6 or num1==6 and operator=="/" and num2==56:
    print("4")
else:
    if operator=="+":
        print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="x":
        print(num1*num2)
    elif operator=="/":
        print(num1/num2)
    else:
        print("ERROR! WRONG INPUT")

input("THANK YOU FOR USING\n")