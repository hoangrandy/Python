# -----------------------------------------------------------------------------
# Name:        spam
# Purpose:     determines if a message is spam or not
#
# Author:      Randy Hoang
# Date:        02/01/2018
# -----------------------------------------------------------------------------
"""
This program determines whether or not your message is considered spam

This is based on the number of unique words that are in the message, it will
take the number of spam words and divide it by the total unique words in the
message given.
"""
SPAM_WORDS = {'opportunity', 'inheritance', 'money', 'rich', 'dictator',
              'discount', 'save', 'free', 'offer', 'credit',
              'loan', 'winner', 'warranty', 'lifetime', 'medicine',
              'claim', 'now', 'urgent', 'expire', 'top',
              'plan', 'prize', 'congratulations', 'help', 'widow'}

def spam_indicator(text):
    """
    This function returns the spam indicator rounded to two decimals
    """


    set_input = set() # Create an empty set
    text = text.lower() # lower case all the words in the input
    new_text = text.split() # Split the user input
    for word in new_text: # For every word that is in the table
        set_input.add(word) # Store it in this set, set_input
    #text_split = text.split() another possible method to create a set
    #new_set = set(text_split)
    spam_match = set_input & SPAM_WORDS #Join the two sets and see what matches
    spam_checker = len(spam_match)/len(set_input) # see the % of spam words
    spam_check = round(spam_checker,2) # Store spam_checker with 2 decimal pnt


    return spam_check



def classify(indicator):
    """
    This function will test if the spam_check is considered spam or not
    If it is higher than 10%, it is SPAM, otherwise print ham
    PRINTs spam or ham
    """
    # This function prints the spam classification
    if indicator <= .1: # if the percentage is lower than 10% than not spam
        print('The message is: HAM')
    elif indicator > .1: # if percentage is higher than 10% of unique words
        print('The message is SPAM')  # SPAAAAAAAAAAAM

def get_input():
    """
    This function prompts the user for input
    RETURNS: input
    """
    # Prompt the user for input and return the input
    user_input = input('Please enter your message: ')
    return user_input # return user input

def main():
    # Get the user input and save it in a variable
    user_input = get_input()

    # Call spam_indicator to compute the spam indicator and save it
    spam_indicator(user_input)

    spam_check = spam_indicator(user_input)
    # Print the spam_indicator
    print('Spam Indicator: ',spam_check)

    # Call classify to print the classification

    classify(spam_check)



if __name__ == '__main__':
    main()
