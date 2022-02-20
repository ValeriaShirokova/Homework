#  - Любой начальный список минимум 70 элементов.(Есть задания где можно меньше, по усмотрению)
#  - Все результаты выводить в консоль.

import random
import math
import names
import randomtimestamp as time
import string
import datetime
start = datetime.date(2000, 1, 1)

# 1) Написать скрипт который создаст список целых чисел.

int_list = list(range(0, 70))
print("The integer list is", int_list)
print("The list length is", len(int_list))

# 2) Написать скрипт который создаст список целых чётных чисел.

rand_int = random.randint(0, 100)
even_number_list = []
while len(even_number_list) < 70:
    for i in range(rand_int):
        if i % 2 == 0:
            even_number_list.append(i)

print("The even number list is", even_number_list)
print("The list length is", len(even_number_list))

# 3) Написать скрипт который создаст список целых нечётных чисел.

rand_int = random.randint(0, 100)
odd_number_list = []
while len(odd_number_list) < 70:
    for i in range(rand_int):
        if i % 2 == 1:
            odd_number_list.append(i)

print("The odd number list is", odd_number_list)
print("The list length is", len(odd_number_list))

# 4) Написать скрипт который из списка целых чисел выведет чётные числа.

int_list = list(range(0, 70))
even_list = []
for i in int_list:
    if i > 0 and i % 2 == 0:
        even_list.append(i)

print("Here is the integer list:", int_list)
print("The even numbers in this list are", even_list)

# 5) Написать скрипт который из списка целых чисел выведет нечётные числа.

int_list = list(range(0, 70))
odd_list = []
for i in int_list:
    if i % 2 == 1:
        odd_list.append(i)

print("Here is the integer list:", int_list)
print("The odd numbers in this list are", odd_list)

# 6) Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.

int_list = list(range(0, 70))
even_list_5 = []
for i in int_list:
    if i % 2 == 0 and i % 5 == 0:
        even_list_5.append(i)

print("Here is the integer list:", int_list)
print("The even numbers you can divide by 5 are", even_list_5)

# 7) Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.

int_list = list(range(0, 70))
even_list_5 = []
for i in int_list:
    if i % 2 == 0 and i % 5 == 0:
        even_list_5.append(i)
amount = len(even_list_5)

print("Here is the integer list:", int_list)
print("The amount of even numbers you can divide by 5 is", amount)

# 8) Написать скрипт который создаст список целых рандомных чисел.

rand_int = random.randint(0, 100)
int_list_rand = []
while len(int_list_rand) < 70:
    for i in range(rand_int):
        int_list_rand.append(i)
print("The random list is", int_list_rand)
print("The list length is", len(int_list_rand))

# 9) Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.

def split_lists(your_list):
    split_list = []
    while len(your_list) > 5:
        i = your_list[:5]
        split_list.append(i)
        your_list = your_list[5:]
        if len(your_list) < 5:
            for x in range(5 - len(your_list)):
                your_list.append(False)
    split_list.append(your_list)

    return split_list


result = split_lists(int_list_rand)
print("The result of splitting the list is", result)

# 10) Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.

def odd_and_even(your_int_list):
    odd_list = []
    even_list = []
    for i in your_int_list:
        if i % 2 == 0:
            even_list.append(i)
        elif i % 2 == 1:
            odd_list.append(i)

    return odd_list, even_list


result = odd_and_even(int_list_rand)
print("The lists are", result)

# 11) Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.

five_stars = []
list = split_lists(int_list_rand)
five_stars.extend(list)
print("The 5_stars list is", five_stars)
print("element:", five_stars[0], len(five_stars))

# 12) Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars

sum_five_list = []
for i in range(0, len(five_stars) - 1):
    x = five_stars[i]
    plus = sum(x)
    sum_five_list.append(plus)

print("The 5_stars sum list is", sum_five_list)

# 13) Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка. В одном списке внутренние списки из 5_stars сумма чисел которых >= 100, а другой сумма чисел которых < 100. Если какого-то списка не получится, то вместо него вернуть текст “No lists”

def five_function(five_stars):
    sum_more_list = []
    sum_less_list = []
    for i in range(0, len(five_stars) - 1):
        x = five_stars[i]
        plus = sum(x)
        if plus >= 100:
            sum_more_list.append(plus)
        elif plus < 100:
            sum_less_list.append(plus)
    if sum_more_list == []:
        sum_more_list = "No lists"
    elif sum_less_list == []:
        sum_less_list = "No lists"

    return sum_more_list, sum_less_list


