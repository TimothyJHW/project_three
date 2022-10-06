"""
This is a Pythonic rendition of the battleships game
Tim Williams Project 3

"""


from string import ascii_lowercase
# from venv import create
import random



alphabet = []
ships=[]
## squares allocated for different board sizes
small = 8
medium = 9
large = 10
board_size = ""
grid = [[]]
number_of_ships = 0
shots_fired = ["a5","f6","c1"]
ship_locations = [["g1","g2","g3"],["a7","b7","c7"]]
ammo = 40


## Main Game Function

def main_game():
    create_alphabet()
    start_of_game()
    building_the_grid()
    deploy_the_fleet()

    while number_of_ships >0:
        user_guess()
        check_for_ships_hit()
        computer_guess()
pass


## Create Ship Objects
class CreateShip:
    ship_number = 1
    def __init__(self,type):
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
        self.position = position_ship(self.occupied_squares)
        self.ship_number = CreateShip.ship_number
        CreateShip.ship_number+=1




## Making the alphabet row headings

def create_alphabet():
    #simple function to create an alphabetical list for the grid
    global alphabet
    for iterator in ascii_lowercase:
        alphabet.append(iterator)
    return alphabet

def start_of_game():
     #establishes board size from user input
    global board_size, number_of_ships, alphabet, small, medium, large

    print("Welcome to Python Battleships")
    while (board_size != "s" and board_size !="m" and board_size != "l"):
        board_size = input("Would you like to play on a small, medium or large board? (s/m/l)")
        board_size = board_size.lower()
    if board_size == "s":
        board_size = small
        number_of_ships = 4
    elif board_size == "m":
        board_size = medium
        number_of_ships = 5
    else:
        board_size = large
        number_of_ships = 6
    alphabet = alphabet[0:board_size]
    return board_size, number_of_ships

## Establish the grid

def building_the_grid(board_size): 
    #builds the game grid from user input of board size
    global grid
    rows = []
    
    # for i in range (board_size):
    #     rows.insert(i)
    for x in range(1,board_size+1):
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

## print the grid to be refreshed after each turn so separate from establishing the grid.

def print_the_grid():
    for rows in range(board_size):
        print (grid[rows])


## The user's guess

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
    

## Creating ships

def deploy_the_fleet():
    #function to randomly distribute the fleets
    global ship_locations, ships, number_of_ships, small, medium,large
    if board_size == small:
        board_ships = ["Battleship","Cruiser","Destroyer"]
        for boat in range(len(board_ships)):
            new_boat = CreateShip(f"{board_ships[boat]}")
            ships.append(new_boat)
            print(ships[boat].type)
            print(ships[boat].position)
    elif board_size == medium:
        board_ships = ["Battleship","Cruiser","Destroyer","Destroyer"]
        for boat in range(len(board_ships)):
            new_boat = CreateShip(f"{board_ships[boat]}")
            ships.append(new_boat)
            print(ships[boat].type)
    else:
        board_ships = ["Battleship","Cruiser","Cruiser","Destroyer","Destroyer"]
        for boat in range(len(board_ships)):
            new_boat = CreateShip(f"{board_ships[boat]}")
            ships.append(new_boat)
            print(ships[boat].type)


## called from within the ship constructor function to establish the ships grid position

def position_ship(squares_occupied):
    new_ship_position = []
    ship_position_occupied = False
    while ship_position_occupied == False:
        rand_row = random.choice(alphabet)
        rand_col = random.randint(1,board_size-1)
        orientation = random.randint(0,1) # initial ship orientation. 0 is horizontal, 1 is vertical
        if orientation == 0 and rand_col+squares_occupied<board_size:
            for squares in range(squares_occupied):
                    new_ship_position.append(rand_row+str(rand_col+squares))          
            if check_ship_overlap(new_ship_position):
                ship_position_occupied = True
            else:
                new_ship_position.clear()
        elif orientation == 1 and alphabet.index(rand_row)+squares_occupied<board_size:
            for squares in range(squares_occupied):
                new_ship_position.append(alphabet[squares]+str(rand_col))
            if check_ship_overlap(new_ship_position):
                ship_position_occupied = True
            else:
                new_ship_position.clear()
    return new_ship_position



    return ship_position

## checks to see if one new ship overlaps with the previous ships' positions

def check_ship_overlap(check):
    global ships
    for x in ships:
        for y in check:
            if y in x.position:
                return False               
    return True


def check_for_ships_hit(shot):
    for x in ships:
        if shot in ships.position:
            print("HIT")
            

    pass



def computer_guess():
    initial_random_guess()
    exploration_shots()


def initial_random_guess():
    global shots_fired
    new_shot = False
    while new_shot==False:
        for i in shots_fired:
            col_guess = alphabet[random.randint(1,board_size-1)]
            row_guess = str(random.randint(1,board_size-1))
            guess = col_guess+row_guess
            if guess != i:
                print("already made that shot")
                new_shot = False
            else:
                new_shot = True
                print("new shot")
                print(guess)
                shots_fired.append(guess)
    return guess

    print (guess)
    for i in ship_locations:
        for index in i:
            if guess  == index:
                print("HIT", guess)
            else:
                print("miss")


            

    print(col_guess,row_guess)




## game sequence

create_alphabet()
board_size,number_of_ships = start_of_game()
building_the_grid(board_size)
print_the_grid()
deploy_the_fleet()
print([x.position for x in ships])
# user_guess()
# initial_random_guess()


## Check if a ship has been hit

def cycle_through_ships(shot):
        for i in range(len(ships)):
            for x in ships[i].position:
                if shot == x:
                    for iter in range(len(shots_fired)):
                        if shot == iter:
                            return("Already tried there")
                    return("Hit!")
                else:
                    return("Miss!")


## 















