"""Task 1 - Існує список з іменами ["john", "marta", "james", "amanda", "marianna"], перетворити рядок,
щоб кожне ім'я явно починалися з великої літери."""

my_list = ["john", "marta", "james", "amanda", "marianna"]
my_new_list = []
for i in range(len(my_list)):
    my_new_list.append(my_list[i].title())
print(f"The new list with upper cases is: {my_new_list}")
