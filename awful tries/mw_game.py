# module that allows us to randomize a list.
import random

# function that reads "words.txt".
# text_full = text.split() evaluates to a list
# with each word in the string as a single list item.
# line 14 is how we get our random word.


def random_word():
    with open('words.txt') as f:
        text = f.read()
    text_full = text.split()
    word = random.choice(text_full)
    print(word)
    return word


def display_word(word, guesses):
    display_word = ''
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
    return display_word


def main(word):
    letters_guessed = []
    guesses = 8
    print("\nHello! Solve this mystery word. \nYour random word has: " +
          str(len(word)) + " characters.")

    while True:
        if guesses != 0:
            print("\nYOU HAVE " +
                  str(guesses) + " CHANCES LEFT.")
            print("Word so far: " + display_word(word, letters_guessed))
            # print("Letters guessed: " + str(letters_guessed))
            guess = input("Guess: ")

            if guess not in letters_guessed:
                letters_guessed.append(guess)

            if display_word(word, letters_guessed) == word:
                print("\nCongrats! You got the right word: " + word)
                break

            else:
                guesses -= 1
                if guess in word:
                    print("Correct letter!")
                elif len(guess) != 1:
                    print('Please enter a single letter.')
                elif guess in letters_guessed:
                    print('You have already guessed that letter. Choose again.')
                elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                    print('Please enter a LETTER.')
                else:
                    print(guess + " is not in word")
        else:
            print("\nOops you ran out of guesses. Correct word was: " + word)
            break


def get_guess(already_guessed):
    already_guessed = ''
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


while True:
    word = random_word()
    main(word)
    if input("Would you like to continue? \nType 'y' to play again ").startswith("y"):
        main(word)
    if input("Would you like to continue? \nType 'n' to exit ").startswith("n"):
        break

    guesses = 0
    if input("Would you like to continue? \nType 'y' to play again ").startswith("y"):
        main(word)
    if input("Would you like to continue? \nType 'n' to exit ").startswith("n"):
        break
