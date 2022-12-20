# 4) Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте
# в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод
# show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните
# доступ к атрибутам, выведите результат. Выполните вызов методов и
# также покажите результат.

class Car:
    speed = 0
    color = None
    name = None
    is_police = False

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print('Car started')

    def stop(self):
        print('Car stopped')

    def turn(self, direction):
        print('Car turn to the ' + direction)

    def show_speed(self):
        print(f'Car speed is {self.speed}')


class TownCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        if speed > 60:
            print(
                f"Car {name} speed is {self.speed}, it's TOO FAST. Calm down.")


class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)


class WorkCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        if speed > 40:
            print(
                f"Car {name} speed is {self.speed}, it's TOO FAST. Calm down.")


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


car_1 = TownCar('Mazda', 58, 'black')
car_2 = PoliceCar('Skoda', 80, 'white')
car_3 = TownCar('Audi', 75, 'blue')
car_4 = WorkCar('Honda', 39, 'white')
car_5 = WorkCar('Citroen', 44, 'red')
car_6 = SportCar('Bmw', 102, 'brown')

print()
print(car_1.name, car_1.color, car_1.speed, car_1.is_police)
print(car_1.go(), car_1.turn('left'), car_1.show_speed(), car_1.stop())

print()
print(car_2.name, car_2.color, car_2.speed, car_2.is_police)
print(car_2.go(), car_2.turn('left'), car_2.show_speed(), car_2.stop())
