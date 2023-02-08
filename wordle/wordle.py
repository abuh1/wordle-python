import sys
import pandas as pd

def main():
    # Get command line argument for 5,6,7 or 8 letter words
    wordsize = int(sys.argv[1])
    if (len(sys.argv) != 2):
        print("Usage: py wordle.py wordsize")
        sys.exit()
    allowed_wordsize = [5, 6, 7, 8]
    if (wordsize not in allowed_wordsize):
        print("Error: wordsize must be either 5,6,7 or 8")
        sys.exit()
        
    # Pick random word
    word = choose_word(wordsize)
    
    print("--------------------------------------------------------------")
    print(f"This is WORDLE in the Python terminal!\nYou have {wordsize + 1} tries to guess the {wordsize}-letter word I am thinking of")
    print("--------------------------------------------------------------")
    # Main game loop
    guessed = False
    tries = 0
    while not guessed and tries != (wordsize + 1):
        print(f"Input a {wordsize}-letter word: ")
        guess = input("")
        if len(guess) != wordsize:
            print(f"Guess must be {wordsize}-letters long.")
            continue
        if guess == word:
            guess_state = check_guess(guess, word)
            print(guess_state)
            print("You got the word!\n")
            guessed = True
        else:
            guess_state = check_guess(guess, word)
            print(guess_state)
            tries += 1
        if tries == 6:
            print("Nice try, you ran out of tries!")

# Function to choose word at random
def choose_word(wordsize):
    # Create pandas dataframe for csv file
    words_df = pd.read_csv('words.csv')
    
    # Get column for number of letters chosen and choose one at randoms
    words_df = words_df.astype(str)
    available_words = words_df[f'{wordsize}-letter']
    
    # Chosen word
    word = available_words.sample().item()
    return word

# Compute the guess
def check_guess(guessed_word, word):
    guess = ""
    for i in range(len(guessed_word)):
        if(guessed_word[i] == word[i]):
            guess += f"\u001b[42;1m{guessed_word[i]}\u001b[0m"
        elif (guessed_word[i] in word) and (guessed_word[i] != word[i]):
            guess += f"\u001b[43;1m{guessed_word[i]}\u001b[0m"
        else:
            guess += f"\u001b[41;1m{guessed_word[i]}\u001b[0m"
    return guess
    
if __name__ == '__main__':
    main()