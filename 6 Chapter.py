#1 number
'''
import random

def dice():
    return random.randint(1, 6)

def result():
    rolls = 0
    while True:
        result = dice()
        rolls += 1
        print(f"Roll {rolls}: {result}")
        if result == 6:
            break

result()
'''

#2 number
'''
user = int(input('Enter the number of sides of the dice: '))
import random

def dice():
    return random.randint(1, user)

def result():
    rolls = 0
    while True:
        result = dice()
        rolls += 1
        print(f"Roll {rolls}: {result}")
        if result == user:
            break

result()
print(result())
'''

#3 number

'''
def function(x):
    liter = x *  3.785
    return(liter)

while True:
    try:
        x = int(input('Enter volume in gallons: '))
        print(function(x))
        if x < 0:
            break
    except ValueError:
        print('Enter the number: ')
'''

# 4 number
'''
def calculate_sum(numbers):
    return sum(numbers)


def main():
    my_list = [1, 2, 3, 4, 5]

    total = calculate_sum(my_list)

    print(f"sum: {total}")

main()
'''

#5 number
'''
def remove(input_list):
    # Use a list comprehension to create a new list with only even numbers
    even_numbers = [x for x in input_list if x % 2 == 0]
    return even_numbers

def main():
    # Create a list of integers for testing
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Call the function to remove odd numbers
    modified_list = remove(original_list)

    # Print the original and modified lists
    print("Original list:", original_list)
    print("Modified list (odd numbers removed):", modified_list)

main()
'''

#6 number
'''
import math

def calculate(diameter_cm, price_eur):
    # Calculate the area of the pizza in square centimeters
    radius_cm = diameter_cm / 2
    area_cm2 = math.pi * (radius_cm**2)

    # Convert the area to square meters
    area_m2 = area_cm2 / 10_000

    # Calculate the unit price per square meter
    unit_price_per_m2 = price_eur / area_m2
    return unit_price_per_m2

def main():
    print("Pizza 1:")
    diameter1 = float(input("Enter the diameter in centimeters: "))
    price1 = float(input("Enter the price in euros: "))

    print("\nPizza 2:")
    diameter2 = float(input("Enter the diameter in centimeters: "))
    price2 = float(input("Enter the price in euros: "))

    unit_price1 = calculate(diameter1, price1)
    unit_price2 = calculate(diameter2, price2)

    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money.")
    elif unit_price2 < unit_price1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")

main()

'''