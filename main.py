import random
import sys

print("Welcome to the game.\nHere you have 6 lives to correctly guess the word\n")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 7


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if letter not in display:
      lives -=1
      if lives == 0:
        print(f"{stages[lives]}")
        print(f"Lives remaning: {lives}\nYou Loose")
        print(f'\nThe solution is "{chosen_word}".')
        break
        
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(f"lives remaining: {lives}\n{stages[lives]}")

sys.exit()