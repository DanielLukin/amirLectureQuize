
# 3 Chapter
#1
'''
length = int(input('How long is zander (in cm)'))
if length >= 42:
    print("It's good")
else:
    answer = 42 - length
    print('Catch ', answer, ' centimeters more fish to collect. This fish needs to be released.')
'''

#2
'''
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
'''

#3
'''
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
'''

#4
'''
year = int(input(' Write a year: '))
if year % 4 == 0 or year % 400 == 0:
    print('The year is a leap year')
else:
    print('The year is not a leap year ')
'''