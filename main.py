print("____PROGRAM STARTED____")
# Variables (Змінні)
user_name = "John"
user_lastname = 'Doe'
user_txt = """Lorem Ipsum"""

# Name systems (Системи назв змінних)
test_variable_one = None  # snake case
testVariableOne = None  # camel case
TestVariableOne = None  # pascal case

# Constants (Константи)
SOME_CONSTANT = 3.14
DISCOUNT = 10

# Primitives type data (Примітивні типи даних)
some_txt = "Lorem Ipsum"  # string (str)
some_num_one = 1  # integer (int)
some_num_two = 8.26  # float
is_exist = True  # boolean (bool)
some_variable = None  # Empty var

# Operation with number (Операції  з цифрами)
num_one = 2
num_two = 5

# # simple
# print(num_one + num_two)
# print(num_one - num_two)
# print(num_one * num_two)
# print(num_one / num_two)
# print(num_one ** 2)

# # conditional
# print(num_one >= num_two)
# print(num_one > num_two)
# print(num_one <= num_two)
# print(num_one < num_two)
# print(num_one == num_two)
# print(num_one != num_two)

# ENTER DATA FROM USER (Ввід даних від користувача)
user_age = int(input("Please enter your age: "))
if user_age < 0:
    print("Data entered incorrect")
elif 0 <= user_age < 12:
    print("You're child!")
elif 12 <= user_age < 18:
    print("You're teen!")
elif 18 <= user_age < 130:
    print("You're adult!")
else:
    print("It's impossible")

print("____PROGRAM FINISHED____")
