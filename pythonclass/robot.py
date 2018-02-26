# -----------------------------------------------------------------------------
# Name:       robot
# Purpose:    class definition for robots
#
# Author:     Randy Hoang
# Date:       2/24/2018
# -----------------------------------------------------------------------------

"""
Module to describe and control robot objects in a maze.
"""
import tkinter


class Robot(object):
    """
    This is the super class Robot

    Arguments:
    name(string): The robot's name
    color(string): The color of the robot
    row(int): This is the position of the robot in the x-axis
    column(int): This is the position of the robot in the y-axis
    battery(int):  This is the amount of steps the robot has remaining

    Attributes:
    name(string): The robot's name
    color(string): The color of the robot
    row(int): This is the position of the robot in the x-axis
    column(int): This is the position of the robot in the y-axis
    battery(int):  This is the amount of steps the robot has remaining
    """

    # class variable used by the show method
    unit_size = 60

    # Class variable describing the maze
    # False represents an obstacle, True represents open space
    maze = [[True, True, False, True, True, True, False, True, True, True],
            [True, True, False, True, True, True, False, True, True, True],
            [True, False, True, True, True, True, False, True, True, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, False, False, False, False, True, True, True, True, True],
            [True, True, False, True, True, True, True, True, False, True],
            [True, False, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True]]

    maze_size = len(maze)
    # class variable to represent a full charge
    # A robot with a fully charged battery can take up to 20 steps
    full = 20



    def __init__(self,  name, color, row=0, column=0):
        self.name = name
        self.color = color
        self.row = row
        self.column = column
        self.battery = self.full



    def __str__(self): # when printed: 'name' is a 'color' robot lost in a maze
        return self.name + ' is a ' + self.color + ' robot lost in a maze.'

    def __gt__(self, other): # This will compare two robots based on battery
        return self.battery > other.battery


    @property # This is used so recharge doesn't need parenthesis
    def recharge(self):
        """
        This method will recharge the robot's battery to self.full class var
        """
        self.battery = self.full
        return self

    def one_step_forward(self):
        """
        This method move the robot one step in the corresponding direction if
        possible,  and decrement the battery value by 1.  A move may not be
        possible if the robot is out of battery,  an obstacle is encountered or
        the boundary of the maze is reached.
        """
        if self.battery >= 1:
            self.row += 1
            self.battery -= 1
        #elif self.battery == 0:
         #   print('Battery is at zero, please recharge!')

        return self

    def one_step_back(self):
        """
        This method move the robot one step in the corresponding direction if
        possible,  and decrement the battery value by 1.  A move may not be
        possible if the robot is out of battery,  an obstacle is encountered or
        the boundary of the maze is reached.
        """
        if self.battery >= 1:
            self.row -= 1
            self.battery -= 1
        return self

    def one_step_right(self):
        """
        This method move the robot one step in the corresponding direction if
        possible,  and decrement the battery value by 1.  A move may not be
        possible if the robot is out of battery,  an obstacle is encountered or
        the boundary of the maze is reached.
        """
        if self.battery >= 1:
            self.column += 1
            self.battery -= 1
        return self

    def one_step_left(self):
        """
        This method move the robot one step in the corresponding direction if
        possible,  and decrement the battery value by 1.  A move may not be
        possible if the robot is out of battery,  an obstacle is encountered or
        the boundary of the maze is reached.
        """
        if self.battery >= 1:
            self.row -= 1
            self.battery -= 1
        return self

    def forward(self, steps):
        """
        These methods take a number of steps as an argument and move the robot
        that many steps in the specified direction,  as far as possible. These
        methods should call the corresponding one_step method repeatedly.
        """
        for movement in range(steps):
            self.one_step_forward()
        return self

    def backward(self, steps):
        """
        These methods take a number of steps as an argument and move the robot
        that many steps in the specified direction,  as far as possible. These
        methods should call the corresponding one_step method repeatedly.
        """
        for movement in range(steps):
            self.one_step_back()
        return self

    def right(self, steps):
        """
        These methods take a number of steps as an argument and move the robot
        that many steps in the specified direction,  as far as possible. These
        methods should call the corresponding one_step method repeatedly.
        """
        for movement in range(steps):
            self.one_step_right()
        return self

    def left(self, steps):
        """
        These methods take a number of steps as an argument and move the robot
        that many steps in the specified direction,  as far as possible. These
        methods should call the corresponding one_step method repeatedly.
        """
        for movement in range(steps):
            self.one_step_left()
        return self

    # The method below has been written for you
    # You can use it when testing your class

    def show(self):
        """
        Draw a graphical representation of the robot in the maze.

        The robot's position and color are shown.
        The color is assumed to be one of the colors recognized by tkinter
        (https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm)
        If the robot's battery is empty, the robot is shown in a
        horizontal position. Otherwise the robot is shown in an upright
        position.
        The obstacles in the maze are shown in red.

        Parameter: None
        Return: None
        """
        root = tkinter.Tk()
        root.title(self.name + ' in the Maze')
        canvas = tkinter.Canvas(root, background='light green',
                                width=self.unit_size * self.maze_size,
                                height=self.unit_size * self.maze_size)
        canvas.grid()

        # draw a representation of the robot in the maze
        if self.battery:
            upper_x = self.column * self.unit_size + self.unit_size / 4
            upper_y = self.row * self.unit_size
            lower_x = upper_x + self.unit_size / 2
            lower_y = upper_y + self.unit_size
            eye_x = lower_x - 3 * self.unit_size / 20
            eye_y = upper_y + self.unit_size / 10

        else: # the robot ran out of battery
            upper_x = self.column * self.unit_size
            upper_y = self.row * self.unit_size + self.unit_size / 2
            lower_x = upper_x + self.unit_size
            lower_y = upper_y + self.unit_size / 2
            eye_x = lower_x - 9 * self.unit_size / 10
            eye_y = lower_y - 3 * self.unit_size / 20

        rectangle = canvas.create_rectangle(upper_x,
                                            upper_y,
                                            lower_x,
                                            lower_y,
                                            fill=self.color)
        # draw the robot's eyes
        canvas.create_oval(upper_x + self.unit_size / 10,
                           upper_y + self.unit_size / 10,
                           upper_x + 3 * self.unit_size / 20,
                           upper_y + 3 * self.unit_size / 20,
                           fill='black')
        canvas.create_oval(eye_x,
                           eye_y,
                           eye_x + self.unit_size / 20,
                           eye_y + self.unit_size / 20,
                           fill='black')
        # draw the obstacles in the maze
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                if not self.maze[row][col]:
                    canvas.create_rectangle(col * self.unit_size,
                                            row * self.unit_size,
                                            (col + 1) * self.unit_size,
                                            (row + 1) * self.unit_size,
                                            fill='red')
        for row in range(self.maze_size):
            canvas.create_line(0,
                               row * self.unit_size,
                               self.maze_size * self.unit_size,
                               row * self.unit_size)
        for col in range(self.maze_size):
            canvas.create_line(col * self.unit_size,
                               0,
                               col * self.unit_size,
                               self.maze_size * self.unit_size)
        root.mainloop()


# Enter you UnderwaterRobot Class definition below
