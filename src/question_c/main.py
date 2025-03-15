#add import
from question_c import get_random_number 

#game loop 1 
def main():
    keep_going = 'y'

    while keep_going == 'y' or keep_going == 'Y':

        number = get_random_number()
        guess = int(input('Guess a number between 1 and 5 '))

        if number == guess:
            print("Congratulations! You'ved guessed the right number")
            

        else:
            print(f'Try again next time! The correct answer was {number}')

        keep_going = input('Would you like to keep going? Y/N' )

#game loop 2 
def keep_guessing():
    keep_going = 'y'

    while keep_going == 'y' or keep_going == 'Y':

        number = get_random_number()
        guess = int(input('Guess a number between 1 and 5 '))

        if number == guess:
            print("Congratulations! You'ved guessed the right number")
            keep_going = input('Would you like to keep going? Y/N' )
            

        else:
            print(f'Try again next time! The correct answer was {number}')


        

