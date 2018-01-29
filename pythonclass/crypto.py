# -----------------------------------------------------------------------------
# Name:        crypto
# Purpose:     encrypts messages and decrypts them
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
    using the input(word) as a parameter
    RETURNS : true if vowel, false if not vowel
    """


    vowel_check = word[0] # Set the first letter of the word as a variable
    if vowel_check in ['a', 'e', 'i', 'o', 'u']: # Check to see if vowel
        return True
    else:
        return False


def encrypt(word):
    """
    This function will encrypt the inputted (word). Add tan at the end of the
    word if the word starts with a vowel.  If word starts with a consonant
    then take the first letter move it to the end and add 'est' then reverse
    the phrase
    RETURNS: the encrypted message
    """

    if starts_with_vowel(word) == True:  # Runs the vowel check function
        vowel_add = 'tan' # Add 'tan' if the word starts with a vowel
        encrypt_vowel = word + vowel_add # Assign to variable the output
        return encrypt_vowel # return output
    elif starts_with_vowel(word) == False: # Runs vowel check for consonants
        encrypt_word = word[1:] # word except first letter
        first_letter = word[0] # first letter
        encrypt_end = 'est' # Add est to the end
        encrypt_conson = encrypt_word + first_letter + encrypt_end # output
        return encrypt_conson # return output


def decrypt(word):
    """
    This function will decrypt a secret message back to the user input
    RETURNS: The original message
    """
    if len(word) < 4: # Exit function if input is less than 4 letters
        print('Wrong input. Please enter an encrpyted message')
        main() # Return to main if invalid
    remove_tan = word[0:-3] # store input except last three letters 'tan'
    remove_est = word[0:-4] # Store input except last three letters + conson

    est = 'est'
    vowel = ['a', 'e', 'i', 'o','u'] # Store vowels in a variable
    beg_letter = word[-4] # original consonant
    if starts_with_vowel(word) == True and 'tan' in word: # if vowel + has tan
        return remove_tan # return input - 'tan'

    elif beg_letter not in vowel and est in word:
        decrypt_conson =  beg_letter + remove_est # original consonant + word
        return decrypt_conson # Return message
    else:
        print('Wrong input. Please enter an encrpyted message')
        exit()


def translate(word,mode):
    """
    This function takes each words and runs it through encrypt or decrypt
    and adding it to the list, then concat the words together
    RETURN: prints output
    """


    indiv_words = word.split() # split the phrase and store it
    encrypt_toggle = 'E'  # Get the user choice 'E' and save to a variable
    decrypt_toggle = 'D'  # Get the user choice 'D' and save it in a variable.
    my_list = [] # create a list


    for words in indiv_words: # loop for each word in list
        if mode == encrypt_toggle: # If user selected Encrypt make it go to
            encrypt(words) # Encrypt function

            my_list.append(encrypt(words)) # Add encrypted words to the list
            new_list = list(reversed(my_list)) # Reverse the list



        elif mode == decrypt_toggle: # If user select Decrypt make it go to
            decrypt(words) # Decrypt function
            my_list.append(decrypt(words)) # Add words to the list
            new_list = list(reversed(my_list)) # Rever the list




    output = ' '.join(new_list) # Concatenate the list
    print("The secret message is: ",output) # print out the list
    exit()


def choose_mode(mode):
    """
    This function will Return the users mode selection
    RETURNS: User selection in variable 'mode'
    """

    if mode == 'E': # If the input is E return E
        return mode
    elif mode == 'D':
        return mode # If the input is D return D
    else:
        print("Please enter a valid key (Make sure you capitalize!)")
        main() # Return to main if user did not select the correct option


def main():


    mode = input("Press 'E' to Encrypt or 'D' to Decrypt: ")
    choose_mode(mode)
    word = input('Please enter the word or phrase you would like to be '
                 'encrypted/decrypted: ')


    translate(word,mode) # Make input go to translate function




if __name__ == '__main__':
    main()