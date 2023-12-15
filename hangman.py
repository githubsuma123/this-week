import random
words = ["apple", "banana", "cherry", "dragonfruit", "elderberry"]


word = random.choice(words)


guessed_letters = []


max_guesses = 6


while max_guesses > 0:
    
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)


    guess = input("Guess a letter: ")

   
    if guess in word:
        print("Correct guess!")
        guessed_letters.append(guess)
    else:
        print("Incorrect guess!")
        max_guesses -= 1

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        break


if max_guesses == 0:
    print("Game over! You ran out of guesses. The word was:", word)