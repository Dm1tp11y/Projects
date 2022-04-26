# 4. Реализуйте базовый класс Car.
#
#     у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#     опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#     добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#     для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "Мишана поехала "
    def stop(self):
        return "остановилась"
    def turn(self, direction):
        return "повернула к " + direction

class TownCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

honda = TownCar('Honda', 60, 'white')
print(honda.name, honda.color, honda.speed, honda.is_police)
print(honda.go(), honda.turn('городу'), honda.stop())
sport = SportCar('Honda', 180, 'red')
work1 = WorkCar('Honda', 90, 'white', True)
work2 = WorkCar('Lexus', 90, 'white', False)
police = PoliceCar('Honda', 180, 'red')