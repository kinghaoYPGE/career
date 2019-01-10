# 狗，蝙蝠，鹦鹉，鸵鸟
"""
animal
|--mammal
    |--m_run
    |--m_fly
|--bird
    |--b_run
    |--b_fly
"""
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Speakable(object):
    pass

class Dog(Mammal, Runnable, Speakable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird, Flyable):
    pass
class Ostrich(Bird, Runnable):
    pass