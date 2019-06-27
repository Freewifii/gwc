#import random

# A list of words that 
#potential_words = ["example", "words", "someone", "can", "guess"]

secret_word = "pridemonth"
sw_len = len(secret_word)
#word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
"pridemonth" = word.lower()

# Make it a list of letters for someone to guess
current_word = ["p", "r", "i", "d", "e", "m", "o", "n", "t", "h"] # TIP: the number of letters should match the word

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
# Some useful variables
guesses = []
maxfails = 20
fails = 0
the_word = "secret"
while fails < maxfails:
	guess = input("Guess a letter: ")
  
    print(guess in secret_word)

	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(current_word)

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")