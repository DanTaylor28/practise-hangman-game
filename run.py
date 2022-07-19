# import random

# def welcome():
#     """
#     takes users name input and ensure its only alphabetic keys.
#     """
#     name = input("Welcome to hangman! Enter your name: ")

#     if name.isalpha() == True:
#         print(f'Hi {name}! Welcome to the game. The computer will randomly choose a word, and you will attempt to guess what the word is. Goodluck and have fun!')
#     else:
#         print('Please enter your name using letters only.') 
#         name = input('Enter a game name here: ')
#         print(f'Hi, {name}, welcome to the game!')

# def play_again():
#     """
#     Asks user if they wish to replay game.
#     """
#     response = input('Would you like to play again? yes/no Enter "Y" for yes or "N" for no.\nPlay Again: ')

#     #Create decision making process
#     if response == 'Y':
#         run_game()
#     else:
#         print('Hope you had fun playing, see you next time')

# def get_word():
#     """
#     Generates a random word for user to guess.
#     """
#     words = ['python', 'cool', 'weather', 'exciting', 'happy']
#     return random.choice(words).lower()

# def run_game():
#     welcome()

#     #define variable alphabet
#     alphabet = ('abcdefghijklmnopqrstuvwxyz')

#     #set guess word to guess_word function for random word to be generated
#     word = get_word()

#     #initiate empty list for guessed letter
#     letters_guessed = []

#     #initiate tries variable for number of tries by the user
#     tries = 7

#     #set initial guess to false
#     guessed = False

#     #print empty line?
#     print()

#     #print guess hint for the user for number of letters contained in word
#     print('The word contains', len(word), 'letters')
#     print(len(word) * '- ')

#     #initiate while loop
#     while guessed == False and tries > 0:
#         print(f'You have {tries} tries')
#         guess = input('Guess a letter or enter the full word\n').lower()
#         #user inputs letter
#         if len(guess) == 1:
#             if guess not in alphabet:
#                 print('You are yet to enter a letter. Check your entry, make sure you enter a letter not a number.')
#             elif guess in letters_guessed:
#                 print('You have already guessed that letter.. Try again')
#             elif guess not in word:
#                 print('Sorry, that letter is not part of the word :(')
#                 letters_guessed.append(guess)
#                 tries -= 1
#             elif guess in word:
#                 print('Great job! That letters in the word!')
#                 letters_guessed.append(guess)
#             else:
#                 print('Check your entry.. You might have entered the wrong entry..')
#         #if user enters full word
#         elif len(guess) == len(word):
#             if guess == word:
#                 print('Great job! You guessed the word :D')
#                 guessed = True
#             else:
#                 print('Sorry, that was not the word..')
#                 tries -= 1
#         else:
#             print('The length of your guess is not the same length as the correct word.')
#             tries -= 1

#         status = ''
#         if guessed == False:
#             for letter in word:
#                 if letter in letters_guessed:
#                     status += letter
#                 else:
#                     status += '-'
#             print(status)

#         if status == word:
#             print('Great job! You guessed the word correctly!')
#             guessed = True
#         elif tries == 0:
#             print('Sorry, you ran out of tries..')

#     play_again()

# run_game()

import random
GAME_WORDS = 'hello goodbye smiling sunny delightful'.split()
HANGMAN = ['''
    +----+
         |
         |
         |
        === ''', '''
    +----+
    O    |
         |
         |
        === ''', '''
    +----+
    O    |
    |    |
         |
        === ''', '''
    +----+
    O    |
   /|    |
         |
        === ''', '''
     +----+
     O    |
    /|\   |
          |
         === ''', '''
     +----+
     O    |
    /|\   |
    /     |
         === ''', '''
     +----+
     O    |
    /|\   |
    / \   |
         === ''']

