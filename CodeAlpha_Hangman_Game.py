import random

# List of words to choose from
words = ['python', 'hangman', 'codealpha', 'intern', 'project']

# Pick a random word
word = random.choice(words)

# Create a list to show the guessed letters as underscores
hidden_word = ['_'] * len(word)

# Keep track of guessed letters
guessed = []

# Number of wrong guesses allowed
lives = 6

print("🎮 Welcome to Hangman!")
print("Guess the word. You have", lives, "lives.\n")

# Main game loop
while lives > 0 and '_' in hidden_word:
    print("Word:", ' '.join(hidden_word))
    letter = input("Guess a letter: ").lower()

    # Check if input is valid
    if len(letter) != 1 or not letter.isalpha():
        print("⚠ Please enter only one letter.\n")
        continue

    # Check if letter was already guessed
    if letter in guessed:
        print("🔁 You already guessed that letter.\n")
        continue

    guessed.append(letter)

    # Check if letter is in the word
    if letter in word:
        print("✅ Correct!\n")
        for i in range(len(word)):
            if word[i] == letter:
                hidden_word[i] = letter
    else:
        lives -= 1
        print("❌ Wrong! Lives left:", lives, "\n")

# Check if player won or lost
if '_' not in hidden_word:
    print("🎉 You guessed it! The word was:", word)
else:
    print("💀 You lost. The word was:", word)
