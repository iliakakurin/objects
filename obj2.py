class Animate(): # одушевленные
    age = 0
    is_alive = True
    name = ''
    def grow(self):
        self.age += 1
        print(f'{self.name} grows. Now {self.name} is {self.age} years old')
    def rename(self, new_name):
        self.name = new_name
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
    power = None
    color = None
    production_year = None
    # добавим функцию, которая будет указывать мощность (лс), цвет и год выпуска
    
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
wolf.rename('Otello')
wolf.move()

# добавить 3 разные функции в разные классы
# причем одна из функций должна быть в родительском классе
# создать объекты этих классов и запустить для них функции
