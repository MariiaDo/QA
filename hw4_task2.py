"""2 - У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] ,
перетворити його у список змінних для Пайтона snace_case, "friends_list", "my_tuple"]"""

my_list = ["FirstItem", "FriendsList", "MyTuple"]
result_list = []

for i in range(len(my_list)):
    result_list.append(len(my_list[i]))
    my_new_list = []
    for j in range(len(my_list[i])):
        if my_list[i][j].isupper() == True and j != 0:
            my_new_list.append("_")
        my_new_list.append(my_list[i][j])
    result_list[i] = "".join(my_new_list).lower()
print(f"The new list is: {result_list}")
















