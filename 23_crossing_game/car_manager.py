import random
from car import Car

MOVE_INCREMENT = 10
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]


class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_car()
        self.move_speed = 0.1

    def generate_car(self):
        is_generate = random.choices(population=[True, False], weights=(1, 5))[0]
        if is_generate:
            position = (280, 10 * random.randint(-25, 25))
            if len(self.cars) < 50:
                color = random.choice(COLORS)
                self.cars.append(Car(position, color))
            else:
                car = self.cars.pop(0)
                car.goto(position)
                self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())

    def increase_speed(self):
        self.move_speed *= 0.9

    def have_collision(self, x, y):
        collision = False
        for car in self.cars:
            if car.distance(x, y) < 20:
                collision = True
                break
        return collision
