# -----------------------------------------------------------------------------
# Name:        wordstats
# Purpose:     Statistics on a textfile
#
# Author:      Randy Hoang
# Date:        2/07/2018
# -----------------------------------------------------------------------------
"""
Output the longest word,  top 5 most frequent words, create a new file w/ words

This program will ask the user for a file input.  It will print out one of the
longest words in the text file, print out the 5 most frequently used words, and
will create a new file called out.txt with the words in alpha order and the
number of times it was used in the file.
"""
import string
# The following imports are needed for the draw_cloud function.
import tkinter
import tkinter.font
import random



# The draw_cloud function is only needed for the optional part:
# to generate a word cloud.
# You don't need to change it.
def draw_cloud(input_count, min_length=0):
    """
    Generate a word cloud based on the input count dictionary specified.
    Parameters:
    input_count (dict): represents words and their corresponding counts.
    min_length (int):  optional - defaults to 0.
         minimum length of the words that will appear
         in the cloud representation.
    Only the 20 most common words (that satisfy the minimum length criteria)
    are included in the generated cloud.
    """
    root = tkinter.Tk()
    root.title("Word Cloud Fun")
    # filter the dictionary by word length
    filter_count = {
        word: input_count[word] for word in input_count
        if len(word) >= min_length}
    max_count = max(filter_count.values())
    ratio = 100 / max_count
    frame = tkinter.Frame(root)
    frame.grid()
    current_row = 0
    for word in sorted(filter_count, key=filter_count.get, reverse=True)[0:20]:
        color = '#' + str(hex(random.randint(256, 4095)))[2:]
        word_font = tkinter.font.Font(size=int(filter_count[word] * ratio))
        label = tkinter.Label(frame, text=word, font=word_font, fg=color)
        label.grid(row=current_row % 5, column=current_row // 5)
        current_row += 1
    root.mainloop()


# Enter your own helper function definitions here


def count_words(filename):
    """
    Reads a given file, line by line, then word by word
    Parameter: filename input from main
    Returns: Dictionary of the word and number of times it has appeared in file
    """
    # build and return the dictionary for the given filename
    word_dict = {}
    with open(filename,'r', encoding = 'utf-8') as my_file: # opens file
        for line in my_file: # read the file line by line

            for word in line.split(): # read the line word by word
                strip_word = word.strip(string.punctuation)
                strip_no = strip_word.strip(string.digits)
                lower_word = strip_no.lower() # lowercases all the words
                if lower_word:
                    if lower_word in word_dict.keys():
                        word_dict[lower_word] += 1
                    else:
                        word_dict[lower_word] = 1
    return word_dict


def report(word_dict):
    """
    This will print out the words in alpha order into a file, print the
    longest word, and print the top 5 most used words in the file and how many
    times.
    Note that if you already ran this program it will append over the file
    Returns: None except prints
    """

    for word in sorted(word_dict): #prints words in alphabetical order
        alpha_order = (f'{word}: {word_dict[word]}')
        with open('out.txt', 'a', encoding='utf-8') as new_file:
            new_file.write(alpha_order + '\n' ) #writes into new file


    # These next few line will find the longest word and print it out
    print("The longest word is: ")
    longestword = max(word_dict, key = len) # Find the longest word
    print(longestword) #Print it out


    # These next few lines will order the dictionary and print out top 5 words
    frequency_list = sorted(word_dict, key = word_dict.get, reverse = True)
    print("The top 5 words sorted by frequency: ")
    frequency_top = frequency_list[:5] # Store the top 5 words into a var
    for word in frequency_top: # For each word in frequency_top (5) print
        print(f'{word}: {word_dict[word]}')




def main():
# If you want to generate a word cloud, uncomment the line below.
# draw_cloud(word_count)
    filename = input("Please enter file name here: ")
    word_dict = count_words(filename)
    report(word_dict)



if __name__ == '__main__':
    main()