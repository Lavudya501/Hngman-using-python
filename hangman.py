import random

def choose_word():
    words = ['hangman', 'python', 'programming', 'code', 'challenge', 'learning','dharmendar']
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 0

    print("Welcome to Hangman!")
    print(word_to_guess)  

    while '_' in display_word(word_to_guess, guessed_letters) and attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input please enter letter not numeric.")
            continue

        if guess in guessed_letters:
            print("we have that word already guess other ")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(f"Incorrect! Attempts left: {max_attempts - attempts}")
        else:
            print("Correct!")

        print(display_word(word_to_guess, guessed_letters))

    if '_' not in display_word(word_to_guess, guessed_letters):
        print(f"Congratulations! You guessed the word: {word_to_guess}")
    else:
        print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
