'''
#number 1
class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Publication Name: {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}")


if __name__ == "__main__":
    donald_duck_magazine = Magazine(name="Donald Duck", chief_editor="Aki Hyppä")
    compartment_no_6_book = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)

    donald_duck_magazine.print_information()
    print("\n")
    compartment_no_6_book.print_information()

#number 2

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


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(name=registration_number, speed=max_speed, reliability=random.uniform(0.7, 0.9))
        self.battery_capacity = battery_capacity

    def __str__(self):
        return super().__str__() + f" | Battery Capacity: {self.battery_capacity} kWh"


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_capacity):
        super().__init__(name=registration_number, speed=max_speed, reliability=random.uniform(0.7, 0.9))
        self.tank_capacity = tank_capacity

    def __str__(self):
        return super().__str__() + f" | Tank Capacity: {self.tank_capacity} Liters"


if __name__ == "__main__":
    electric_car = ElectricCar(registration_number="ABC-15", max_speed=180, battery_capacity=52.5)
    gasoline_car = GasolineCar(registration_number="ACD-123", max_speed=165, tank_capacity=32.3)

    hours = 3
    for _ in range(hours):
        electric_car.drive()
        gasoline_car.drive()

    print("Electric Car Status:")
    print(electric_car)

    print("\nGasoline Car Status:")
    print(gasoline_car)

'''