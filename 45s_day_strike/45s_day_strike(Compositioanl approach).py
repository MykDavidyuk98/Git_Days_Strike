import math
import random

class K18_07a:
    def __init__(self, x):
        self.plcolo = 3.14 * x * x
    
class K18_07b:
    def __init__(self, x):
        self.pltrik = math.sqrt(3) * x * x / 4

class K18_07:
    def __init__(self, x, y):
        self.plzag = x * y

    def func1 (self, r1, r2, a, m = 2, n = 2):
        self.p1 = K18_07a(r1)
        self.p2 = K18_07a(r2)
        self.p3 = K18_07b(a)
        self.k1 = m
        self.k2 = n
    
    def func2 (self):
        self.func2 = self.plzag - self.p1.plcolo * self.k1 - self.p2.plcolo * self.k2 - self.p3.pltrik
    
    def func3 (self):
        print(f'Загальна площа = {str(self.plzag)}см.кв')
        print(f'Залишок площі = {str(self.func2)}см.кв')

# ob = K18_07(30, 20)
# ob.func1 (4, 6, 5)
# ob.func2 ()
# ob.func3 ()

# Example from GPT
# Compositional approach in OOP
# Суть композиційного підходу в програмуванні полягає в тому, щоб створювати складні об’єкти з простіших, 
# використовуючи включення одних класів у інші як атрибути.
# Це дозволяє уникнути жорсткої ієрархії спадкування і зробити код гнучкішим і легшим для змін.

# class Engine:
#     def start(self):
#         print("Engine start")
    
# class Car:
#     def __init__(self):
#         self.engine = Engine()
    
#     def drive(self):
#         self.engine.start()
#         print('Car is moving')

# my_car = Car()
# my_car.drive()

# Який клас називають класом-контейнером? 
# Класом - контейнером називають клас, який містить інші обєкти(інших класів) як свої атрибути.
# Основна роль - обєднувати або керувати іншими обєктами, створюючи складну структуру
# Ознаки класу контейнера: 1) Має один або кілька атрибутів, які є обєктами інших класів
#                          2) Забезпечує доступ до функціоналу цих обєктів
#                          3) Часто використовується в композиції 
# Exapmle:

# class CPU:
#     def info(self):
#         return "Processor: Intel I5" 
    
# class RAM:
#     def info(self):
#         return "RAM: 16GB"

# # Клас-контейнер (Container-class), бо містить атрибути, які є обєктами класів CPU і RAM
# class Computer:
#     def __init__(self):
#         self.cpu = CPU()
#         self.ram = RAM()
    
#     def show_specs(self):
#         print(self.cpu.info())
#         print(self.ram.info())

# pc = Computer()
# pc.show_specs()

# Із якою Метою застосовують композиційний підхід? 
# 🔹 1. Гнучкості в проектуванні
# Компоненти можна легко замінювати, змінювати або повторно використовувати без зміни всієї структури.
# 🔹 2. Кращої модульності
# Об’єкти розділяються на незалежні частини (класи), які простіше тестувати, налагоджувати і розвивати.
# 🔹 3. Зменшення залежності від спадкування
# Композиція дозволяє уникнути складної ієрархії класів, що часто буває важко підтримувати.
# 🔹 4. Повторного використання коду
# Один і той самий клас можна використати в різних об'єктах-контейнерах.
# 📌 Висновок:
# Композиція допомагає створювати гнучкий, зрозумілий і зручний для змін код, що особливо важливо в великих і складних проєктах.

# 4 Поясніть сутність композиційного підходу в програмуванні на конкретному прикладі: 

# class Battery:
#     def info(self):
#         return "4000 mAh"

# class Screen:
#     def info(self):
#         return '6.5-inch OLED'

# class Camera:
#     def info(self):
#         return "48 MP"

# # Container - class
# class Smartphone: 
#     def __init__(self):
#         self.baterry = Battery()
#         self.camera = Camera()
#         self.screen = Screen()
    
#     def show_specs(self):
#         print(f'Screen: {self.screen.info()}')
#         print(f'Baterry: {self.baterry.info()}')
#         print(f'Camera: {self.camera.info()}')

# # using Compositional method in OOP
# phone = Smartphone()
# phone.show_specs()

# 🧠 Суть композиції тут в тому, що:
# -Клас Smartphone не наслідує інші класи.
# -Він включає (has-a) об’єкти інших класів як складові частини.
# -Це дозволяє легко замінити або змінити окремий компонент (наприклад, нову батарею чи камеру) — не змінюючи решту класу.

# 📌 Висновок:
# Композиція — це коли "об’єкт складається з інших об’єктів", і ми будуємо складні системи з простіших модулів.

# Exersice 1 from 8.3 st.143 

class Book_A5:
    def __init__(self, width, height):
        self.plbook = width * height

class Page_A4:
    def __init__(self, width, height):
        self.plpage = width * height

class Desk:
    def __init__(self, l, p):
        self.pldesk = l * p
    
    def math_pl(self, book_w, book_h, page_w, page_h):
        self.p1 = Book_A5(book_w, book_h)
        self.p2 = Page_A4(page_w, page_h)
    
    def math_diff_pl(self):
        self.math_diff = self.pldesk - (self.p1.plbook + self.p2.plpage)
    
    def show_pl(self):
        print(f'Загальна площа столу: {str(self.pldesk)}см.кв')
        print(f'Книга займає площу: {str(self.p1.plbook)}см.кв')
        print(f'Аркуш займає площу: {str(self.p2.plpage)}см.кв')
        print(f'Залишок площі = {str(self.math_diff)}см.кв')

ob1 = Desk(10, 15)
ob1.math_pl(5, 10, 2, 5)
ob1.math_diff_pl()
ob1.show_pl()
        