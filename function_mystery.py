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
                else:
                    print(guess + " is not in word")
        else:
            print("\nOops you ran out of guesses. Correct word was: " + word)
            break


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
