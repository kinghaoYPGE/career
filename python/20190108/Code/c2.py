# 子类(subclass)
# 父类(superclass)

class Animal(object):
    def run(self):
        print('Animal is running!')

class Dog(Animal):
    def run(self):
        print('Dog is running!') 
    
    def eat(self):
        print('Eating meat!')

class Cat(Animal):
    def run(self):
        print('Cat is running!')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running!')

# animal-like object
class Person(object):
    def run(self):
        print('Person is running!')

def run_twice(animal):
    animal.run()
    animal.run()

animal = Animal()
# animal.run()

dog = Dog()
# dog.run()
# dog.eat()
cat = Cat()
# cat.run()
# list_a = []
# r = isinstance(list_a, list)
# print(r)
# r = isinstance(animal, Animal)
# print(r)
# r = isinstance(dog, Animal)
# print(r)
# r = isinstance(cat, Animal)
# print(r)
# r = isinstance(dog, Dog)
# print(r)
# r = isinstance(animal, Dog)
# print(r)
# r = isinstance(cat, Dog)
# print(r)
# print(type(animal), type(dog))
run_twice(animal)
run_twice(dog)
run_twice(cat)
tortoise = Tortoise()
run_twice(tortoise)
person = Person()
# 鸭子类型 如file-like object
run_twice(person)
