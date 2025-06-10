# Умова: Є список словників. Знайди словник, у якому "score" найбільший.
# students = [
#     {'name': 'Olga', 'score': 78},
#     {'name': 'Ivan', 'score': 85},
#     {'name': 'Dmytro', 'score': 91}
# ]

# print(max(students, key=lambda student: student['score']))

# 🧠 Як це працює покроково:
# 1. max(students, key=...)
# Це вбудована функція max(), яка знаходить максимальний елемент у колекції.
# Але як max() розуміє, що порівнювати? Ми це задаємо через параметр key=.
# 2. key=lambda student: student['score']
# lambda student: student['score'] — це анонімна функція (функція без імені), яка:
# приймає один словник student (наприклад, {'name': 'Olga', 'score': 78})
# повертає його бал student['score']
# Тобто max() буде шукати студента, у якого максимальне значення 'score'.




# students = [
#     {'name': 'Olga', 'score': 78},
#     {'name': 'Ivan', 'score': 85},
#     {'name': 'Dmytro', 'score': 91}
# ]
#  Рішення вручну:
# # Step 1: Припускаємо, що перший студент має найвищий бал
# top_student = students[0]  # {'name': 'Olga', 'score': 78}

# # Step 2: Ітеруємо по решті студентів

# for student in students[1:]:

#     # Якщо знайдено більший бал — оновлюємо
#     if student['score'] > top_student['score']:
#         top_student = student

# # Step 3: Виводимо результат
# print(top_student)


# 3
# У компанії є всі зареєстровані працівники та список тих, хто ще не пройшов інструктаж з техніки безпеки.
#  Знайди імена працівників, які ще не пройшли інструктаж:

# employees = {"e1": "Oksana", "e2": "Roman", "e3": "Ihor", "e4": "Vira"}
# trained = {"e2", "e4"}

# employees_keys_list = set(employees.keys())
# print(employees_keys_list)

# not_trained = lambda x, y: x -y
# new_list =  not_trained(employees_keys_list, trained)

# not_trained_names = [employees[names] for names in new_list]
# print(new_list)


# 3
# workers = {"w1": "Anna", "w2": "Petro", "w3": "Olha", "w4": "Nazar"}
# certified = {"w2", "w4", "w5"}

# # common = set(workers.keys()) & certified
# common = lambda x, y: set(x.keys()) & y
# common_list = common(workers, certified)
# result = [workers[workers_id] for workers_id in common_list]
# print(result)