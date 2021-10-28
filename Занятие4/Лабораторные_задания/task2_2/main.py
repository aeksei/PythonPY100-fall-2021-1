# num = 48
# a = num // 10
# b = num % 10
# if a == 4 and b == 8:
#     print("входят")
# elif a == 8 and b == 4:
#     print("входят")


num1 = 21
digits_list = [int(d) for d in str(num1)]
print(digits_list)

if (4 in digits_list and 8 in digits_list) or \
        (9 in digits_list):
    print("Число(а) входят ")
else:
    print("Нет")


digits_list = [2, 1]
if [4] and [8] or [9] in digits_list:
    ...
