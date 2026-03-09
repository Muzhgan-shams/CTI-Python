# hangman
import random
from hangman_words import words_list
from hangman_words import logo
from hangman_arts import stages

print(logo)
chosen_word = random.choice(words_list).lower()
game_over = False
correct_letters = []
lives = 6
while not game_over:
    print(f"***********{lives}/6 lives***********")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print("You already guessed this letter")
    # Placeholder _
    blank = ""
    for i in range(0, len(chosen_word)):
        blank += "_"

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed wrong, {lives} left")
        if lives == 0:
            game_over = True
            print(f"You lost 🥲 The word was {chosen_word}")
    print(display)
    if "_" not in display:
        game_over = True
        print("You Won!")
    print(stages[-lives-1])
