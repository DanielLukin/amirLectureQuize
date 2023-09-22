# number 1
'''
import random
try:
    user = int(input('Enter your number of rolls: '))
    sum = 0
    for i in range(user):
        roll = random.randint(1, 6)
        sum += roll
    print(sum)
except ValueError:
    print('Enter the number of rolls: ')
'''

#number 2
'''
nums = []

while True:
    user_input = input("Enter numbers: ")
    if user_input == "":
        break
    try:
        number = input(user_input)
        nums.append(number)
    except ValueError:
        print("Please write a number: ")

if not nums:
    print("No numbers! ")
else:
    nums.sort()
    nums.reverse()
    top_five = nums[:5]

    print("The five greatest numbers are :")
    for i, num in enumerate(top_five, start=1):
        print(f"{i}: {num}")
'''

#number 3
'''
def function(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    num = int(input("Enter a number: "))
    if function(num):
        print(f"{num} is a prime number!")
    else:
        print(f"{num} is not a prime number!")
except ValueError:
    print("Please enter a valid number: ")
'''
#number 4
'''
cities = []
for i in range(5):
    city_name = input(f"Enter the name of city {i + 1}: ")
    cities.append(city_name)

print("city:")
for city in cities:
    print(city)
'''