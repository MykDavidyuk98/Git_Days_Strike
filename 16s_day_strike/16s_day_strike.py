import math
import random
import simple_or_not

# Обчислити факторіал числа за допомогою while
# Факторіал — добуток усіх цілих чисел від 1 до N.
# N_number = int(input("Введіть число N: "))
# k = 1
# sum_numbers = 1
# while k <= N_number:
#     sum_numbers *= k
#     k += 1
# print(sum_numbers)


# Знайти перше парне число в списку (цикл з break)
# Задано список, знайти й вивести перше парне число, зупинивши цикл.
# mas = [random.randint(1,133) for i in range(15)]
# print(f'Масив виглядає: {mas}')
# for k in mas:
#     if  not k%2:
#         print(f'Перше парне чило в масиві -> {k}')
#         break
# else:
#     print('Парних чисел в масиві немає')


# Обчислення середнього значення введених чисел до числа >100
# Користувач вводить числа, поки не введе число більше за 100. Вивести середнє всіх попередніх.
# new_el = int(input('Введіть число: '))
# count_num = 0
# sum_num = 0
# while new_el <= 100:
#     count_num +=1 
#     sum_num += new_el
#     new_el = int(input('Введіть наступне число: '))
# average_sum = sum_num / count_num
# average_sum = round(average_sum, 1)
# print(f'Сума всіх чисел: {sum_num}, середнє знгачення: {average_sum}')


# count_num = 0
# sum_num = 0 
# while True:
#     new_el = int(input('Введіть число (зупинка > 100): '))
#     if new_el > 100:
#         break
#     count_num += 1
#     sum_num += new_el
# if count_num > 0:
#     print(f'Сума всіх чисел {sum_num}, (середнє значення: {round((sum_num / count_num), 1)})')
# else:
#     print('Перше введене число більше 100, спробуйте ще раз')


# Вивести числа від 1 до 50, пропускаючи кратні 7
# Цикл з умовним оператором continue.
# for i in range(1, 51, 1):
#     if i%7 == 0:
#         continue
#     else:
#         print(i)


# Вивести, скільки в списку чисел більше 10
# Прохід циклом по списку та підрахунок за умовою.
# mas = [random.randint(1, 20) for i in range(10)]
# print(f'список: {mas}')
# num_index = 0
# count_num = 0
# while num_index < len(mas):
#     if mas[num_index] > 10:
#         count_num += 1
#     num_index += 1
# print(f'В списку {count_num} чисел > 10')


# Перевірити, чи є серед N введених чисел хоча б одне від’ємне
# Цикл з введенням чисел та умовна перевірка.
# num_el = int(input('Введіть кількість чисел для вводу: '))
# count = 0
# count_neg = 0
# while count < num_el:
#     new_el = int(input(f'Введіть {count+1} число: '))
#     if new_el < 0:
#         count_neg += 1
#     count += 1
# print(f'Серед введених чисел {count_neg} {"відємне" if count_neg == 1 else "відємних"}')

# Функція, що приймає число і повертає "просте / не просте"
# Комбінація: функція + умовні оператори + перевірка через цикл.
# def simple_or_not (x: int):
#     if x <= 1:
#         return 'не просте'
#     for i in range(2, int(x**0.5)+1):
#         if x % i == 0:
#             return 'не просте'
#     return 'просте'
# print(simple_or_not(7))


# Функція, яка повертає найбільше з трьох чисел
# Комбінація: функція + умовні оператори (вкладені або max).
# def max_of_num (a: int, b: int, c: int):
    # mas = [0, 0, 0]
    # mas[0], mas[1], mas[2] = a, b, c
#     return max(a, b, c)
# print(max_of_num(10, 23, 4))


# Є відсортований список цілих чисел.
# Користувач вводить число, яке потрібно знайти.
# Реалізуй функцію binary_search(arr, target), яка повертає:

# індекс числа, якщо воно є в списку,

# або повідомлення "Елемент не знайдено".

mas = [random.randint(2,100) for i in range(9)]
mas = sorted(mas)
print(mas)
found_number = int(input('Введіть число яке потрібно знайти: '))
def binary_search(arr, target):
    """ Алгоритм кожного разу ділить масив навпіл. 
    Це значно швидше, ніж звичайний перебір. 
    Кількість кроків для n елементів — приблизно log₂(n). """
    
    left = 0             # Початкова ліва межа пошуку
    right = len(arr) - 1    # Початкова ліва межа пошуку
    step = 0                # Початкова кількість ітерацій 
    while left <= right:       # Поки межі не перетнулись 
        step += 1           
        mid = (left + right)//2    # Обчислюємо середній індекс
        if arr[mid] == target:      # Якщо елемент знайдено — повертаємо результат
            return f'Індекс числа {target}: {mid}, кількість ітерацій {step}'       
        elif arr[mid] < target:     # Якщо середній елемент менший за ціль — шукаємо правіше
            left = mid + 1
        else:                   # Інакше шукаємо лівіше
            right = mid - 1 
    # Якщо елемент не знайдено — повертаємо відповідне повідомлення
    return f'Елемент {target} не знайдено'

    # left = 0
    # right = len(arr) - 1
    # # і sum of iteration , every iteration cut arr in a half
    # for i in range(len(arr)):
    #     mid = (left +right)//2
    #     if arr[mid] == target:
    #        return f'індекс числа {found_number}: {mid}'
    #     elif arr[mid] < target:
    #         left = mid + 1
    #     else:
    #         right = mid - 1
    # return f'Число {target} не знайдено'  

print(binary_search(mas, found_number))

# 

