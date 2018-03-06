# -----------------------------------------------------------------------------
# Name:        language
# Purpose:     generate a sentence
#
# Author:      Randy Hoang
# Date:
# -----------------------------------------------------------------------------
"""
module docstring
"""
import random
import string
# Enter your imports here


def learn(filename):
    """
    This function will open the file and read it once + strip punctuation
    and lowercase
    Then return a tuple (first, words)
    words will print out each word : whatever word follows that word
    Parameters: open a filename
    Returns: A Tuple (first word, dictionary of words followed by next words)
    """
    list = [] # Declare an empty set for the words
    with open(filename, 'r', encoding='utf-8') as my_file:

        text = my_file.read()


    for char in string.punctuation:
        text = text.replace(char, '')
        lower_text = text.lower()
    for word in lower_text.split():
        list.append(word)

    first = list[0]
    words = {}

    for index in list:

    #words = (first,dict)
    #print (words)





def sentence_generator(filename, length=10):
    """
    This will generate a sentence based on the inputted length, if none is
    inputted default to 10
    Rule is pick a key 'first word' then pick a another key from that value
    IF ending word is chosen, then start with the 'first' word again
    Parameters: Filename to read, length : length (words) of generated sentence
    """
    random.seed(1)  # Set the seed for the random generator - do not remove
    # Enter your code here

def main():
    learn('spider.txt')



if __name__ == "__main__":
    main()