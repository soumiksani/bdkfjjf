import random
numbers=[1,2,3,4,5,6,7,8,9]

print('Games start and guess a number from 1-9 ')
print('*'*40)
computer_numbers=random.choice(numbers)

while True:
    number =int(input('What is your Guess number: '))
    if computer_numbers == number:
        print('Congratulations')
        break
    else:
        print("hoy nai")