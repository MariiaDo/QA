"""5- The list of names is given: names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

Using the continue statement, print only the correct names to the console"""

names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
for i in range(len(names)):
    if isinstance((names[i]), str) != True:
        continue
    print(names[i])
