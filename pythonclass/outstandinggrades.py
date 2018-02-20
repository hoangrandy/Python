# -----------------------------------------------------------------------------
# Name:    Gradebook
# Purpose: To list out the students who made the cutoff score
#
#
# Author:   Randy Hoang
# Date:     02/19/2018
# -----------------------------------------------------------------------------
"""
This will list out all the students who made the cut

This program will copy the student dictionary and then deleted all the students
who was under the cutoff score then return the output 
"""


def main():


if __name__ == '__main__':
    main()
cs21a = {'Randy':100, 'Havish': 98, 'Anna': 92, 'Dan':60}


def outstanding(students, cutoff = 100):
    output = set()
    sample_set = students.copy()
    for grade in list(sample_set.keys()): # creates a list of keys
        if sample_set[grade] < cutoff:
            del sample_set[grade]

    for student in sample_set.keys():
        output.add(student)
    return output




def main():
    cuttoffgrade = int(input("Insert the cut-off grade: "))
    print(outstanding(cs21a, cuttoffgrade))


if __name__ == '__main__':
    main()
