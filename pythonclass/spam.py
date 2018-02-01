# -----------------------------------------------------------------------------
# Name:        spam
# Purpose:
#
# Author:
# Date:
# -----------------------------------------------------------------------------
"""
Enter your module docstring with a one-line overview here

and a more detailed description here.
"""
SPAM_WORDS = {'opportunity', 'inheritance', 'money', 'rich', 'dictator',
              'discount', 'save', 'free', 'offer', 'credit',
              'loan', 'winner', 'warranty', 'lifetime', 'medicine',
              'claim', 'now', 'urgent', 'expire', 'top',
              'plan', 'prize', 'congratulations', 'help', 'widow'}

def spam_indicator(text):
    """
    Enter your function docstring here
    """
    # This function returns the spam indicator rounded to two decimals

    set_input = set() # Create an empty set
    text = text.lower() # lower case all the words in the input
    new_text = text.split() # Split the user input
    for word in new_text: # For every word that is in the table
        set_input.add(word) # Store it in this set, set_input
    #text_split = text.split() another possible method to create a set
    #new_set = set(text_split)
    spam_match = set_input & SPAM_WORDS #Join the two sets and see what matches
    spam_checker = len(spam_match)/len(set_input) # see the % of spam words
    spam_check = f'{spam_checker:.2f}' # Store spam_checker with 2 decimal pnt

    return spam_check



def classify(indicator):
    """
    Enter your function docstring here
    """
    # This function prints the spam classification

def get_input():
    """
    Enter your function docstring here
    """
    # Prompt the user for input and return the input
    user_input = input('Please enter your message: ')
    return user_input

def main():
    # Get the user input and save it in a variable
    # Call spam_indicator to compute the spam indicator and save it
    # Print the spam_indicator
    # Call classify to print the classification
    user_input = get_input()
    spam_indicator(user_input)


if __name__ == '__main__':
    main()
