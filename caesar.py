def encrypt(text, rot):
    message = ''
    for char in text:
        newchar = rotate_character(char, rot)
        message = message + newchar
    return message

def alphabet_position(char):
    newchar = unicode.lower(char)
    CharIndex = alphabet.index(newchar)
    return CharIndex


def rotate_character(char, rot):
    if char.isalpha() == True:
        LetterIndex = alphabet_position(char)
        RotatedIndex = LetterIndex + rot
        if RotatedIndex < 26:
            encrypted = alphabet[RotatedIndex]
        else:
            encrypted = alphabet[RotatedIndex % 26]
        if char.isupper() == True:
            return encrypted.upper()
        else:
            return encrypted
    return char

alphabet = 'abcdefghijklmnopqrstuvwxyz'
