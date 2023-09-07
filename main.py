#1
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1


#2
number = int(input('Write your number: '))
while number >= 0:
    print(number * 2.54)
    break
while number < 0:
    print('Not acceptable ')
    break


#3
nums = []

while True:
    num = input("Пиши сюда свой текст")
    if num.isdigit():
        nums.append(int(num))
    else:
        print(min(nums), max(nums))


#4


number = random.randint(1,10)

while True:
    try:

        number_guess = int(input("Choose a number between 1-10:"))

        if number_guess == number:
            print("You guessed the correct number!")
            break
        elif number_guess < number:
            print("Number guessed is too low. Try again.")
        else:
            print("Number guessed is too high. Try again.")

    except ValueError:
        print("Invalid input. Enter a valid number between 1-10.")


#5

username = 'python'
password = 'rules'

attempts = 0


while attempts < 5:
    username_input = input("Username:").lower()
    if username_input == username:
        a=input("password?")
        if a == password:
            print("welcome!")
            break
        else:
            print("That is the wrong password.")
    else:
        print("That is the wrong username")
        attempts += 1

if attempts == 5:
    print("Access denied.")
