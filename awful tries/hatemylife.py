import random


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
            print(display_word(word, letters_guessed))
            guess = input("Guess: ")

            if guess not in letters_guessed:
                letters_guessed.append(guess)

            if display_word(word, letters_guessed) == word:
                print("\nCongrats! You got the right word: " + word)
                print('Do you want to play again? (yes or no)')
                return input().lower().startswith('y')

            else:
                if guess in word:
                    print("Correct letter!")
                else:
                    guesses -= 1
                    print(guess + " is not in word")
        else:
            guesses = 0
            print("\nOops you ran out of guesses. Correct word was: " + word)
        if guesses == 0:
            print('Do you want to play again? (yes or no)')
            return input().lower().startswith('y')


while True:
    word = random_word()
    main(word)
#     if input("Would you like to continue? \nType 'y' to play again ").startswith("y"):
#         main(word)
#     if input("Would you like to continue? \nType 'n' to exit ").startswith("n"):
#         break

#     guesses = 0
#     if input("Would you like to continue? \nType 'y' to play again ").startswith("y"):
#         main(word)
#     if input("Would you like to continue? \nType 'n' to exit ").startswith("n"):
#         break
