import random


def play_game():
    with open('words.txt') as f:
        text = f.read()
    text_full = text.split()
    selected_word = random.choice(text_full)
    guess = ''
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False
    correct_letters = []
    spaces = '_' * len(selected_word)
    print(spaces)
    print(selected_word)

################################################################

    print("Hello! Your random word has: " +
          str(len(selected_word)) + " characters.")

    for guess in selected_word:
        correct_letters.append('_')

    while guess != selected_word and not (out_of_guesses):

        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
            if guess in selected_word:
                for i in range(len(selected_word)):
                    if guess == selected_word[i]:
                        correct_letters[i] = guess
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("Out of tries, you lose!")
    else:
        print("You win!" + " You guessed the correct word: " + str(selected_word))


if __name__ == "__main__":
    play_game()
