# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.

# example
# alphabet_position("The sunset sets at twelve o' clock.")

# expected output
# "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

def alphabet_position(text):
    s = []
    for c in text.lower():
        if c.isalpha():
            s.append(str(ord(c)-96))
            
    return ' '.join(s)
