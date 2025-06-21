import random

print("Welcome to Hangman Game!")
word_list = ["aadhar","work",]
hangman_art ={
  "lives_0":'''
    +---+
   |   |
       |
       |
       |
       |
========='''
,

"lives_1":'''
  +---+
   |   |
   O   |
       |
       |
       |
========='''
,

"lives_2":'''
  +---+
   |   |
   O   |
   |   |
       |
       |
========='''
,
"lives_3":'''
 +---+
   |   |
   O   |
  /|   |
       |
       |
========='''
,

"lives_4":'''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
========='''
,
"lives_5":'''
  +---+
   |   |
   O   |
  /|\  |
  /    |
       |
========='''

,
"lives_6":'''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
========='''
}
lives = 6
guessing_word = random.choice(word_list)
place_holder = ""
word_length = len(guessing_word)
for position in range(word_length):
    place_holder+= "_"
print(place_holder)
game_over = False
correct_letters = []
print("************************you have 6 lives left**************************")
while not game_over:
    input_word= input("Guess the word : ").lower()
    display = ""
    print(input_word)
    for letter in guessing_word:
        if letter == input_word:
            display+=letter
            correct_letters.append(input_word)
            print(f"You've already guessed '{input_word}'. Try another letter.")
            continue
        elif letter in correct_letters:
             display+=letter
              
        else:
            display+="_"
    print("word to guess :"+display)
    if input_word not in guessing_word:
        lives-=1
        print(f"you guessed {input_word} not in the guessing word. You lose the life.you have {lives} lives left")
        print(hangman_art[f"lives_{6-lives}"])
        if lives == 0:
            game_over = True
            print("******************************you lose********************************")

        print(f"*************************you have{lives} lives left*******************************")
    if "_" not in display:
       game_over = True
       print("***************************you're win**********************************************")



