# FUNCTIONS WITH OUTPUTS

# def format_name(f_name, l_name):
#     format_name_f= f_name.title()
#     format_name_l= l_name.title()
#     return f"{format_name_f} {format_name_l}"  
# print(format_name("naol", "uMEr") )  

# PROJECT: CALCULATOR

# def add(a1, a2):
#     return a1 + a2
# def subtract(a1, a2):
#     return a1 - a2
# def multiply(a1, a2):
#     return a1 * a2
# def divide(a1, a2):
#     return a1/a2

# operations= {"+": add, "-": subtract, "*": multiply, "/": divide}
# def calculator():
#     num1= float(input("what is the first number? \n"))
#     for keys in operations:
#         print(keys)

#     stop_operation= False
#     while not stop_operation:
#         operation_symbol= input("pick an operation \n")
#         num2= float(input("what's the next number? \n"))
#         calc_operation= operations[operation_symbol]
#         answer= calc_operation(num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#         should_continue= input(f"type 'y' to do further operations with {answer} or type 'n' to restart calculator \n ")
#         if should_continue== "y":
#             num1=answer
#         elif should_continue=="n":
#             stop_operation= True
#             calculator()
# calculator()
