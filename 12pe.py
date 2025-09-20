def play_hangman(word, max_wrong=6):
    """
    Play a game of Hangman.

    Parameters:
    word (str): The secret word to guess.
    max_wrong (int): Maximum number of wrong guesses allowed (default is 6).
    """
    # Step 1: Prepare the word
    word = word.strip().lower()
    if not word.isalpha():
        print("Invalid input. Please enter a valid word containing only letters.")
        return

    # Step 2: Initialize display and tracking variables
    status = ['_'] * len(word)
    wrong_guesses = 0
    guessed_letters = set()

    # Step 3: Main game loop
    while '_' in status and wrong_guesses < max_wrong:
        print("\nCurrent status:", ' '.join(status))
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")

        guess = input("Player 2, please guess a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        # Check if the guess is correct
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    status[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            wrong_guesses += 1

    # Step 4: Game end conditions
    print("\nFinal status:", ' '.join(status))
    if '_' not in status:
        print("🎉 Congratulations! You've guessed the word!")
    else:
        print(f"😢 Game over! You've used all your guesses. The word was: {word}")

# Optional: Tournament mode using *args
def tournament(*words):
    """
    Play multiple rounds of Hangman with different words.

    Parameters:
    *words (str): Words to be used in the tournament.
    """
    print("🌟 Welcome to the Hangman Tournament! 🌟")
    for i, word in enumerate(words, start=1):
        print(f"\n--- Round {i} ---")
        play_hangman(word)
    print("\n🏆 Thanks for playing the tournament!")

# Example usage:
if __name__ == "__main__":
    # Get the secret word from Player 1
    secret_word = input("Player 1, enter the secret word (letters only, no spaces): ")
    play_hangman(secret_word)

    # Optional tournament mode example:
    # tournament("python", "hangman", "challenge", "programming")
