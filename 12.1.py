n = int(input("Введите число больше или равно 1----"))

numbers = []
for i in range(1,n+1):
    if i % 2 == 1:
        numbers.append(i)
print(f"Список нечетных чисел от 1 до {n}----{numbers}")