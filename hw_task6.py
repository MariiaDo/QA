"""6 -

Please write a program which count and print the numbers of each character in a string input by console.

Example: If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2 c,2 b,2 e,1 d,1 g,1 f,1

Hints: Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.

Use str.join() method and dict comprehension for print result """

input_str = "abcdefgabc"
my_dict_1 = {}
printStr = ""
for i in range(len(input_str)):
    my_dict_1.update({input_str[i]: input_str.count(input_str[i])})

for i in my_dict_1:
    printStr += i + "," + str(my_dict_1.get(i)) + " "

print(printStr)
