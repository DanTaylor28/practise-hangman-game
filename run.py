import random

def welcome():
    """
    takes users name input and ensure its only alphabetic keys.
    """
    name = input("Welcome to hangman! Enter your name: ")

    if name.isalpha() == True:
        print(f'Hi {name}! Welcome to the game. The computer will randomly choose a word, and you will attempt to guess what the word is. Goodluck and have fun!')
    else:
        print('Please enter your name using letters only.') 
        name = input('Enter a game name here: ')
        print(f'Hi, {name}, welcome to the game!')

def play_again():
    """
    Asks user if they wish to replay game.
    """
    response = input('Would you like to play again? yes/no Enter "Y" for yes or "N" for no.')

    #Create decision making process
    if response == 'Y':
        game_run()
    else:
        print('Hope you had fun playing, see you next time')
    

    


welcome()
play_again()
