# Write your code here
import random
word_list = ['python', 'java', 'kotlin', 'javascript']
c_word = random.choice(word_list)
hidden_word = ('-' * len(c_word))
hidden_word = list(hidden_word)
arr_letters = list(c_word)
print('H A N G M A N')
print()
for i in range(8):
    printable_words = ''.join(t for t in hidden_word)
    print(printable_words)
    guess_letter = input('Input a letter: > ')
    if guess_letter in arr_letters:
        print()
        l_index = arr_letters.index(guess_letter)
        arr_letters[l_index] = '-'
        hidden_word[l_index] = guess_letter
    else:
        print('No such letter in the word\n')


print("Thanks for playing!")
print("We'll see how well you did in the next stage")
