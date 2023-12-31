import random

class Car:
    def __init__(self, name, speed, reliability):
        self.name = name
        self.speed = speed
        self.reliability = reliability
        self.distance = 0

    def drive(self):
        if random.random() < self.reliability:
            self.distance += self.speed

    def __str__(self):
        return f"{self.name:<15} | Speed: {self.speed} km/h | Distance: {self.distance} km"

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.drive()
            car.speed += random.randint(-5, 5)
            car.speed = max(0, car.speed)

    def print_status(self):
        print(f"{'Car':<15} | {'Speed':<15} | {'Distance':<15}")
        print("-" * 45)
        for car in self.cars:
            print(car)
        print("-" * 45)

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False

cars = [Car(f"Car-{i+1}", random.randint(100, 200), random.uniform(0.7, 0.9)) for i in range(10)]

grand_demolition_derby = Race("Grand Demolition Derby", 8000, cars)

hour = 1
while not grand_demolition_derby.race_finished():
    grand_demolition_derby.hour_passes()
    if hour % 10 == 0:
        grand_demolition_derby.print_status()
    hour += 1

grand_demolition_derby.print_status()
print("The race has finished")