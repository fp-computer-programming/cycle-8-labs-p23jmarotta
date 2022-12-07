# Creator JM 12/7/22

def count_a(word):
    word = word.lower() # make sure the word is lowercased
    letters = [char for char in word] # split word into list of letters
    a_count = 0 # number of a's
    i = 0
    while len(letters) > i: # while the increment is less than the letter of words
        if letters[i] == 'a':
            a_count += 1
        i += 1

    return a_count

print(count_a('Yay')) # prints '1'
print(count_a('Alpha')) # prints '2'