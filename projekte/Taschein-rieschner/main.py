# getting inputs
first_num, operator, second_num =input("Enter the Oberation: ").split(" ")
print("_" * 50)
# convert to float
first_num = float(first_num)
second_num = float(second_num)
# check the operator and do the operation
if operator == '+' :
  operator_nam = "'Additionr"
  result = first_num + second_num
elif operator == '-' :
   operator_nam = "Subtraction"
   result = first_num - second_num
elif operator == '*' :
   operator_nam = "Multiplication"
   result = first_num * second_num
elif operator == '/' :
   operator_nam = "Division"
   result = first_num / second_num
elif operator == '**' :
   operator_nam = "Power"
   result = first_num ** second_num

# print the result
print(f'{operator_nam} result is {result:,.3f}')