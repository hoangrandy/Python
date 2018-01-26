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
    Enter your function docstring here
    """
    # return True if the word starts with a vowel and False otherwise

def encrypt(word):
    """
    Enter your function docstring here
    """
    # encrypt a single word into the secret language
    # call starts_with_vowel to decide which pattern to follow
    # return a single word (encrypted)


def decrypt(word):
    """
    Enter your function docstring here
    """
    # decrypt a single word from the secret language
    # If the word is not a valid word in the secret language, return None

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
        encrypt()
    elif user_input == 'D':
        decrypt()
    else:
        print("Please enter a valid key (Make sure you capitalize!)")

def main():
    # Get the user choice 'E' or 'D' and save it in a variable.
    # Prompt the user for the message to be translated.
    # Translate the message by calling translate - save result.
    # Print the result - or 'Invalid message' if applicable.


if __name__ == '__main__':
    main()