#1) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число
# value = 120
# value = int(value)
# if value < 100:
#     new_value = value //2
#     print (new_value)
# else:
#     new_value = - value
#     print(new_value)


#2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно 1, в противном случае - 0
# value = 90
# value = int(value)
# if value < 100:
#     new_value = 1
#     print(new_value)
# else:
#     new_value = 0
#     print(new_value)


# 3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно True, в противном случае - False
# value = 123
# value = int(value)
# if value < 100:
#     new_value = True
#     print(new_value)
# else:
#     new_value = False
#     print(new_value)

# 4) У вас есть переменная my_str, тип - str. Заменить в my_str все маленькие буквы на большие.
# my_str = "Hello my name is Alexey"
# my_str = my_str.upper()
# print(my_str)

# 5) У вас есть переменная my_str, тип - str. Заменить в my_str все большие буквы на маленькие.
# my_str = "HELLO MY NAME IS ALEXEY"
# my_str = my_str.lower()
# print(my_str)


# 6) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же. Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.
# my_str = "Alex"
# if len(my_str) < 5:
#     print(my_str * 2)
# else:
#     print(my_str)


# 7) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же. Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.
# my_str = "Alex"
# if len(my_str) < 5:
#     print(my_str + my_str[::-1])
# else:
#     print(my_str)
