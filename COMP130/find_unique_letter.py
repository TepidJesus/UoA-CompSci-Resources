
"""
Finds and returns a string of all the letters of two words that occur in one but not the other.
"""

def find_unique_letters(word_a, word_b):
    letters = []
    for char in word_a:
        if char not in word_b and char not in letters:
            letters.append(char)
        else:
            continue
    for char in word_b:
        if char not in word_a and char not in letters:
            letters.append(char)
        else:
            continue
        
    letters.sort()
    return "".join(letters)