secretWord = 'disney'
userguess= '_'

guesses= ['_','_','_','_','_','_']

for 'd' in range (0,6):
    if (select word [1] == userguess)

if (userguess in secretword)
 for i in range (0.3)
    (secretword[1] == userguess)
for char in secret_word:
    secret_list.append(char)

current_word = ["p", "r", "i", "d", "e", "m", "o", "n", "t", "h"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
def isWordGuessed(secretWord,lettersGuessed):
    guess = 0
    while guess <= 8:
      secretLetters = list(secretWord)
      secretWordLen = len(secretLetters)
      letter = input('Enter a letter: ')
      lettersGuessed.append(letter)

      print('Letters guessed so far: ',lettersGuessed)

      if letter not in secredLetters:
          guess +=1
      while letter in secretLetters:
          secretLetters.remove(letter)
      if secretLetters == []:
          return True
  
      else:
          return False
      
      isWordGuessed(secretWord,lettersGuessed)