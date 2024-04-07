# Adds spaces bettween each letter in word
# example: hello -> "h e l l o"
def add_letter_spacing(word):
    new_word = ""
    for char in word:
        new_word += char + " "
    return new_word