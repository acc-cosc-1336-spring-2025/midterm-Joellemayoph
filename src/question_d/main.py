#add import
from question_d import get_person_category

def main():
    keep_going = 'y'

    while keep_going == 'y' or keep_going == 'Y':

        age = int(input('Please enter your age. [Must be > 1 or < 125]: '))
        category = get_person_category(age)

        print(f'You are a(n) {category}')

        keep_going = input('Would you like to keep going? Y/N' )

main()