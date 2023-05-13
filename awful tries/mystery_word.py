import random


def play_game():
    with open('words.txt') as f:
        text = f.read()
    text_full = text.split()
    selected_word = random.choice(text_full)
    hyphen_word = '_' * len(selected_word)
    blank = ' '
    correct_letters = []

    display_word = blank.join(selected_word)
    hidden_word = blank.join(hyphen_word)

    print(display_word)
    print(hidden_word)

    guesses = 3

    while guesses > 0:
        guess = input("please enter a letter: " + str(hidden_word))
        if guess in selected_word:
            print("your guess is correct")
            for i in range(len(selected_word)):
                if guess == selected_word[i]:
                    correct_letters[i] = guess
                    print(correct_letters)
        else:
            guesses -= 1
            print("Try again, you have " + str(guesses) + " left.")


if __name__ == "__main__":
    play_game()
