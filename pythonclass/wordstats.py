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
import pickle


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
    with open('text.txt','r', encoding = 'utf-8') as my_file: # opens file
        for line in my_file: # read the file line by line
            for word in line.split(): # read the line word by word
                word = word.strip(string.punctuation) # remove the punctuations
                no_punc = word.strip(string.digits) #fix this, doesn't work
                #translator = str.maketrans('','', '0123456789')
                #no_punc = (word.translate(translator))
                lower_word = no_punc.lower() # lowercases all the words
                #word_dict[word] = lower_word.count(word)
                if lower_word not in word_dict: #and lower_word not in numbers:
                    word_dict[lower_word] = 1
                else:
                    word_dict[lower_word] += 1
    return word_dict


def report(word_dict):
    """     Enter your function docstring here     """

    for word in sorted(word_dict): #prints words in alphabetical order
        alpha_order = (f'{word}: {word_dict[word]}')
        with open('example.txt', 'a', encoding='utf-8') as new_file:
            new_file.write(alpha_order + '\n' ) #writes into new file

    # These next few lines will order the dictionary and print out top 5 words
    frequency_list = sorted(word_dict, key = word_dict.get, reverse = True)
    print("The words sorted by frequency: ")
    frequency_top = frequency_list[:5]
    for word in frequency_top:
        print(f'{word}: {word_dict[word]}')
        



def main():
# get the input filename and save it in a variable
# call count_words to build the dictionary for the given file
# save the dictionary in the variable word_count
# call report to report on the contents of the dictionary word_count

# If you want to generate a word cloud, uncomment the line below.
# draw_cloud(word_count)
    my_file = open('text.txt')
    word_dict = count_words(my_file)
    report(word_dict)



if __name__ == '__main__':
    main()
