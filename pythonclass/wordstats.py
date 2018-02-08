# -----------------------------------------------------------------------------
# Name:        wordstats
# Purpose:
#
# Author:      Randy Hoang
# Date:        2/07/2018
# -----------------------------------------------------------------------------
"""
Docstring: Enter your one-line overview here

and your detailed description
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
    reads a given file, line by line, then word by word,
    and returns a dictionary
    """
    # build and return the dictionary for the given filename
    word_dict = {}
    with open('pride.txt','r', encoding = 'utf-8') as my_file:
        for line in my_file:
            for word in line.split():
                word = word.strip(string.punctuation)
                lower_word = word.lower()
                print(lower_word)

            #word_dict["test"] = lower_word
            #print (word_dict)
                #if lower_word not in word_dict:
                #    word_dict[lower_word] = 0
                # word_dict[lower_word] = word_dict.get(lower_word, 0) + 1
            #print(word_dict)

def report(word_dict):
    """     Enter your function docstring here     """
    # report on various statistics based on the given word count dictionary


def main():
# get the input filename and save it in a variable
# call count_words to build the dictionary for the given file
# save the dictionary in the variable word_count
# call report to report on the contents of the dictionary word_count

# If you want to generate a word cloud, uncomment the line below.
# draw_cloud(word_count)
    my_file = open('pride.txt')
    count_words(my_file)

if __name__ == '__main__':
    main()
