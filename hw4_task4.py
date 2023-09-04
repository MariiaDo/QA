"""4 - You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
Names of people in the format "John Dow" first and second name. Find those who are on all blacklists."""

casino_blacklist = {"John Dow", "Ivan Ivan", "Petr Petr", "Olga Olga"}
poker_blacklist = {"Mariia Mariia", "Liliia Li", "John Dow", "Vasyl Va", "Olga Olga"}
alcohol_blacklist = {"Valentina Po", "Irina Ou", "Mariia Mariia", "John Dow"}

common_list = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(f"The common list is: {common_list}.")