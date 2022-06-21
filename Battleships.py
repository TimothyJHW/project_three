"""
This is a Pythonic rendition of the battleships game
Tim Williams Project 3

"""


from string import ascii_lowercase
from venv import create
import PySimpleGUI as sg
import random

from attr import s


alphabet = []
board_size = ""
grid = [[]]
number_of_ships = 0
shots_fired = 40
ship_locations =[]

def main_game():
    create_alphabet()
    start_of_game()
    building_the_grid()
    deploy_the_fleets()

    while number_of_ships >0:
        user_guess()
        check_for_ships_hit()
        computer_selection()
pass

class CreateShip:
    def __init__(self,type):
        self.ship_number = 1
        self.type = type.lower()
        self.occupied_squares = 0
        self.position = []
        self.destroyed = False
        if self.type == "battleship":
            self.occupied_squares = 3
        elif self.type == "cruiser":
            self.occupied_squares = 2
        elif self.type == "destroyer":
            self.occupied_squares = 1
        else:
            self.occupied_squares = 1
        self.orientation = random.randint(0,1) # initial ship orientation. 0 is horizontal, 1 is vertical
        self.ship_number += 1

a = CreateShip("cruisEr")
print(a.occupied_squares,a.type,a.orientation,a)

def create_alphabet():
    #simple function to create an alphabetical list for the grid
    global alphabet
    for iterator in ascii_lowercase:
        alphabet.append(iterator)
    return alphabet

def start_of_game():
     #establishes board size from user input
    global board_size
    global number_of_ships
    global alphabet
    print("Welcome to Python Battleships")
    while (board_size != "s" and board_size !="m" and board_size != "l"):
        board_size = input("Would you like to play on a small, medium or large board? (s/m/l)")
        board_size = board_size.lower()
    if board_size == "s":
        board_size = 8
        number_of_ships = 4
    elif board_size == "m":
        board_size = 9
        number_of_ships = 5
    else:
        board_size = 10
        number_of_ships = 6
    alphabet = alphabet[0:board_size]
    return board_size

def building_the_grid(board_size): 
    #builds the game grid from user input of board size
    global grid
    rows = []
    
    # for i in range (board_size):
    #     rows.insert(i)
    for iter in range(1,board_size+1):
        columns = []
        # rows.append(iter)
        for second_iter in range(1,board_size+1):
            columns.append("0")
        rows.append(columns)
    grid = rows
    #set up keys in grid
    for i in range(1,board_size):
        grid[0][i] = str(i)
        grid[i][0] = alphabet[i-1]
    grid[0][0]=" "

def print_the_grid():
    for rows in range(board_size):
        print (grid[rows])

def user_guess():
    #user firing solution error capture based on the addressable elements in the string
    accept=False
    while accept == False:
        fire_guess = input("Choose your next shot by inputting grid ref")
        if fire_guess[0].isalpha() and fire_guess[0].lower() in alphabet and len(fire_guess) == 2: #is the 1st char of the input within range and a letter
            if fire_guess[1:].isnumeric() and int(fire_guess[1:])>=0 and int(fire_guess[1:])<= board_size: # is the 2nd char of input within range and a number
                accept = True
            else:print("Please enter valid refs")
    #search the grid to see if there has been a hit first split user response up into column and row
    col = int(alphabet.index(fire_guess[:1]))
    row = int(fire_guess[1:])
    if grid[col][row] == "0":
        print("You missed")
        grid[col][row]="#"
        print_the_grid()
    elif grid[col][row] == "1":
        print ("A hit, a palpable hit!")
        grid[col][row] ="x"
    elif grid[col][row] == "#" or grid[col][row] == "x":
        print("You have already fired at that spot")
    


def deploy_the_fleets():
    #funtion to randomly distribute the fleets
    global ship_locations
    ship_lengths = [4,3,2,2] # the number of lengths of different types of ship
    for ships in ship_lengths:
        ship_position_occupied = False
        while ship_position_occupied ==False:
            rand_row = random.choice(alphabet)
            rand_col = random.randint(1,board_size+1)
            orientation = random.randint(0,1) # initial ship orientation. 0 is horizontal, 1 is vertical
            for positions in range(ships):
                if orientation == 0:
                    ship_locations.append(rand_row+str(rand_col+positions))
                elif orientation == 1:
                    temp = alphabet[positions]
                    # print(temp)
                    # # ship_locations.append(alphabet[alphabet.index(rand_row)+positions]+str(rand_col))



def check_for_ships_hit():
    pass

create_alphabet()
board_size = start_of_game()
building_the_grid(board_size)
print_the_grid()
# deploy_the_fleets()
print()
user_guess()



# main_game()s




# sg.theme('DarkGray')




# layout = [  [sg.Text('Choose the board size')],
#             [sg.Text('Enter (s)mall, (m)edium or (l)arge'), sg.InputText()],
#             [sg.OK(), sg.Cancel()]]

# # Create the Window
# window = sg.Window('Welcome to Battleships', layout)
# # Event Loop to process "events"
# while True:             
#     event, values = window.read()
#     if event in (sg.WIN_CLOSED, 'Cancel'):
#         break
#     else:
#         board_size = event
#         while (board_size != "s" and board_size !="m" and board_size != "l"):
#             board_size = board_size.lower()
#         if board_size == "s":
#             board_size = 10
#         elif board_size == "m":
#             board_size = 15
#         else:
#             board_size = 20


# window.close()
















