# Creator JM 12/7/22

def is_palindrome(word):
    word = word.lower()
    letters = [char for char in word] # split the word into letters
    i = 0
    check = 0
    while len(letters) > i: # Go through every letter
        if letters[i] == letters[-1 + -i]: # if letter equals the letter on the other side of the word
            check += 1 # give the word a point
        i += 1
    if check == len(letters): # if every letter is the same
        return True
    else:
        return False

print(is_palindrome('miraclelcarim')) # returns True
print(is_palindrome('alex')) # returns False