def intro():
    """
    Prints a welcome message to the terminal and an input
    to get the users name. Entering non alphabetic symbols
    or an input less than 2 letters raises an error
    which is handled by a try/except statement.
    """
    print('Welcome to Hangman! Guess the correct word before you are hung!')
    print('Guess 1 letter at a time or the full word if you feel confident.')

    while True:
        try:
            name = (str(input('Please enter your name below:\n')))
            if name.isalpha() and len(name) > 1:
                print(f'Hello {name}, we hope you enjoy playing & best of luck!')
                break
            else:
                raise TypeError
        except TypeError as e:
                print('The name you entered is invalid.. Please try again.')
                continue

def get_random_word(random_word):
    """
    Returns a random word from the list of game words defined above 
    using the random pack imported at the top of the code.
    """
    word = random.randint(0, len(random_word) -1)
    return(random_word[word])

def game_board(game_word, correct_guesses, incorrect_guesses):
    """
    Print out the expected animation of hangman to correspond to how many
    incorrect guesses have been made.
    Also prints out an f string showing the incorrect guesses made by 
    the user.
    """
    print(HANGMAN[len(incorrect_guesses)])
    print()
    print(f'Incorrectly guessed letters: {incorrect_guesses}\n')
    # print('missed letters:', end= ' ')
    # for letter in incorrect_guesses:
    #     print(letter, end=' ')
    # print()

# def hidden_answer():
#     """
#     Display dashes corresponding with the number of letters
#     in the word by iterating through with a for loop. 
#     Updates after each user guess inserting correctly guessed
#     letters obtained from the correct_guesses variable.
#     """
    dashes = len(game_word) * '-'

    for i, x in enumerate(game_word):
        if game_word[i] in correct_guesses:
            dashes = dashes[:i] + game_word[i] + dashes[i+1:]

    for letter in dashes:
        print(letter, end=' ')
    print()

def user_guess(guessed_letters):
    """
    Takes a users guess and establishes whether it is a
    single letter or full word guess. 
    Uses a while loop and if/elif statements to ensure a valid
    guess is entered.
    """
    while True:
        print('Enter your guess below.')
        print('Either a single letter or have a go at the whole word')
        print()
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('please enter single letter')
        elif guess in guessed_letters:
            print('youve already guessed that letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('please enter a letter!')
        else:
            return guess
        # if len(guess) == 1:
        #     if guess in guessed_letters:
        #         print(f'You guessed {guess}, you already guessed that. Try again')
        #     elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        #         print('Only guesses in the alphabet accepted.. Try again')
        #     else:
        #         return guess
        # elif len(guess) == len(game_word):
        #     if guess == game_word:
        #         print(f'{guess} is the word! Well done!')
        #         break
        #     else:
        #         print('That was incorrect.. Try again')
        # else:
        #     return guess

def play_again():
    """
    would user like to play again
    """
    print('do you want to play again? (yes or no)')
    return input().lower().startswith('y')


intro()
game_word = get_random_word(GAME_WORDS)
incorrect_guesses = ''
correct_guesses = ''
game_is_done = False


while True:
    game_board(game_word, correct_guesses, incorrect_guesses)
    # hidden_answer()

    guess = str(user_guess(incorrect_guesses + correct_guesses))

    if guess in game_word:
        correct_guesses = correct_guesses + guess

        foundAllLetters = True
        for i, x in enumerate(game_word):
            if game_word[i] not in correct_guesses:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'you win! the word is {game_word}')
            game_is_done = True
    else:
        incorrect_guesses = incorrect_guesses + guess

        if len(incorrect_guesses) == len(HANGMAN) - 1:
            game_board(game_word, correct_guesses, incorrect_guesses)
            print(f'You have run out of guesses after {incorrect_guesses} wrong guesses & {correct_guesses} correct guesses. ')
            print(f'The word you were looking for was {game_word}')
            game_is_done = True

    if game_is_done:
        if play_again():
            incorrect_guesses = ''
            correct_guesses = ''
            game_is_done = False
            game_word = get_random_word(GAME_WORDS)
        else:
            break
            







# intro()
# game_word = get_random_word(GAME_WORDS)
# game_board(game_word, correct_guesses, incorrect_guesses)
# hidden_answer()
# user_guess(guessed_letters)
# play_again()


