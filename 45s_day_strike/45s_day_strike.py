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
