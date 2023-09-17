"""2- Написати програму, яка просканує кореневу папку вашого проєкту, збереже у файл files_size.txt назви та розмір
файлів, і надрукує назву найбільшого файлу та його розмір."""

import os

path = "."
file_info = []
my_dict = {}
res_dict = {}
bigger = None
with open('files_size.txt', 'w') as file:
    for i in os.listdir(path):
        if os.path.isfile(path + '\\' + i):
            my_dict.update({str(i): os.path.getsize(i)})

            file.writelines((str(i), ": ", str(os.path.getsize(path + '\\' + i)), '\n'))
        else:  # блок для внутренней вложенности (в надежде, что нет вложенности следующих уровней :-) )
            print("Список файлов в папке: ", i, ': ', os.listdir((path + '\\' + i)))
            for j in os.listdir(path + '\\' + i):
                my_dict.update({str(j): os.path.getsize(str(path + '\\' + i + '\\' + j))})

                file.writelines((str(j), ": ", str(os.path.getsize(path + '\\' + i + '\\' + j)), '\n'))

bigger = max(my_dict.values())
for item in my_dict.items():
    if item[1] == bigger:
        res_dict.update({item[0]: item[1]})

print("Самый большой файл в проекте: ", res_dict)
