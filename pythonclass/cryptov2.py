# -----------------------------------------------------------------------------
# Name:        crypto
# Purpose:     CS 21 assignment # 3
#
# Author:      Randy Hoang
# Date:        1/27/2018
# -----------------------------------------------------------------------------
"""
This program Encrypt messages to a secret code or Decrypts a secret code

If you encrypt a message each word that starts with a vowel in the phrase will
add tan to the end of each word.  If the word starts with a consonant it will
take the first letter, move it to the end and add est.  Not only that but if
you encrypt multiple words it will also reverse it.  Decrypt just reverses
the encrypted message to regular text.
"""


def starts_with_vowel(word):
    """
    This function will check if the first letter of (original word) is a vowel
    RETURNS : true if vowel, false if not vowel
    """


    vowel_check = word[0]
    if vowel_check in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


def encrypt(word):
    """
    This function will encrypt the inputted message. Add tan at the end of the
    word if the word starts with a vowel.  If word starts with a consonant
    then take the first letter move it to the end and add 'est' then reverse
    the phrase
    RETURNS: the encrypted message
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
        return encrypt_conson


def decrypt(word):
    """
    This function will decrypt a secret message back to the user input
    RETURNS: The original message
    """
    if len(word) < 4:
        print('Wrong input. Please enter an encrpyted message')
        main()
    remove_tan = word[0:-3]
    remove_est = word[0:-4]

    est = 'est'
    vowel = ['a', 'e', 'i', 'o','u']
    beg_letter = word[-4]
    if starts_with_vowel(word) == True and 'tan' in word:
        return remove_tan

    elif beg_letter not in vowel and est in word and 'tan' not in word:
        decrypt_conson =  beg_letter + remove_est
        return decrypt_conson
    else:
        print('Wrong input. Please enter an encrpyted message')
        exit()


def translate(word,mode):
    """
    This function takes each words and runs it through encrypt or decrypt
    and adding it to the list, then concat the words together
    RETURN: prints output
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
    my_list = []


    for words in indiv_words:
        if mode == encrypt_toggle:
            encrypt(words)

            my_list.append(encrypt(words))
            new_list = list(reversed(my_list))



        elif mode == decrypt_toggle:
            decrypt(words)
            my_list.append(decrypt(words))
            new_list = list(reversed(my_list))




    output = ' '.join(new_list)
    print("The secret message is: ",output)
    exit()


def choose_mode(mode):
    """
    This function will Return the users mode selection
    RETURNS: User selection in variable 'mode'
    """

    if mode == 'E':
        return mode
    elif mode == 'D':
        return mode
    else:
        print("Please enter a valid key (Make sure you capitalize!)")
        main()


def main():
    

    mode = input("Press 'E' to Encrypt or 'D' to Decrypt: ")
    choose_mode(mode)
    word = input('Please enter the word or phrase you would like to be '
                 'encrypted/decrypted: ')


    translate(word,mode)




if __name__ == '__main__':
    main()