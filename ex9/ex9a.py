"""
Hangman ( https://en.wikipedia.org/wiki/Hangman_(game) ) is a word puzzle on which the television game show Wheel of Fortune is based. The goal of the puzzle is for the player to guess a word, letter by letter, before making a predetermined number of incorrect letter guesses.  When a player guesses a correct letter, all instances of that letter are filled in for the corresponding blank.  When a player guesses an incorrect letter, a mark is counted against the player.  If too many marks for incorrect guesses are tallied before the player completes the word, the player loses the game.

Write a function named hangman_guesses that takes a string with some of the letters replaced by underscores and prints a list of words that could possibly be made by filling in the blanks following the rules of hangman.  Use the words.txt file as your dictionary.

Recall that the blanks cannot be filled with letters already known to be a part of the word.  

As an example, hangman_guesses('h_ngm_n') would print 'hangman' and 'hangmen'.  However, hangman_guesses('hangm_n') would only print 'hangmen' because the a has already been guessed.

Can you think of other word puzzles this might be useful towards?
"""
def hangman_guesses(word):
  result = []
  for line in check_len(word):
    is_Match = True
    for i in range(len(word)):
      if not (word[i] == line[i] or (word[i] == "_" and not line[i] in forbidden(word))):
          is_Match = False
    if is_Match:
      result.append(line.strip())
    
  print(result)

# letters "_" can not be
def forbidden(word):
  forbid = []
  for i in word:
    if i != "_":
      forbid.append(i)
  return forbid    

#limit words to the word that matches the length
def check_len(word):
  len_list = []
  for i in doc:
    if len(i) == len(word) + 1:
      len_list.append(i)
  return len_list

doc = open('C:\Projects\git_projects\Think-Python-2e\ex9\words.txt')
hangman_guesses('h_ngm_n')