result = five_function(five_stars)
print("The result is", result)

# 14) Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок вы сумеете отложить 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.

def savings():
    x = 0
    z = 0
    mylist = []
    mylist_2 = []
    for x in range(90):
        if x < 20:
            y = 0
        elif x >= 20 and x < 27:
            y = 250
        elif x == 27:
            y = 500
        elif x >= 60:
            y = 0
        else:
            y = 500 * 1 * (x - 27)
        z = z + y
        mylist.append(x)
        mylist.append(z)
        mylist_2.append(mylist)
        mylist = []

    try:
        my_age = int(input("Please enter your age: "))
        for i in range(len(mylist_2)):
            if my_age == mylist_2[i][0]:
                print("Now you have", mylist_2[i][1], "$")
        for i in range(len(mylist_2)):
            if mylist_2[i][1] >= 10000:
                if mylist_2[i][0]-my_age < 0:
                    break
                print("You will have 10 000 $ in", mylist_2[i][0]-my_age, "year(s)")
                break
        for i in range(len(mylist_2)):
            if mylist_2[i][1] >= 20000:
                if mylist_2[i][0]-my_age < 0:
                    break
                print("You will have 20 000 $ in", mylist_2[i][0]-my_age, "year(s)")
                break
        for i in range(len(mylist_2)):
            if mylist_2[i][1] >= 30000:
                if mylist_2[i][0] - my_age < 0:
                    break
                print("You will have 30 000 $ in", mylist_2[i][0]-my_age, "year(s)")
                break
        for i in range(len(mylist_2)):
            if mylist_2[i][1] >= 50000:
                if mylist_2[i][0] - my_age < 0:
                    break
                print("You will have 50 000 $ in", mylist_2[i][0]-my_age, "year(s)")
                break
        for i in range(len(mylist_2)):
            if mylist_2[i][1] >= 100000:
                if mylist_2[i][0] - my_age < 0:
                    break
                print("You will have 100 000 $ in", mylist_2[i][0]-my_age, "year(s)")
                break
    except ValueError:
        print("Please enter your current age in completed years")


result = savings()

# 15) Написать функцию которая получив на вход стартовую ЗП Junior QA и количество лет стажа выведет в консоль прогресс роста ЗП по каждому году из введенного количества лет стажа. Внутри функция учитывает дорожную карту развития скилов QA и список, полезных для компании, активностей которые может делать QA.

