import random

guess_limit = 3


def get_word():
    with open('words.txt') as f:
        text = f.read()
    text_full = text.split()
    selected_word = random.choice(text_full)
    return selected_word


def play_game(secret_word):
    print(secret_word)
    print("Word looks like: " + "_" * len(secret_word))
    count = guess_limit
    success_char = []
    while count > 0:
        user_guess = input("Type a single letter here, ")
        listed = ''.join(
            [c if c in success_char else "_" for c in secret_word])
    if len(user_guess) > 1 or user_guess == "":
        print("Guess should only be 1 chracter")
        print("the word now looks like this: " + str(listed))
        print("You have " + str(count) + " guesses left.")
    elif user_guess not in secret_word:
        count -= 1
        print("There are no " + str(user_guess) + "'s in the word")
        if count == 0:
            print("Sorry, you lost. The secret word was: " + str(secret_word))
        else:
            print("You have " + str(count) + " guesses left")
            print("The word now looks like this: " + str(listed))
    else:
        print("The guess is correct")
        if user_guess not in success_char:
            success_char.append(user_guess)
        listed = ''.join(
            [c if c in success_char else "_" for c in secret_word])
        if set(success_char[:]) == set(secret_word[:]):
            print("Congrats!!!")
################################################################


def main():
    secret_word = get_word()
    play_game(secret_word)


if __name__ == "__main__":
    main()
