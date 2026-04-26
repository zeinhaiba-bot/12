numbers = [10, 20, 30, 40, 50]
num = int(input('Введите число>> '))

for i in range(len(numbers)):
    if numbers[i] == num:
        print(f'Ваше число с индексом>> {i}')
        break
else:
    print('Такого числа нет!')