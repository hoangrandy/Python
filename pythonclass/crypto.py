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


    for letter in word.split():
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
        print (word + vowel_add)
    elif starts_with_vowel(word) == False:
        encrypt_word = word[1:]
        first_letter = word[0]
        encrypt_end = 'est'
        print(encrypt_word + first_letter + encrypt_end)




def decrypt(word):
    """
    decrypt a single word from the secret language
    If the word is not a valid word in the secret language, return None
    """



def translate(text, mode):
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

def choose_mode():
    """
    Prompt the user for input repeatedly until they enter 'E' or 'D'.
    Return the user's choice.
    """


    user_input = input("Press 'E' to encrypt or 'D' to Decrypt: ")
    if user_input == 'E':
        return user_input
    elif user_input == 'D':
        return user_input
    else:
        print("Please enter a valid key (Make sure you capitalize!)")



def main():

    # Prompt the user for the message to be translated.
    # Translate the message by calling translate - save result.
    # Print the result - or 'Invalid message' if applicable.

    encrypt_toggle = 'E'  # Get the user choice 'E' and save to a variable
    decrypt_toggle = 'D'  # Get the user choice 'D' and save it in a variable.

    choose_mode()
    word = input('Please enter the word or phrase you would like to be '
                 'encrypted/decrypted: ')
    if encrypt_toggle:
        encrypt(word)
    elif decrypt_toggle:
        decrypt(word)






if __name__ == '__main__':
    main()
