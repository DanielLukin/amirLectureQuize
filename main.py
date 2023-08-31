#1
user = input('Print your name: ')
print('Hello,', user + '!')


#2
radius = float(input('Print the radius of the circle: '))
area = 3.14 * (radius ** 2)
print('Area of the circle = ', area)


#3
length = float(input('print the length of the rectangle: '))
width = float(input('print the width of the rectangle: '))
perimetr = (width + length) * 2
area = width * length
print('Perimetr of the rectangle = ', perimetr, '\n' + 'Area of the rectangle = ', area)


#4
number1 = int(input('Print first integer number: '))
number2 = int(input('Print second integer number: '))
number3 = int(input('Print third integer number: '))
s = number1 + number2 + number3
average = (number1 + number2 + number3) / 3
product = number1 * number2 * number3
print('Sum of three numbers = ', s, '\n', 'Product of three numbers = ', product, '\n', 'Average of three numbers = ', average )


#5
number1 = float(input('Write a mass in a talents: '))
number2 = float(input('Write a mass in a pounds: '))
number3 = float(input('Write a mass in a lots: '))
a = (number1 * 20 * 32 * 13.3) + (number2 * 32 * 13.3) + (number3 * 13.3)
b = a / 1000
c = a % 1000
print('The weight in modern units: ', b, 'kilograms ', c, 'grams')


                             # 3 Chapter
#1
length = int(input('How long is zander (in cm)'))
if length >= 42:
    print("It's good")
else:
    answer = 42 - length
    print('Catch ', answer, ' centimeters more fish to collect. This fish needs to be released.')


#2
c = input('Enter the cabin class of a cruise ship')
if c == 'LUX':
    print('Upper-deck cabin with a balcony')
elif c == 'A':
    print('Above the car deck, equipped with a window')
elif c == 'B':
    print('Windowless cabin above the car deck')
elif c == 'C':
    print('Windowless cabin below the car deck')
else:
    print('Invalid cabin class')


#3
user = input('Write your gender: ')
hem = int(input('Write your hemoglobin: '))
if user == 'Male':
    if hem > 167:
        print('You have high hemoglobin ')
    elif hem < 134:
        print('You have low hemoglobin ')
    else:
        print('You have normal hemoglobin ')
else:
    print('Invalid gender ')

if user == 'Woman':
    if hem > 155:
        print('You have high hemoglobin ')
    elif hem < 117:
        print('You have low hemoglobin ')
    else:
        print('You have normal hemoglobin ')
else:
    print('Invalid gender ')


#4
year = int(input(' Write a year: '))
if year % 4 == 0 or year % 400 == 0:
    print('The year is a leap year')
else:
    print('The year is not a leap year ')