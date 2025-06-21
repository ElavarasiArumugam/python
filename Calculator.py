def operation(num_1,operator,num_2):
    if operator == '+':
        return num_1 + num_2
    elif operator == '/':
        return num_1 / num_2
    elif operator == '-':
        return num_1 - num_2
    elif operator == '%':
        return num_1 % num_2
    elif operator == '*':
        return num_1 * num_2
    else:
        print("you entered the invalid operator")
        return None 
        

print("Welcome to calculator")
num_1 = int(input("enter a number: "))

operator = input("choose the operator /,+,-,%,* ").strip()
num_2 = int(input("enter the next number"))
answer = operation(num_1,operator,num_2)
if answer != None:

    print(f"the answer is{num_1} {operator} {num_2} = {answer}")
else:
     exit() 
while True:  
    next_operation = input(f"If you want to continue with {answer}.Type 'Yes' or 'No'").lower()
    if next_operation == "yes":
        operator_2 = input("choose the operator /,+,-,%").strip()
        num_2 = int(input("enter the next number"))
        new_answer = operation(answer,operator_2,num_2)
        if new_answer != None:
            print(f"The answer is: {answer} {operator} {num_2} = {new_answer}")
            answer = new_answer
        else:
            break
    else:
        print("thankyou for using calculator")
        break
    
    
