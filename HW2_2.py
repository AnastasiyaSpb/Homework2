# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

a = int(input("Введите число: "))
result_list = []

for i in range(1,a+1):
    s = 1
    for b in range (1,i+1):
        s *= b
    result_list.append(s)

print(result_list)