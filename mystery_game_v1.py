import random

with open('words.txt') as f:
    text = f.read()
text_full = text.split()
secret_word = random.choice(text_full)
word = secret_word.upper()
print(word)

replay = True
while replay:

    guesses = 8
    display = '_' * (len(word))
    guessed_letters = []

    print("\n---- Hello! Your random word has: " +
          str(len(word)) + " characters. ----\n")

    game_over = False
    while not game_over:
        print("YOU HAVE " + str(guesses) + " GUESSES REMAINING.\n")
        guess = input(
            '|||||||||||||| Please guess a letter: ' + '').upper()

        i = 0
        if guess in word:
            while word.find(guess, i) != -1:
                i = word.find(guess, i)
                display = display[:i] + guess + display[i+1:]
                i += 1
            guessed_letters += guess
            print("\nLETTERS ALREADY GUESSED: " + str(guessed_letters))
            print('Correct!\n')
            print(display)
        else:
            guessed_letters += guess
            print("letters already guessed: " + str(guessed_letters))
            print("Sorry, " + guess + " was incorrect.\n")
            print(display)
            guesses -= 1

        if word == display:
            print('you win!! the word was ' + word)
            game_over = True
        elif guesses == 0:
            print('womp womp. game over.')
            game_over = True

    again = input('Would you like to play again? (y/n) \n')
    if again == 'n':
        replay = False
    elif again == 'y':
        replay = True
