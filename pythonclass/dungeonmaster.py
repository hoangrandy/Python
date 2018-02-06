# -----------------------------------------------------------------------------
# Name:        Dungeon
# Purpose:     A Dungeon Game in python 3
#
# Author: Randy Hoang
# Date: 02/05/2018
# -----------------------------------------------------------------------------
"""
Dungeon Master

The game in python 3
"""





def user_input():
    """
    This function asks for the input then stores it in a variable
    :return: input
    """
    userinput = input(' ')
    return userinput


def entrance():
    print("""You wake up, everything is blurry and you do not remember what
happened to you... You start to gain your vision back, but it feels weird.  
Although it is blurry, you don't seem to know where you are at.""")
    print("""You feel around, hopefully finding something that can 
help you out.  You feel something that feels like eyedrops. """)

    userinput = input('Do you take the eyedrops? ')
    if userinput:
        print('good for you ')

def main():
    entrance()


if __name__ == '__main__':
    main()
