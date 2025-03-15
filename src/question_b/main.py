#add import
from question_b import reverse_string

def main():
    
    keep_going = 'y'

    while keep_going == 'y' or keep_going == 'Y':
        string1 = str(input('Enter the word you would like to reverse: '))
        reversed = reverse_string(string1)
        
        print(reversed)

        keep_going = input('Would you like to keep going? Y/N ')
    
main()
