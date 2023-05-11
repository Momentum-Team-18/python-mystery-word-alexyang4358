import random


def play_game():
    with open('words.txt') as f:
        text = f.read()
    text_full = text.split()
    selected_word = random.choice(text_full)
    # hyphen_word = '_' * len(selected_word)
    # blank = ' '
    correct_letters = []

    # display_word = blank.join(selected_word)
    # hidden_word = blank.join(hyphen_word)

    # print(display_word)
    # print(hidden_word)

    print("Hello! Your random word has: " +
          str(len(selected_word)) + " characters.")

    for guess in selected_word:
        correct_letters.append('_')

    guesses = 3
    while guesses > 0:
        guess = input("Please enter one letter: " + str(correct_letters) + " ")
        if guess in selected_word:
            for i in range(len(selected_word)):
                if guess == selected_word[i]:
                    correct_letters[i] = guess
                    print("That letter is correct.")
        else:
            guesses -= 1
            print("Try again, you have " + str(guesses) + " left.")
    else:
        guesses = 0
        print("You lost, the word was: " + str(selected_word))


if __name__ == "__main__":
    play_game()
