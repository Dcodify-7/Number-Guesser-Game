#Beginning

#import
import random


#main function + play gain function
def number_guesser():
    my_number = random.randint(1,10)
    print("Welcome to number guesser game")
    print()
    print("""The idea of the game is to guess 
the number I have picked. Number 
is between 1-10 (int numbers only)""")
    print()

    #error handling
    while True:
        try:
            number = int(input("Enter the number: "))
            break #if input is a full number
        except ValueError:
            print("Oopsy, that was not a valid number. Please try again.\n")


    # loop + error handling
    while number != my_number:
        print(f"{number} is wrong, hehehe ;p. Try again.\n")
        while True:
            try:
                number = int(input("Enter the number: "))
                break
            except ValueError:
                print("Oopsy, that was not a valid number. Please try again.\n")

    # When the loop ends, user guessed correctly
    if my_number == 7:
        print(f"Yup, you are right. Btw {my_number} is my favourite number ;)\n")
    else:
        print(f"Yup, you guessed it right! The number was {my_number}.\n")


if __name__ == "__main__":
    while True:
        number_guesser()
        play_again = input("Do you wanna play again? (y/n): ").lower()
        if play_again != "y":
            print("Thank you for playing! Bye ;p")
            break