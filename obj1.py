class Animate(): # одушевленные
    age = 0
    is_alive = True
    name = ''
    def grow(self):
        self.age += 1
        print(f'{self.name} grows. Now {self.name} is {self.age} years old')
    # добавить функцию, которая меняет имя объекта
    pass

class Inanimate():  # неодушевленные
    pass

class Animals(Animate):

    def move(self):
        print(self.name, 'moved')

    def check(self):
        if self.is_alive:
            print('Alive')
        else:
            print('Dead')

class Plants(Animate):
    pass
class Bacteria(Animate):
    pass
class Rocks(Inanimate):
    pass
class Cars(Inanimate):
    name = ''
    pass

wolf = Animals()
wolf.name = 'Akella'
wolf.age = 10
print(wolf.name, wolf.age)
wolf.move()
fox = Animals()
fox.name = 'Red Devil'
fox.check()
wolf.grow()
fox.grow()

# добавить 3 разные функции в разные классы
# причем одна из функций должна быть в родительском классе
# создать объекты этих классов и запустить для них функции
