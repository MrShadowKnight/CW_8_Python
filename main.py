import json
# def initials(first_name, second_name, father_name):
#     print(f"{first_name.capitalize()} {second_name[0].capitalize()}. {father_name[0].capitalize()}.")

# first_name = input("Введіть прізвище: ")
# second_name = input("Введіть імя: ")
# father_name = input("Введіть побатькова: ")

# initials(first_name, second_name, father_name)

# def fibonacci_row(end):
#     number_one = 1
#     number_two = 2
#     fibonacci_row_list =[1, 2]
#     while number_two <= end:
#         number_three = number_one + number_two
#         number_one = number_two
#         number_two = number_three
#         if number_three <= end:
#             fibonacci_row_list.append(number_three)
#     return fibonacci_row_list

# end = int(input("Введіть кінцеве число ряду Фібоначчі: "))
# print(fibonacci_row(end))
with open("test.json", "r") as file:
    accounts = json.load(file)

# def money_withdraw(money):

for i in accounts['accounts']:
    print(i['id'])
# print("Меню")
# print("1 --- Створити новий рахунок")
# print("2 --- Зняти кошти з рахунку")
# print("3 --- Поповнити рахунок")
# print("4 --- Перевести кошти з одного рахунку на інший")
# print("5 --- Перевірити баланс рахунку")
# print("6 --- Вийти з програми")