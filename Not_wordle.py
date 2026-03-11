secret_word ='banana'
max_guess = 5
current_guess = 1

print('Not-wordle')

guess = input('guess: ')
#the  range(len(guess)) This creates a list of numbers representing the positions of the letters (0 for the 1st letter, 1 for the 2nd, etc.)
for l in range(len(guess)):
#guess[l] just lets the string to be used for letter
    letters = guess[l]

    if guess == secret_word:
        print('ok')
