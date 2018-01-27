# -----------------------------------------------------------------------------
# Name:        crypto
# Purpose:     CS 21 assignment # 3
#
# Author:
# Date:
# -----------------------------------------------------------------------------
"""
Enter your docstring with a one-line overview here
and a more detailed description here.
"""


def starts_with_vowel(word):
    """
    return True if the word starts with a vowel and False otherwise
    """


    vowel_check = word[0]
    if vowel_check in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


def encrypt(word):
    """
    encrypt a single word into the secret language
    If the input starts with a vowel, then add tan to the end
    If the input starts with a non-vowel then take the first letter
    add it to the end instead and follow up with 'est'
    """

    if starts_with_vowel(word) == True: 
        vowel_add = 'tan'
        encrypt_vowel = word + vowel_add
        return encrypt_vowel
    elif starts_with_vowel(word) == False:
        encrypt_word = word[1:]
        first_letter = word[0]
        encrypt_end = 'est'
        encrypt_conson = encrypt_word + first_letter + encrypt_end
        return (encrypt_conson)


def decrypt(word):
    """
    decrypt a single word from the secret language
    If the word is not a valid word in the secret language, return None
    """
    remove_tan = word[0:-3]
    remove_est = word[0:-4]
    beg_letter = word[-4]
    est = word[-3:]
    vowel = ['a', 'e', 'i', 'o','u']

    if starts_with_vowel(word) == True and 'tan' in word:
        return remove_tan
    elif beg_letter not in vowel and est in word:
        decrypt_conson =  beg_letter + remove_est
        return decrypt_conson


def translate(word,mode):
    """
    Enter your function docstring here
    """
    # Translate (encrypt or decrypt) the whole message

    # Split the text into a list of words
    # if mode is 'E' encrypt each of the words in the list
    # if mode id 'D' decrypt each word in the list
    # Build a new list with these translated words
    # Reverse the list
    # join the list of reversed translated words into a single string
    # and return it


    indiv_words = word.split()
    encrypt_toggle = 'E'  # Get the user choice 'E' and save to a variable
    decrypt_toggle = 'D'  # Get the user choice 'D' and save it in a variable.
    for words in indiv_words:
        if mode == encrypt_toggle:
            encrypt(words)
            print (encrypt(word))

        elif mode == decrypt_toggle:
            decrypt(words)
            print (decrypt(word))





def choose_mode(mode):
    """
    Prompt the user for input repeatedly until they enter 'E' or 'D'.
    Return the user's choice.
    """

    if mode == 'E':
        return mode
    elif mode == 'D':
        return mode
    else:
        print("Please enter a valid key (Make sure you capitalize!)")
        exit()


def main(): #fix
    # Prompt the user for the message to be translated.
    # Translate the message by calling translate - save result.
    # Print the result - or 'Invalid message' if applicable.

    mode = input("Press 'E' to encrypt or 'D' to Decrypt: ")
    choose_mode(mode)
    word = input('Please enter the word or phrase you would like to be '
                 'encrypted/decrypted: ')
    translate(word,mode)




if __name__ == '__main__':
    main()