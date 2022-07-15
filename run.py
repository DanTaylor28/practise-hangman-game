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
    response = input('Would you like to play again? yes/no Enter "Y" for yes or "N" for no.\nPlay Again: ')

    #Create decision making process
    if response == 'Y':
        run_game()
    else:
        print('Hope you had fun playing, see you next time')

def get_word():
    """
    Generates a random word for user to guess.
    """
    words = ['python', 'cool', 'weather', 'exciting', 'happy']
    return random.choice(words).lower()

def run_game():
    welcome()

    #define variable alphabet
    alphabet = ('abcdefghijklmnopqrstuvwxyz')

    #set guess word to guess_word function for random word to be generated
    word = get_word()

    #initiate empty list for guessed letter
    letters_guessed = []

    #initiate tries variable for number of tries by the user
    tries = 7

    #set initial guess to false
    guessed = False

    #print empty line?
    print()

    #print guess hint for the user for number of letters contained in word
    print('The word contains', len(word), 'letters')
    print(len(word) * '- ')

    #initiate while loop
    while guessed == False and tries > 0:
        print(f'You have {tries} tries')
        guess = input('Guess a letter or enter the full word\n').lower()
        #user inputs letter
        if len(guess) == 1:
            if guess not in alphabet:
                print('You are yet to enter a letter. Check your entry, make sure you enter a letter not a number.')
            elif guess in letters_guessed:
                print('You have already guessed that letter.. Try again')
            elif guess not in word:
                print('Sorry, that letter is not part of the word :(')
                letters_guessed.append(guess)
                tries -= 1
            elif guess in word:
                print('Great job! That letters in the word!')
                letters_guessed.append(guess)
            else:
                print('Check your entry.. You might have entered the wrong entry..')
        #if user enters full word
        elif len(guess) == len(word):
            if guess == word:
                print('Great job! You guessed the word :D')
                guessed = True
            else:
                print('Sorry, that was not the word..')
                tries -= 1
        else:
            print('The length of your guess is not the same length as the correct word.')
            tries -= 1

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '-'
            print(status)

        if status == word:
            print('Great job! You guessed the word correctly!')
            guessed = True
        elif tries == 0:
            print('Sorry, you ran out of tries..')

    play_again()

run_game()
            


            



    

    




