
word = 'transistor'
print(word)

guesses = 8
display = '_' * (len(word))

print("\nYour random word has: " + str(len(word)) + " characters.")

game_over = False
while not game_over:
    print(str(guesses))
    print(display)
    guess = input('Please guess a letter')