def qa_roadmap_for_3_years(start_salary, working_years):

    while working_years <= 1:
        answer_1_1 = input("Have you learned how to write proper bug reports? [yes/no] ")
        if answer_1_1 == "yes":
            start_salary = round(start_salary * 1.05, 2)
            print("Your salary has increased by 10 %, now it's", start_salary, "$")
        pass
        answer_1_2 = input("Have you had a chance to create checklists? [yes/no] ")
        if answer_1_2 == "yes":
            start_salary = round(start_salary * 1.05, 2)
            print("Your salary has increased by 5 %, now it's", start_salary, "$")
        pass
        answer_1_3 = input("Have you learned how to work with browser DevTools? [yes/no] ")
        if answer_1_3 == "yes":
            start_salary = round(start_salary * 1.05, 2)
            print("Your salary has increased by 5 %, now it's", start_salary, "$")
        pass
        answer_1_4 = input("Do you know how to work with GitHub using the bash command line? [yes/no] ")
        if answer_1_4 == "yes":
            start_salary = round(start_salary * 1.05, 2)
            print("Your salary has increased by 5 %, now it's", start_salary, "$")
        pass
        answer_1_5 = input("Have you worked in Agile teams? [yes/no] ")
        if answer_1_5 == "yes":
            start_salary = round(start_salary * 1.05, 2)
            print("Your salary has increased by 5 %, now it's", start_salary, "$")
        pass
        if answer_1_1 != "yes" and answer_1_2 != "yes" and answer_1_3 != "yes" and answer_1_4 != "yes" and answer_1_5 != "yes":
            print("Try to master those skills to get a salary raise")
        break
    while 1 < working_years <= 2:
        answer_2_1 = input("Have you learned how to write basic SQL queries? [yes/no] ")
        if answer_2_1 == "yes":
            start_salary = round(start_salary * 1.15, 2)
            print("Your salary has increased by 15 %, now it's", start_salary, "$")
        pass
        answer_2_2 = input("Have you learned how to write tests in Postman? [yes/no] ")
        if answer_2_2 == "yes":
            start_salary = round(start_salary * 1.2, 2)
            print("Your salary has increased by 20 %, now it's", start_salary, "$")
        pass
        answer_2_3 = input("Do you know how to work with Android Studio? [yes/no] ")
        if answer_2_3 == "yes":
            start_salary = round(start_salary * 1.2, 2)
            print("Your salary has increased by 20 %, now it's", start_salary, "$")
        pass
        answer_2_4 = input("Have you learned how to work with Charles or Fiddler? [yes/no] ")
        if answer_2_4 == "yes":
            start_salary = round(start_salary * 1.2, 2)
            print("Your salary has increased by 20 %, now it's", start_salary, "$")
        pass
        answer_2_5 = input("Have you done performance tests using JMeter? [yes/no] ")
        if answer_2_5 == "yes":
            start_salary = round(start_salary * 1.25, 2)
            print("Your salary has increased by 25 %, now it's", start_salary, "$")
        pass
        if answer_2_1 != "yes" and answer_2_2 != "yes" and answer_2_3 != "yes" and answer_2_4 != "yes" and answer_2_5 != "yes":
            print("Try to master some of those skills to get a salary raise")
        break
    while 2 < working_years <= 3:
        answer_3_1 = input("Have you learned some programming language? [yes/no] ")
        if answer_3_1 == "yes":
            start_salary = round(start_salary * 1.25, 2)
            print("Your salary has increased by 25 %, now it's", start_salary, "$")
        pass
        answer_3_2 = input("Have you mastered some testing automation tool(s)? [yes/no] ")
        if answer_3_2 == "yes":
            start_salary = round(start_salary * 1.2, 2)
            print("Your salary has increased by 20 %, now it's", start_salary, "$")
        pass
        answer_3_3 = input("Have you had a successful experience being in charge of a testing process? [yes/no] ")
        if answer_3_3 == "yes":
            start_salary = round(start_salary * 1.2, 2)
            print("Your salary has increased by 20 %, now it's", start_salary, "$")
        if answer_3_1 != "yes" and answer_3_2 != "yes" and answer_3_3 != "yes":
            print("Keep learning to get a salary raise")
        break

result = qa_roadmap_for_3_years(1000, 0.5)

# 16) Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.

name_list = []
for i in range(0, 70):
    n = names.get_full_name()
    name_list.append(n)
print("The name list is", name_list)

# 17) Написать скрипт который сгенерирует список имён файлов. К каждому имени  файла надо прикрепить номер итерации цикла как порядковый номер.

file_formats = [".txt", ".docx", ".xlsx"]
file_list = []
for i in range(1, 70):
    name_gen = "file_" + str(i) + random.choice(file_formats)
    file_list.append(name_gen)
print("The file list is", file_list)

# 18) Написать скрипт который сгенерирует список списков. Каждый элемент списка это список в котором 0-й элемент - это имя пользователя, а 1-й - элемент это дата регистрации.

reg_list = []
full_reg_list = []
for i in range(0, 70):
    reg_date = str(time.random_date(start))
    n = names.get_full_name()
    reg_list.insert(0, n)
    reg_list.insert(1, reg_date)
    full_reg_list.append(reg_list)
    reg_list = []

print("The list of lists is", full_reg_list)

# 19) Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список в котором:
# 0-й - элемент - это имя пользователя,
# 1-й - элемент - это логин,
# 2-й - элемент - это пароль,
# 3-й - элемент - это email (email тоже генерировать),
# 4-й - элемент - это дата регистрации

# # 20) Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором:
# # 0-й - элемент - это логин,
# # 1-й - элемент - это имя,
# # 2-й - элемент - семейный статус (True, False - генерировать рандомно)
#
# # 21) Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором:
# # 0-й - элемент - это логин,
# # 1-й - элемент - это имя,
# # 2-й - элемент - гендер (1-м, 0-ж)
#
# # 22) Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором:
# # 0-й - элемент - это логин,
# # 1-й - элемент - это имя,
# # 2-й - элемент - зарплата (генерироовать от 300$ до 5000$)

employee_list = []
full_employee_list = []
family_list = []
full_family_list = []
gender_list = []
full_gender_list = []
salary_list = []
full_salary_list = []

