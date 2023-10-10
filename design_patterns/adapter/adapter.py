""" 1 -
Implement adapter patter from_txt_to_html
for example, we have a such structure in txt:

name,last_name,age,salary
John,Malkovich,28,1000

I want to see:

<name>John</name>
<last_name>Malkovich</last_name>
.............

It should work with any file with such a structure
"""


class TxtAdapter:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def txt_to_xml(self):
        with open(self.__file_path, 'r') as file:
            lines = file.readlines()

        header = lines[0].replace('\n', '').split(',')
        users_data = [user.replace('\n', '').split(',') for user in lines[1:]]

        a = []
        b = []
        c = []
        for i in range(1, len(header) + 1):
            a.append("<")
            b.append(">")
            c.append("< /")

        result = []
        for user in users_data:
            result.append(list(zip(a, header, b, user, c, header, b)))

        res = str(result).replace("), (", "\n").replace(")], [(", "\n").replace("[[(", "").replace(")]]", "").replace(
            "'", "").replace(",", "").replace(" ", "")
        return res


if __name__ == '__main__':
    xml_ = TxtAdapter('users.txt').txt_to_xml()
    print(xml_)
