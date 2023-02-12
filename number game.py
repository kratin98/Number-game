import random
number = random.randint(1,10)
player_name = input("Hello, what is your name?")
no_of_guesses=0
print('Okay!'+ player_name + 'I am guessing a number between 1 and 10')
while no_of_guesses<5:
    player_guess = int(input())
    no_of_guesses +=1
    if player_guess<number:
        print('too low')
    elif player_guess>number:
        print('too high')
    elif player_guess==number:
        break
if player_guess==number:
    print('You have guessed the number in', str(no_of_guesses), 'tries!!')
else:
    print('You didnt get the answer right, the answer was', str(number), '!')