for i in range(0, 70):
    n_f = names.get_first_name(gender="female")
    n_m = names.get_first_name(gender="male")
    n = random.choice([n_f, n_m])
    s = names.get_last_name()
    full_n = n + " " + s
    employee_list.insert(0, full_n)
    family_list.insert(1, full_n)
    gender_list.insert(1, full_n)
    if n == n_m:
        gender_list.insert(2, 1)
    elif n == n_f:
        gender_list.insert(2, 0)
    salary_list.insert(1, full_n)
    login = n[0].lower() + "." + s.lower()
    employee_list.insert(1, login)
    family_list.insert(0, login)
    gender_list.insert(0, login)
    salary_list.insert(0, login)
    password = " "
    while len(password) < 11:
        for x in range(0, 5):
            rand_int = str(random.randint(0, 9))
            rand_letter = random.choice(string.ascii_letters)
            password = password + rand_int + rand_letter
    employee_list.insert(2, password)
    email_dom = ["@gmail.com", "@ymail.com", "@iCloud.com"]
    email = n.lower() + "_" + s.lower() + random.choice(email_dom)
    employee_list.insert(3, email)
    reg_date = str(time.random_date(start))
    employee_list.insert(4, reg_date)
    t_or_f = [True, False]
    married = random.choice(t_or_f)
    family_list.insert(2, married)
    salary = str(random.randint(300, 5000)) + "$"
    salary_list.insert(2, salary)
    full_employee_list.append(employee_list)
    full_family_list.append(family_list)
    full_gender_list.append(gender_list)
    full_salary_list.append(salary_list)
    employee_list = []
    family_list = []
    gender_list = []
    salary_list = []
print("The employee list is", full_employee_list)
print("The family list is", full_family_list)
print("The gender list is", full_gender_list)
print("The salary list is", full_salary_list)

# 23) Написать скрипт который создаст список мён работников из salary у которых ЗП от 1500$ до 3000$.

big_salary_list = []
for i in range(len(full_salary_list)):
    sal_str = full_salary_list[i][2]
    sal = int(sal_str.replace("$", ""))
    if 1500 <= sal <= 3000:
        big_salary_list.append(full_salary_list[i][1])
print("The big salary list is", big_salary_list)

# 24) Написать скрипт который создаст список имён мужчин из gender.

men_list = []
for i in range(len(full_gender_list)):
    if full_gender_list[i][2] == 1:
        men_list.append(full_gender_list[i][1])
print("The men list is", men_list)

# 25) Написать скрипт который создаст список имён женщин из gender.

women_list = []
for i in range(len(full_gender_list)):
    if full_gender_list[i][2] == 0:
        women_list.append(full_gender_list[i][1])
print("The women list is", women_list)

# 26) Написать скрипт который создаст список имён неженатых мужчин из family.

single_men_list = []
for i in range(len(full_family_list)):
    if full_family_list[i][2] == False and full_gender_list[i][2] == 1:
        single_men_list.append(full_family_list[i][1])
print("The single men list is", single_men_list)

# 27) Написать скрипт который создаст список имён незамужних женщин из family.

single_women_list = []
for i in range(len(full_family_list)):
    if full_family_list[i][2] == False and full_gender_list[i][2] == 0:
        single_women_list.append(full_family_list[i][1])
print("The single women list is", single_women_list)

# 28) Написать скрипт который создаст список имён неженатых мужчин с ЗП больше или равной 1500$. Используйте Employees, family, gender, salary. Реализуйте как скрипт, без функций

one_half_sal_single_men_list = []
for i in range(len(full_employee_list)):
    sal_str_1 = full_salary_list[i][2]
    sal_1 = int(sal_str_1.replace("$", ""))
    if full_family_list[i][2] is False and full_gender_list[i][2] == 1 and sal_1 >= 1500:
        one_half_sal_single_men_list.append(full_employee_list[i][0])

print("The guys who make over 1.5K$ list is", one_half_sal_single_men_list)

# 29) Реализуйте пункт 28 через через функции.

def who_to_marry_in_this_company(employee_l, family_l, gender_l, salary_l):
    prospect_list = []
    for i in range(len(employee_l)):
        sal_str_1 = salary_l[i][2]
        sal_1 = int(sal_str_1.replace("$", ""))
        if family_l[i][2] is False and gender_l[i][2] == 1 and sal_1 >= 1500:
            prospect_list.append(employee_l[i][0])

    return prospect_list


potential_husband_list = who_to_marry_in_this_company(full_employee_list, full_family_list, full_gender_list, full_salary_list)
print("Those men are a catch:", potential_husband_list)