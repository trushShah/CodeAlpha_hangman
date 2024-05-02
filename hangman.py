import random

def choose_word():
    with open("words.txt", "r") as file:
        words = file.readlines()
    return random.choice(words).strip().upper()

def get_category(word):

    category = {
    "Fruits": ["APPLE", "BANANA", "ORANGE", "WATERMELON", "STRAWBERRY"],
    "Animals": ["CAT", "DOG", "ELEPHANT", "JELLYFISH", "KANGAROO", "PENGUIN", "TURTLE", "ZEBRA", "DOLPHIN"],
    "Musical Instruments": ["GUITAR", "XYLOPHONE", "VIOLIN"],
    "Plants/Flowers": ["FLOWER", "SUNFLOWER", "TREE"],
    "Sports/Activities": ["VOLLEYBALL", "BASKETBALL", "YOGA"],
    "Clothing/Accessories": ["HAT", "JACKET", "UMBRELLA"],
    "Food/Drink": ["ICE CREAM", "PIZZA", "CARROT"],
    "Nature/Geography": ["MOUNTAIN", "RAINBOW", "MOON", "STAR", "WATERFALL", "IGLOO"]
}
    for category, word_list in category.items():
        if word in word_list:
            return category
    return "Unknown"

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    hint_given = False
    incorrect_guesses = 0
    
    print("Welcome to Hangman!")
    print("The word contains", len(word), "letters.")
    
    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        
        guess = input("Please guess a letter: ").upper()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Please try again!")
        elif guess in word:
            print("Correct guess!")
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You've guessed the word:", word)
                break
        else:
            print("Sorry, that letter is not in the word.")
            attempts -= 1
            incorrect_guesses += 1
            if incorrect_guesses == 2 and not hint_given:
                category = get_category(word)
                if category != "Unknown":
                    print(f"Here's a hint: The word falls into the category of '{category}'.")
                    hint_given = True
            if attempts == 0:
                print("\nGame over! The word was:", word)
                break
    
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thank you for playing!")
hangman()
