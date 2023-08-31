"""Task 1 - Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'"""

print("TASK 1")
input_word = input("Please, enter the word to check: ")
turned_word = input_word[::-1]
is_polindrom = "+" if input_word == turned_word else "-"
print(is_polindrom)

"""Task 2 - Користувач вводить текст і слово, яке потрібно знайти, якщо це слово є в тексті, 
вивести 'YES', інакше 'NO'"""

print("TASK 2")
text = input("Please enter the text in which you want to search for the word: ")
word = input("now enter the word: ")

is_present = "YES" if text.count(word) > 0 else "NO"
print(is_present)


"""Task 3 - Написати валідатор для пошти. Користувач вводить пошту, а програма повинна перевірити, що в пошті 
є символ '@' і '.', і якщо це так, вивести "YES", інакше "NO" """

print("TASK 3")
mail = input("Please, enter your e-mail: ")
is_valid_email = "YES" if mail.count("@") > 0 and mail.count(".") > 0 else "NO"
print(is_valid_email)


"""Task 4 - Користувач вводить текст через пробіл. Конвертувати текст у список. Вивести останні 3 елементи 
зі списку, якщо список містить менше 3-х елементів, вивести повідомлення про те що кількість елементів 
менша за 3 і вказати кількість елементів поточного списку"""

print("TASK 4")

text = input("Please, enter a text with spaces: ")
new_list = list(text.split())
number = len(new_list)
print(f"The hole list: {new_list}")
print(f"The number of entered elements is {number}. But must be at least 3.") if number < 3 else print(f"Last 3 elements are: {new_list[-3:]}")

"""Task 5 - Додати перевірку введеної IP-адреси. Адреса вважається коректно заданою, якщо вона:
складається з 4 чисел (а не літер чи інших символів)
числа розділені точкою кожне число в діапазоні від 0 до 255 Якщо адреса неправильна, виводьте повідомлення: 
«Неправильна IP-адреса». 
Повідомлення "Неправильна IP-адреса" має виводитися лише один раз, навіть якщо кілька пунктів вище не виконані.
Обмеження: завдання треба виконувати, використовуючи лише пройдені теми."""

print("TASK 5")

ip_adress = input("Please, enter valid IP-adress: ")
list_ip = list(ip_adress.split("."))

correct_adress = True
numbers = len(list_ip)
max_num = max(list_ip)
min_num = min(list_ip)

if numbers != 4: # если я не поставлю эту проверку первой, а из_диджит второй, то при определенных вводах будут некорректные прерывания программы. А так программа никогда некорректно не прервется.
    correct_adress = False  # Возможно можно другим способом добиться стабильности, но я не вижу. Try использовать нельзя, т.к. есть условие пользоваться только тем, что мы проходили. Но я объединила max и min проверку и убрала 1 elif
elif not(list_ip[0].isdigit() and list_ip[1].isdigit() and list_ip[2].isdigit() and list_ip[3].isdigit()):
    correct_adress = False
elif int(max_num) > 255 or int(min_num) <0:
    correct_adress = False
else:
    correct_adress = True


if correct_adress == True:
    print("OK")
else:
    print("Your adress is NOT normal")