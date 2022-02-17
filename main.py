first_number = input(print("Enter the first number: "))
second_number = input(print("Enter the second number: "))
print ("For a Mutiplication Calculation enter 1")
print ("For a Division Calculation enter 2")
print ("For a Adding Calculation enter 3")
print ("For a Subtraction Calculation enter 4")
calculation = input(print("What calculation do you want: "))
if calculation == 1:
  final = first_number * second_number
if calculation == 2:
  final = first_number / second_number
if calculation == 3:
  final = first_number + second_number
if calculation == 4:
  final = first_number - second_number
