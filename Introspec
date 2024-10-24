import pprint
import inspect


class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.model = __model
        self.engine_power = __engine_power
        self.color = __color

    def get_model(self):
        print(f'Модель: {self.model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.engine_power}')

    def get_color(self):
        print(f'Цвет: {self.color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in list(map(str.lower, self.__COLOR_VARIANTS)):
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


def introspection_info(obj):
    introspection = [type(obj), dir(obj), inspect.getmodule(obj)]
    return introspection


Car = Vehicle('Fedos', 'Toyota Mark II', 'blue', 500)
pprint.pprint(introspection_info(Car))
print("-----------------------------------------------------------------------------")
pprint.pprint(introspection_info(len))
