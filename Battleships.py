"""
This is a Pythonic rendition of the battleships game

"""

from string import ascii_lowercase
from venv import create
import PySimpleGUI as sg
import random

class CreateShip:
    def __init__(self,type):
        self.type = type.lower()
        self.occupied_squares = 0
        if self.type == "battleship":
            self.occupied_squares = 4
        elif self.type == "cruiser":
            self.occupied_squares = 3
        elif self.type == "destroyer":
            self.occupied_squares = 2
        else:
            self.occupied_squares = 1
        self.orientation = random.randint(0,1) # initial ship orientation. 0 is horizontal, 1 is vertical

a = CreateShip("cruisEr")
print(a.occupied_squares,a.type,a.orientation,a)

def create_alphabet():
    a = []
    for iterator in ascii_lowercase:
        a.append(iterator)
    return a

alphabet = create_alphabet()

print(alphabet)





# def start_of_game(): #establishes board size from user input
#     board_size =""
#     while (board_size != "s" and board_size !="m" and board_size != "l"):
#         board_size = input("Would you like to play on a small, medium or large board? (s/m/l)")
#         board_size = board_size.lower()
#     if board_size == "s":
#         board_size = 10
#     elif board_size == "m":
#         board_size = 15
#     else:
#         board_size = 20
#     return board_size

def building_the_grid(board_size): #builds the game grid from user input of board size
    rows = []
    columns = []
    for iter in range(board_size):
        rows.append(0)

        columns.append(0)
    rows.append(columns)
    # return rows, columns
    return rows



# board_size = start_of_game()
# a = building_the_grid(board_size)
# # print(a,"\n",b)
# print(a[9],type(a[10]))

sg.theme('DarkGray')  
layout = [  [sg.Text('Choose the board size')],
            [sg.Text('Enter (s)mall, (m)edium or (l)arge'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Welcome to Battleships', layout)
# Event Loop to process "events"
while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    else:
        board_size = event
        while (board_size != "s" and board_size !="m" and board_size != "l"):
            board_size = board_size.lower()
        if board_size == "s":
            board_size = 10
        elif board_size == "m":
            board_size = 15
        else:
            board_size = 20


window.close()









