import random


with open('hangman_data.txt') as f:
    words = f.read()

guessed_words = set()
words = words.lstrip('[').rstrip(']').split(',')
guess_word = random.choice(words).strip('"').lower()
new_word = list(guess_word)

for i in range(random.randint(len(guess_word)//2, (len(guess_word)))):
    index = random.randint(0, len(guess_word)-1)
    new_word[index] = '_'

for word in (''.join(new_word)):
    if word != "_":
        guessed_words.add(word)
        for index, letter in enumerate(guess_word):
            if letter == word:
                new_word[index] = letter

print("Guess the word: ")
print("\n")
print(''.join(new_word))
print("\n")

tries = 5
won = False

while(tries != 0):
    guess_letter = input('guess the letter: ')

    if guess_word == ''.join(new_word):
        print('congrats you won')
        won = True
        break

    if (guess_letter in guess_word) and (guess_letter not in ''.join(new_word)):
        for index, letter in enumerate(guess_word):
            if letter == guess_letter:
                new_word[index] = guess_letter

        print('Correct guess: The word now is')
        print(''.join(new_word))
        guessed_words.add(guess_letter)

        if guess_word == ''.join(new_word):
            print('congrats you won')
            won = True
            break
    else:
        if guess_letter in guessed_words:
            print(
                'you have already guessed this letter or it already is revealed. Try again')
        else:
            guessed_words.add(guess_letter)
            tries -= 1
            print(
                f'There is no {guess_letter} in the _ word. You have {tries} tries left')

if not won:
    print(f'You lost. The word was {guess_word}')
