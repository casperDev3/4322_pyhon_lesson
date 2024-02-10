import random

# user_first_name = input("Enter your name: ")
# user_last_name = input("Enter your lastname: ")
# user_fathers_name = input("Enter your father's name: ")
# user_age = int(input("Enter your age: "))

##### ARRAYS
users_list = ["test", 12, 16, True]
users_list.append("banana")  # add element to end
users_list.pop()  # remove element from end array
# print(len(users_list))
# print(users_list[0])
# print(users_list[2])
# for item in users_list:
#     if item == 12:
#         print("It's twelfth!")
#         break
#     continue

###### OBJECTS

# user["city"] = "Dro"
# del user["last_name"]
# print(user)

#### ARRAY of LISTS
citizens = []
count = 0
while count < 1000000:
    print(
        f'circle: {count}'
    )
    user = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 35,
        "qty_children": random.randint(0, 8)
    }
    citizens.append(user)
    count += 1
    pass

child_free_counter = 0
many_children_counter = 0
for human in citizens:
    if human['qty_children'] == 0:
        child_free_counter += 1
        continue
    elif human['qty_children'] >= 3:
        many_children_counter += 1
        continue
    continue

print("_CFC: ", child_free_counter)
print("_AOC: ", many_children_counter)
