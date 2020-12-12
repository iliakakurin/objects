class Animate(): # одушевленные
    age = 0
    is_alive = True
    pass

class Inanimate():  # неодушевленные
    pass

class Animals(Animate):
    name = ''

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
fox.check()

# добавить 3 разные функции в разные классы
# причем одна из функций должна быть в родительском классе
# создать объекты этих классов и запустить для них функции
