import random


def play_game():
    with open('words.txt') as f:
        text = f.read()
        text_full = text.split()
        selected_word = random.choice(text_full)
        hyphen_word = selected_word.replace("a-z", "_")

    guesses = 2
    while guesses > 0:
        letter = input('Your word is: ' + str(hyphen_word) +
                       '. Guess first letter: ')
        if letter in selected_word:
            print("good job")
        else:
            print("nope")
            guesses -= 1


if __name__ == "__main__":
    play_game()
