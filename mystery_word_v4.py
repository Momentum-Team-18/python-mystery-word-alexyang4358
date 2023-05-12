import random


def play_game():
    with open('words.txt') as f:
        text = f.read()
    text_full = text.split()
    selected_word = random.choice(text_full)
    correct_letters = []

    print("Hello! Your random word has: " +
          str(len(selected_word)) + " characters.")

    while True:
        guess = input()
        guess = guess.lower()
        guesses = 3
        for guess in selected_word:
            correct_letters.append('_')
            # print(selected_word)
        while guesses > 0:
            guess = input("Please enter one letter: " +
                          str(correct_letters) + " ")
            for i in range(len(selected_word)):
                if guess == selected_word[i]:
                    correct_letters[i] = guess
                    already_guessed = [i]
                    print("That letter is correct.")
                    if len(guess) != 1:
                        print('Please enter a single letter.')
                    elif guess in already_guessed:
                        print('You have already guessed that letter. Choose again.')
                    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                        print('Please enter a LETTER.')
                    else:
                        return guess
            else:
                guesses -= 1
                print("Try again, you have " + str(guesses) + " left.")
        else:
            guesses = 0
            print("You lost, the word was: " + str(selected_word))

        break


if __name__ == "__main__":
    play_game()
