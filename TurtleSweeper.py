import turtle
import random
import math

settings_list = ["new", "shown", "on", "on"]

print("TurtleSweeper - v.1.3")
print("Welcome to TurtleSweeper!")
First_Intro_Done = False

Has_Player_WonG = 0
Game_Over = False
Played_Once = False
turtle_drawing = False
show_win_message = True

def Play():
    global Has_Player_WonG
    global Game_Over
    print("---------------------------------------------------------------------")

    def Check_If_Valid_Input3(Input):
        Valid_Input = 0
        if Input == "easy":
            Valid_Input = 1
        elif Input == "medium":
            Valid_Input = 2
        elif Input == "hard":
            Valid_Input = 3
        return Valid_Input

    # Grid Parameters (to change difficulty)
    Difficulty_Choose = False
    while Difficulty_Choose == False:
        Difficulty_Input = input("Please choose a difficulty - easy, medium, or hard: ")
        if Check_If_Valid_Input3(Difficulty_Input) == 1:
            Grid_Width = 10
            Grid_Height = 8
            Difficulty_Choose = True
        elif Check_If_Valid_Input3(Difficulty_Input) == 2:
            Grid_Width = 18
            Grid_Height = 14
            Difficulty_Choose = True
        elif Check_If_Valid_Input3(Difficulty_Input) == 3:
            Grid_Width = 24
            Grid_Height = 20
            Difficulty_Choose = True
        else:
            print('type "easy", "medium", or "hard" to set difficulty')

    turtle.TurtleScreen._RUNNING = True

    # The turtle that does all the work
    wee = turtle.Turtle()
    wee.shape("turtle")
    wee.speed(100)
    wee.hideturtle()

    # List of colors for different numbers of tiles
    if settings_list[0] == "old":
        colors_list = [
            "antique white",
            "blue",
            "green",
            "maroon",
            "purple",
            "yellow",
            "cyan",
            "gray",
            "light steel blue",
            "black",
            "red",
            "white"
        ]
    elif settings_list[0] == "new":
        colors_list = [
            "antique white",
            "blue",
            "green",
            "maroon",
            "purple",
            "gold",
            "turquoise",
            "deep pink",
            "chartreuse",
            "black",
            "red",
            "white"
        ]
    elif settings_list[0] == "rainbow":
        colors_list = [
            "#C0C0C0",
            "#FF0000",
            "#FF8000",
            "#FFFF00",
            "#80F000",
            "#00FF00",
            "#00FF80",
            "#00FFFF",
            "#0080FF",
            "black",
            "#800000",
            "white"
        ]
    elif settings_list[0] == "microsoft":
        colors_list = [
            "#C0C0C0",
            "blue",
            "green",
            "#FF0000",
            "purple",
            "maroon",
            "turquoise",
            "#000000",
            "gray",
            "black",
            "red",
            "white"
        ]

    # List of bombs and numbers (for non-bomb tiles)
    Box_List = []
    # List of bombs and dug/undug tiles
    Dig_List = []
    # List of dug/undug tiles and flagged/unflagged areas
    Flag_List = []

    # Temporary list for storing large areas of zero tiles
    Temp_Zero_List = []

    if settings_list[1] == "shown":
        wee.showturtle()
    elif settings_list[1] == "hidden": pass

    Max_Squares = Grid_Width * (Grid_Height - 1) + Grid_Width

    # Variables for ending the game
    Difficulty_Choose = False

    # Percentage of the Map that will hold a bomb
    Bomb_Probability = 0.21

    # Maps turtle to the right location when drawing squares
    def Map_Wee(x_coord, y_coord):
        wee_xloc = ((x_coord - 1) * Square_SizeG) - ((Square_SizeG * Grid_Width) / 2)
        wee_yloc = ((y_coord - 1) * Square_SizeG) - ((Square_SizeG * Grid_Height) / 2)

        coord_list = [wee_xloc, wee_yloc]

        return coord_list

    # Creates and scales grid based on parameters
    def Create_Grid():
        def draw_y(val, number, grid):
            wee.forward(Square_Size * Grid_Height)

            wee.penup()
            if int(number) <= Grid_Width and grid != (Grid_Width + 1):
                wee.setpos(
                    val - (Square_Size * 7/16), Square_Size * (Grid_Height / 2) - (1.068 * Square_Size * Grid_Height)
                )
                wee.pendown()
                wee.write(number, align="center", font=("Comic Sans MS", int(Square_Size / 4), "normal"))
                wee.penup()
                wee.setpos(val, Square_Size * (Grid_Height / 2))
                wee.pendown()

        def draw_x(val, number, grid):
            wee.forward(Square_Size * Grid_Width)

            wee.penup()
            if int(number) <= Grid_Height and grid != (Grid_Height + 1):
                wee.setpos(
                    -(Square_Size * (Grid_Width / 2)) * 1.071, val - (Square_Size * 3/4)
                )
                wee.pendown()
                wee.write(number, align="center", font=("Comic Sans MS", int(Square_Size / 4), "normal"))
                wee.penup()
                wee.setpos(-(Square_Size * (Grid_Width / 2)), val)
                wee.pendown()

        if (576 / Grid_Width) > (480 / Grid_Height):
            Square_Size = 480 / Grid_Height
            wee.turtlesize(stretch_wid= Square_Size / 50, stretch_len= Square_Size / 50, outline= Square_Size / 50)
            wee.right(90)
            wee.penup()
            wee.goto(-((Square_Size * Grid_Width) / 2), 240)
            wee.pendown()

            input_valy = -((Square_Size * Grid_Width) / 2) + Square_Size
            input_numbery = "1"
            num_lines_y = 0
            while input_valy <= ((Square_Size * Grid_Width) / 2) + Square_Size + 1:
                draw_y(input_valy, input_numbery, num_lines_y)
                input_valy = input_valy + Square_Size
                input_numbery = str(int(input_numbery) + 1)
                num_lines_y = num_lines_y + 1

            wee.left(90)
            wee.penup()
            wee.goto(-((Square_Size * Grid_Width) / 2), -240)
            wee.pendown()

            input_valx = -((Square_Size * Grid_Height) / 2) + Square_Size
            input_numberx = "1"
            num_lines_x = 0
            while input_valx <= ((Square_Size * Grid_Height) / 2) + Square_Size + 1:
                draw_x(input_valx, input_numberx, num_lines_x)
                input_valx = input_valx + Square_Size
                input_numberx = str(int(input_numberx) + 1)
                num_lines_x = num_lines_x + 1

        if (576 / Grid_Width) <= (480 / Grid_Height):
            Square_Size = 576 / Grid_Width
            wee.turtlesize(stretch_wid= Square_Size / 50, stretch_len= Square_Size / 50, outline= Square_Size / 50)
            wee.right(90)
            wee.penup()
            wee.goto(-288, ((Square_Size * Grid_Height) / 2))
            wee.pendown()

            input_valy = -((Square_Size * Grid_Width) / 2) + Square_Size
            input_numbery = "1"
            num_lines_y = 0
            while input_valy <= ((Square_Size * Grid_Width) / 2) + Square_Size + 1:
                draw_y(input_valy, input_numbery, num_lines_y)
                input_valy = input_valy + Square_Size
                input_numbery = str(int(input_numbery) + 1)
                num_lines_y = num_lines_y + 1

            wee.left(90)
            wee.penup()
            wee.goto(-288, -((Square_Size * Grid_Height) / 2))
            wee.pendown()

            input_valx = -((Square_Size * Grid_Height) / 2) + Square_Size
            input_numberx = "1"
            num_lines_x = 0
            while input_valx <= ((Square_Size * Grid_Height) / 2) + Square_Size + 1:
                draw_x(input_valx, input_numberx, num_lines_x)
                input_valx = input_valx + Square_Size
                input_numberx = str(int(input_numberx) + 1)
                num_lines_x = num_lines_x + 1
        return Square_Size

    Square_SizeG = Create_Grid()

    # Plants Bombs to Box_List
    def Create_Game():
        num_Box_List = 0
        while num_Box_List < Max_Squares:
            NextAppend = random.random()
            if NextAppend > Bomb_Probability:
                TheAppend = 0
            if NextAppend <= Bomb_Probability:
                TheAppend = "bomb"
            Box_List.append(TheAppend)
            num_Box_List = num_Box_List + 1

    Create_Game()

    # Takes coordinates and converts it to the ID (Index) in Box/Dug List
    def Convert_to_Square_ID(x_coord, y_coord):
        if 0 < x_coord <= Grid_Width and 0 < y_coord <= Grid_Height:
            Square_ID = Grid_Width * (y_coord - 1) + x_coord - 1
            return Square_ID
        else:
            return "null"

    # Takes Square ID in Box/Dug List and converts it to X and Y coordinates
    def Convert_to_Coordinates(Square_ID):
        Coords_List = []
        X = (Square_ID) % Grid_Width + 1
        Coords_List.append(X)
        Y = math.ceil((((Square_ID) - X) / Grid_Width) + 1)
        Coords_List.append(Y)

        return Coords_List

    # Checks Neighboring tiles for bombs (used in Create_Game2)
    def Check_Neighboring_Squares(x, y):
        num_Surrounding_Bomb = 0
        if Convert_to_Square_ID(x - 1, y) != "null":
            if Box_List[Convert_to_Square_ID(x - 1, y)] == "bomb":
                num_Surrounding_Bomb = num_Surrounding_Bomb + 1
        if Convert_to_Square_ID(x - 1, y - 1) != "null":
            if Box_List[Convert_to_Square_ID(x - 1, y - 1)] == "bomb":
                num_Surrounding_Bomb = num_Surrounding_Bomb + 1
        if Convert_to_Square_ID(x, y - 1) != "null":
            if Box_List[Convert_to_Square_ID(x, y - 1)] == "bomb":
                num_Surrounding_Bomb = num_Surrounding_Bomb + 1
        if Convert_to_Square_ID(x + 1, y - 1) != "null":
            if Box_List[Convert_to_Square_ID(x + 1, y - 1)] == "bomb":
                num_Surrounding_Bomb = num_Surrounding_Bomb + 1
        if Convert_to_Square_ID(x + 1, y) != "null":
            if Box_List[Convert_to_Square_ID(x + 1, y)] == "bomb":
                num_Surrounding_Bomb = num_Surrounding_Bomb + 1
        if Convert_to_Square_ID(x + 1, y + 1) != "null":
            if Box_List[Convert_to_Square_ID(x + 1, y + 1)] == "bomb":
                num_Surrounding_Bomb = num_Surrounding_Bomb + 1
        if Convert_to_Square_ID(x, y + 1) != "null":
            if Box_List[Convert_to_Square_ID(x, y + 1)] == "bomb":
                num_Surrounding_Bomb = num_Surrounding_Bomb + 1
        if Convert_to_Square_ID(x - 1, y + 1) != "null":
            if Box_List[Convert_to_Square_ID(x - 1, y + 1)] == "bomb":
                num_Surrounding_Bomb = num_Surrounding_Bomb + 1
        return num_Surrounding_Bomb

    def Check_Neighboring_Squares2(x,y):
        add_to_Player1 = 0
        numList = 0
        if Convert_to_Square_ID(x-1,y) != "null":
            if Dig_List[Convert_to_Square_ID(x-1,y)] == 0:
                if Box_List[Convert_to_Square_ID(x-1,y)] > 0:
                    Dig_List[Convert_to_Square_ID(x-1,y)] = "dug"
                    Flag_List[Convert_to_Square_ID(x-1,y)] = "dug"
                    wee_cords = Map_Wee(x-1,y)
                    wee.penup()
                    wee.goto(wee_cords[0],wee_cords[1])
                    wee.pendown()
                    odd_Or_even2 = ((x-1) + y) % 2
                    Fill_Square(colors_list[Box_List[Convert_to_Square_ID(x-1,y)]], odd_Or_even2, x-1, y)
                    add_to_Player1 = add_to_Player1 + 1
                if Box_List[Convert_to_Square_ID(x-1,y)] == 0:
                    if Temp_Zero_List.count(Convert_to_Square_ID(x-1,y)) == 0:
                        Temp_Zero_List.append(Convert_to_Square_ID(x-1,y))
                        numList = numList + 1
        if Convert_to_Square_ID(x-1,y-1) != "null":
            if Dig_List[Convert_to_Square_ID(x-1,y-1)] == 0:
                if Box_List[Convert_to_Square_ID(x-1,y-1)] > 0:
                    Dig_List[Convert_to_Square_ID(x-1,y-1)] = "dug"
                    Flag_List[Convert_to_Square_ID(x-1,y-1)] = "dug"
                    wee_cords = Map_Wee(x-1,y-1)
                    wee.penup()
                    wee.goto(wee_cords[0],wee_cords[1])
                    wee.pendown()
                    odd_Or_even2 = ((x-1) + (y-1)) % 2
                    Fill_Square(colors_list[Box_List[Convert_to_Square_ID(x-1,y-1)]], odd_Or_even2, x-1, y-1)
                    add_to_Player1 = add_to_Player1 + 1
                if Box_List[Convert_to_Square_ID(x-1,y-1)] == 0:
                    if Temp_Zero_List.count(Convert_to_Square_ID(x-1,y-1)) == 0:
                        Temp_Zero_List.append(Convert_to_Square_ID(x-1,y-1))
                        numList = numList + 1
        if Convert_to_Square_ID(x,y-1) != "null":
            if Dig_List[Convert_to_Square_ID(x,y-1)] == 0:
                if Box_List[Convert_to_Square_ID(x,y-1)] > 0:
                    Dig_List[Convert_to_Square_ID(x,y-1)] = "dug"
                    Flag_List[Convert_to_Square_ID(x,y-1)] = "dug"
                    wee_cords = Map_Wee(x,y-1)
                    wee.penup()
                    wee.goto(wee_cords[0],wee_cords[1])
                    wee.pendown()
                    odd_Or_even2 = (x + (y-1)) % 2
                    Fill_Square(colors_list[Box_List[Convert_to_Square_ID(x,y-1)]], odd_Or_even2, x, y-1)
                    add_to_Player1 = add_to_Player1 + 1
                if Box_List[Convert_to_Square_ID(x,y-1)] == 0:
                    if Temp_Zero_List.count(Convert_to_Square_ID(x,y-1)) == 0:
                        Temp_Zero_List.append(Convert_to_Square_ID(x,y-1))
                        numList = numList + 1
        if Convert_to_Square_ID(x+1,y-1) != "null":
            if Dig_List[Convert_to_Square_ID(x+1,y-1)] == 0:
                if Box_List[Convert_to_Square_ID(x+1,y-1)] > 0:
                    Dig_List[Convert_to_Square_ID(x+1,y-1)] = "dug"
                    Flag_List[Convert_to_Square_ID(x+1,y-1)] = "dug"
                    wee_cords = Map_Wee(x+1,y-1)
                    wee.penup()
                    wee.goto(wee_cords[0],wee_cords[1])
                    wee.pendown()
                    odd_Or_even2 = ((x+1) + (y-1)) % 2
                    Fill_Square(colors_list[Box_List[Convert_to_Square_ID(x+1,y-1)]], odd_Or_even2, x+1, y-1)
                    add_to_Player1 = add_to_Player1 + 1
                if Box_List[Convert_to_Square_ID(x+1,y-1)] == 0:
                    if Temp_Zero_List.count(Convert_to_Square_ID(x+1,y-1)) == 0:
                        Temp_Zero_List.append(Convert_to_Square_ID(x+1,y-1))
                        numList = numList + 1
        if Convert_to_Square_ID(x+1,y) != "null":
            if Dig_List[Convert_to_Square_ID(x+1,y)] == 0:
                if Box_List[Convert_to_Square_ID(x+1,y)] > 0:
                    Dig_List[Convert_to_Square_ID(x+1,y)] = "dug"
                    Flag_List[Convert_to_Square_ID(x+1,y)] = "dug"
                    wee_cords = Map_Wee(x+1,y)
                    wee.penup()
                    wee.goto(wee_cords[0],wee_cords[1])
                    wee.pendown()
                    odd_Or_even2 = ((x+1) + y) % 2
                    Fill_Square(colors_list[Box_List[Convert_to_Square_ID(x+1,y)]], odd_Or_even2, x+1, y)
                    add_to_Player1 = add_to_Player1 + 1
                if Box_List[Convert_to_Square_ID(x+1,y)] == 0:
                    if Temp_Zero_List.count(Convert_to_Square_ID(x+1,y)) == 0:
                        Temp_Zero_List.append(Convert_to_Square_ID(x+1,y))
                        numList = numList + 1
        if Convert_to_Square_ID(x+1,y+1) != "null":
            if Dig_List[Convert_to_Square_ID(x+1,y+1)] == 0:
                if Box_List[Convert_to_Square_ID(x+1,y+1)] > 0:
                    Dig_List[Convert_to_Square_ID(x+1,y+1)] = "dug"
                    Flag_List[Convert_to_Square_ID(x+1,y+1)] = "dug"
                    wee_cords = Map_Wee(x+1,y+1)
                    wee.penup()
                    wee.goto(wee_cords[0],wee_cords[1])
                    wee.pendown()
                    odd_Or_even2 = ((x+1) + (y+1)) % 2
                    Fill_Square(colors_list[Box_List[Convert_to_Square_ID(x+1,y+1)]], odd_Or_even2, x+1, y+1)
                    add_to_Player1 = add_to_Player1 + 1
                if Box_List[Convert_to_Square_ID(x+1,y+1)] == 0:
                    if Temp_Zero_List.count(Convert_to_Square_ID(x+1,y+1)) == 0:
                        Temp_Zero_List.append(Convert_to_Square_ID(x+1,y+1))
                        numList = numList + 1
        if Convert_to_Square_ID(x,y+1) != "null":
            if Dig_List[Convert_to_Square_ID(x,y+1)] == 0:
                if Box_List[Convert_to_Square_ID(x,y+1)] > 0:
                    Dig_List[Convert_to_Square_ID(x,y+1)] = "dug"
                    Flag_List[Convert_to_Square_ID(x,y+1)] = "dug"
                    wee_cords = Map_Wee(x,y+1)
                    wee.penup()
                    wee.goto(wee_cords[0],wee_cords[1])
                    wee.pendown()
                    odd_Or_even2 = (x + (y+1)) % 2
                    Fill_Square(colors_list[Box_List[Convert_to_Square_ID(x,y+1)]], odd_Or_even2, x, y+1)
                    add_to_Player1 = add_to_Player1 + 1
                if Box_List[Convert_to_Square_ID(x,y+1)] == 0:
                    if Temp_Zero_List.count(Convert_to_Square_ID(x,y+1)) == 0:
                        Temp_Zero_List.append(Convert_to_Square_ID(x,y+1))
                        numList = numList + 1
        if Convert_to_Square_ID(x-1,y+1) != "null":
            if Dig_List[Convert_to_Square_ID(x-1,y+1)] == 0:
                if Box_List[Convert_to_Square_ID(x-1,y+1)] > 0:
                    Dig_List[Convert_to_Square_ID(x-1,y+1)] = "dug"
                    Flag_List[Convert_to_Square_ID(x-1,y+1)] = "dug"
                    wee_cords = Map_Wee(x-1,y+1)
                    wee.penup()
                    wee.goto(wee_cords[0],wee_cords[1])
                    wee.pendown()
                    odd_Or_even2 = ((x-1) + (y+1)) % 2
                    Fill_Square(colors_list[Box_List[Convert_to_Square_ID(x-1,y+1)]], odd_Or_even2, x-1, y+1)
                    add_to_Player1 = add_to_Player1 + 1
                if Box_List[Convert_to_Square_ID(x-1,y+1)] == 0:
                    if Temp_Zero_List.count(Convert_to_Square_ID(x-1,y+1)) == 0:
                        Temp_Zero_List.append(Convert_to_Square_ID(x-1,y+1))
                        numList = numList + 1
        return add_to_Player1

    # Assigns numbers to surrounding tiles in Box_List
    def Create_Game2():
        x_to_check = 0
        y_to_check = 1
        while x_to_check * y_to_check < Max_Squares:
            if x_to_check >= Grid_Width:
                x_to_check = 1
                y_to_check = y_to_check + 1
            else:
                x_to_check = x_to_check + 1
            if Box_List[Convert_to_Square_ID(x_to_check, y_to_check)] != "bomb":
                Surrounding_Bomb = Check_Neighboring_Squares(x_to_check, y_to_check)
                Box_List[Convert_to_Square_ID(x_to_check, y_to_check)] = Surrounding_Bomb

    Create_Game2()

    # Parses bombs from Box_List to Dig_List
    def Create_Game3():
        id_to_check = 0
        while id_to_check < len(Box_List):
            if Box_List[id_to_check] != "bomb":
                Dig_List.append(0)
            elif Box_List[id_to_check] == "bomb":
                Dig_List.append("bomb")
            id_to_check = id_to_check + 1

    Create_Game3()

    # Parses Dig_List to figure out how many spaces to clean to win, as well as total bombs
    def Create_Game4():
        Win_Variable = 0
        id_to_chek = 0
        while id_to_chek < len(Dig_List):
            if Dig_List[id_to_chek] != "bomb":
                Win_Variable = Win_Variable + 1
            id_to_chek = id_to_chek + 1
        return Win_Variable

    Win_VariableG = Create_Game4()
    Total_Bombs = (Grid_Width * Grid_Height) - Win_VariableG

    # Creates the Flag_List
    def Create_Game5():
        id_to_chec = 0
        while id_to_chec < len(Box_List):
            Flag_List.append(0)
            id_to_chec = id_to_chec + 1

    Create_Game5()

    # Main input check for main loop
    def Check_If_Valid_Input(Input):
        Valid_Input = 0
        Valid_Input_Change = 1
        if (Input[0]).isalpha() == True:
            if Input[0] == "f" or Input[0] == "u":
                if len(Input) > 1:
                    if Input[1] == ":" and len(Input) > 2 and Input[2] != ":":
                        Input_List1 = Input.split(":")
                        if ((Input_List1[1])[0]).isnumeric() == True:
                            if ((Input_List1[1])[len(Input_List1[1]) - 1]).isnumeric() == True:
                                if len(Input_List1[1]) <= len(str(Grid_Width)) + len(str(Grid_Height)) + 1:
                                    index_to_check = 0
                                    comma = 0
                                    while index_to_check < len(Input_List1[1]):
                                        if ((Input_List1[1])[index_to_check]) == ",":
                                            comma = comma + 1
                                        if ((Input_List1[1])[index_to_check]).isnumeric() == False and ((Input_List1[1])[index_to_check]) != ",":
                                            Valid_Input_Change = 0
                                            index_to_check = len(Input_List1[1])
                                        index_to_check = index_to_check + 1
                                    if comma == 1 and Valid_Input_Change != 0:
                                        Valid_Input = 1
                                elif len(Input_List1[1]) > len(str(Grid_Width)) + len(str(Grid_Height)) + 1:
                                    Valid_Input = 3
            elif Input == "end":
                Valid_Input = 4
            elif Input == "quit":
                Valid_Input = 4
        if (Input[0]).isnumeric() == True:
            if (Input[len(Input) - 1]).isnumeric() == True:
                index_to_check = 0
                comma = 0
                while index_to_check < len(Input):
                    if (Input[index_to_check]) == ",":
                        comma = comma + 1
                    if (Input[index_to_check]).isnumeric() == False and (Input[index_to_check]) != ",":
                        Valid_Input_Change = 0
                        index_to_check = len(Input)
                    index_to_check = index_to_check + 1
                if comma == 1 and Valid_Input_Change != 0:
                    Valid_Input = 2
        return Valid_Input

    # Input check for digging a flagged area conformation
    def Check_If_Valid_Input2(Input):
        Valid_Input = 0
        if Input == "yes":
            Valid_Input = 1
        elif Input == "no":
            Valid_Input = 2
        else:
            Valid_Input = 0
        return Valid_Input

    # Fills squares with correspondent colors based on surrounding bombs
    def Fill_Square(color, value, x, y):
        if 0 < colors_list.index(color) < 9:
            if settings_list[0] == "new" or settings_list[0] == "old":
                if value == 1:
                    wee.fillcolor("#d7b889")
                if value == 0:
                    wee.fillcolor("#e5c29f")
            elif settings_list[0] == "rainbow":
                wee.fillcolor("black")
            elif settings_list[0] == "microsoft":
                wee.fillcolor(colors_list[0])
            wee.begin_fill()
            if settings_list[0] == "rainbow":
                wee.pencolor("white")
            if settings_list[2] == "on":
                if Convert_to_Square_ID(x, y - 1) != "null":
                    if Dig_List[Convert_to_Square_ID(x, y - 1)] == "dug":
                        if settings_list[0] == "new" or settings_list[0] == "old":
                            if value == 1:
                                wee.pencolor("#e5c29f")
                            elif value == 0:
                                wee.pencolor("#d7b889")
                        elif settings_list[0] == "microsoft":
                            wee.pencolor(colors_list[0])
                        elif settings_list[0] == "rainbow":
                            wee.pencolor("black")
            wee.forward(Square_SizeG)
            wee.pencolor("black")
            if settings_list[0] == "rainbow":
                wee.pencolor("white")
            wee.left(90)
            if settings_list[2] == "on":
                if Convert_to_Square_ID(x + 1, y) != "null":
                    if Dig_List[Convert_to_Square_ID(x + 1, y)] == "dug":
                        if settings_list[0] == "new" or settings_list[0] == "old":
                            if value == 1:
                                wee.pencolor("#d7b889")
                            elif value == 0:
                                wee.pencolor("#e5c29f")
                        elif settings_list[0] == "microsoft":
                            wee.pencolor(colors_list[0])
                        elif settings_list[0] == "rainbow":
                            wee.pencolor("black")
            wee.forward(Square_SizeG)
            wee.pencolor("black")
            if settings_list[0] == "rainbow":
                wee.pencolor("white")
            wee.left(90)
            if settings_list[2] == "on":
                if Convert_to_Square_ID(x, y + 1) != "null":
                    if Dig_List[Convert_to_Square_ID(x, y + 1)] == "dug":
                        if settings_list[0] == "new" or settings_list[0] == "old":
                            if value == 1:
                                wee.pencolor("#d7b889")
                            elif value == 0:
                                wee.pencolor("#e5c29f")
                        elif settings_list[0] == "microsoft":
                            wee.pencolor(colors_list[0])
                        elif settings_list[0] == "rainbow":
                            wee.pencolor("black")
            wee.forward(Square_SizeG)
            wee.pencolor("black")
            if settings_list[0] == "rainbow":
                wee.pencolor("white")
            wee.left(90)
            if settings_list[2] == "on":
                if Convert_to_Square_ID(x - 1, y) != "null":
                    if Dig_List[Convert_to_Square_ID(x - 1, y)] == "dug":
                        if settings_list[0] == "new" or settings_list[0] == "old":
                            if value == 1:
                                wee.pencolor("#e5c29f")
                            elif value == 0:
                                wee.pencolor("#d7b889")
                        elif settings_list[0] == "microsoft":
                            wee.pencolor(colors_list[0])
                        elif settings_list[0] == "rainbow":
                            wee.pencolor("black")
            wee.forward(Square_SizeG)
            wee.pencolor("black")
            if settings_list[0] == "rainbow":
                wee.pencolor("white")
            wee.left(90)
            wee.end_fill()
            wee.penup()
            wee.forward(Square_SizeG / 2)
            wee.left(90)
            wee.forward(Square_SizeG / 10)
            wee.pencolor(color)
            if Grid_Width > 10 or Grid_Height > 8:
                wee.write(str(colors_list.index(color)), align = "center", font = ("Sans Serif", int(Square_SizeG / 2), "bold"))
            else:
                wee.write(str(colors_list.index(color)), align = "center", font = ("Sans Serif", int(Square_SizeG / 2), "normal"))
            wee.pencolor("black")
            wee.backward(Square_SizeG / 10)
            if settings_list[0] == "rainbow":
                wee.pencolor("white")
            wee.right(90)
            wee.backward(Square_SizeG / 2)
            wee.pencolor("black")
        elif colors_list.index(color) == 0:
            if settings_list[0] == "new" or settings_list[0] == "old":
                if value == 1:
                    wee.fillcolor("#d7b889")
                if value == 0:
                    wee.fillcolor("#e5c29f")
            elif settings_list[0] == "rainbow":
                wee.fillcolor("black")
            elif settings_list[0] == "microsoft":
                wee.fillcolor(colors_list[0])
            wee.begin_fill()
            if settings_list[0] == "rainbow":
                wee.pencolor("white")
            if settings_list[2] == "on":
                if Convert_to_Square_ID(x, y - 1) != "null":
                    if Dig_List[Convert_to_Square_ID(x, y - 1)] == "dug":
                        if settings_list[0] == "new" or settings_list[0] == "old":
                            if value == 1:
                                wee.pencolor("#e5c29f")
                            elif value == 0:
                                wee.pencolor("#d7b889")
                        elif settings_list[0] == "microsoft":
                            wee.pencolor(colors_list[0])
                        elif settings_list[0] == "rainbow":
                            wee.pencolor("black")
            wee.forward(Square_SizeG)
            wee.pencolor("black")
            if settings_list[0] == "rainbow":
                wee.pencolor("white")
            wee.left(90)
            if settings_list[2] == "on":
                if Convert_to_Square_ID(x + 1, y) != "null":
                    if Dig_List[Convert_to_Square_ID(x + 1, y)] == "dug":
                        if settings_list[0] == "new" or settings_list[0] == "old":
                            if value == 1:
                                wee.pencolor("#d7b889")
                            elif value == 0:
                                wee.pencolor("#e5c29f")
                        elif settings_list[0] == "microsoft":
                            wee.pencolor(colors_list[0])
                        elif settings_list[0] == "rainbow":
                            wee.pencolor("black")
            wee.forward(Square_SizeG)
            wee.pencolor("black")
            if settings_list[0] == "rainbow":
                wee.pencolor("white")
            wee.left(90)
            if settings_list[2] == "on":
                if Convert_to_Square_ID(x, y + 1) != "null":
                    if Dig_List[Convert_to_Square_ID(x, y + 1)] == "dug":
                        if settings_list[0] == "new" or settings_list[0] == "old":
                            if value == 1:
                                wee.pencolor("#d7b889")
                            elif value == 0:
                                wee.pencolor("#e5c29f")
                        elif settings_list[0] == "microsoft":
                            wee.pencolor(colors_list[0])
                        elif settings_list[0] == "rainbow":
                            wee.pencolor("black")
            wee.forward(Square_SizeG)
            wee.pencolor("black")
            if settings_list[0] == "rainbow":
                wee.pencolor("white")
            wee.left(90)
            if settings_list[2] == "on":
                if Convert_to_Square_ID(x - 1, y) != "null":
                    if Dig_List[Convert_to_Square_ID(x - 1, y)] == "dug":
                        if settings_list[0] == "new" or settings_list[0] == "old":
                            if value == 1:
                                wee.pencolor("#e5c29f")
                            elif value == 0:
                                wee.pencolor("#d7b889")
                        elif settings_list[0] == "microsoft":
                            wee.pencolor(colors_list[0])
                        elif settings_list[0] == "rainbow":
                            wee.pencolor("black")
            wee.forward(Square_SizeG)
            wee.pencolor("black")
            if settings_list[0] == "rainbow":
                wee.pencolor("white")
            wee.left(90)
            wee.end_fill()
        elif colors_list.index(color) == 9:
            wee.pencolor("black")
            if settings_list[0] != "rainbow":
                wee.fillcolor("black")
            elif settings_list[0] == "rainbow":
                wee.fillcolor("sky blue")
            wee.begin_fill()
            wee.forward(Square_SizeG)
            wee.left(90)
            wee.forward(Square_SizeG)
            wee.left(90)
            wee.forward(Square_SizeG)
            wee.left(90)
            wee.forward(Square_SizeG)
            wee.left(90)
            wee.end_fill()
        elif colors_list.index(color) == 10:
            if settings_list[0] == "rainbow":
                wee.pencolor("white")
            wee.fillcolor(colors_list[10])
            wee.begin_fill()
            wee.forward(Square_SizeG)
            wee.left(90)
            wee.forward(Square_SizeG)
            wee.left(90)
            wee.forward(Square_SizeG)
            wee.left(90)
            wee.forward(Square_SizeG)
            wee.left(90)
            wee.end_fill()
        elif colors_list.index(color) == 11:
            wee.pencolor("black")
            wee.fillcolor("white")
            wee.begin_fill()
            wee.forward(Square_SizeG)
            wee.left(90)
            wee.forward(Square_SizeG)
            wee.left(90)
            wee.forward(Square_SizeG)
            wee.left(90)
            wee.forward(Square_SizeG)
            wee.left(90)
            wee.end_fill()

    # Main Loop for keyboard inputs
    if settings_list[3] == "off":
        Help_Needed = 0
        Help_Lock = 0
        while Game_Over == False:
            Exit_Flag = 1
            if Has_Player_WonG == Win_VariableG:
                print("You WON!!!")
                Game_Over = True
            else:
                if Help_Needed >= 3 and Help_Lock == 0:
                    print('Type "quit" or "end" to end this game')
                    print("For more help on player commands, and how to play")
                    print('See the "help" section under the main menu')
                User_Input = input("What would you like to do next? ")
                Type_of_Input = Check_If_Valid_Input(User_Input)
                if Type_of_Input == 1:
                    Help_Needed = 0
                    Help_Lock = 1
                    User_Input_list = User_Input.split(":")
                    if User_Input_list[0] == "f":
                        User_Input_list2 = (User_Input_list[1]).split(",")
                        XcOd = int(User_Input_list2[0])
                        YcOd = int(User_Input_list2[1])
                        if Convert_to_Square_ID(XcOd, YcOd) != "null":
                            if Flag_List[Convert_to_Square_ID(XcOd, YcOd)] == 0:
                                wee_coords = Map_Wee(XcOd, YcOd)
                                wee.penup()
                                wee.goto(wee_coords[0], wee_coords[1])
                                wee.pendown()
                                Fill_Square(colors_list[10], "bruh", "bruhh", "bruhhh")
                                Flag_List[Convert_to_Square_ID(XcOd, YcOd)] = 1
                            elif Flag_List[Convert_to_Square_ID(XcOd, YcOd)] == "dug":
                                print("You cannot flag an already dug space!")
                            elif Flag_List[Convert_to_Square_ID(XcOd, YcOd)] == 1:
                                print("That space is already flagged!")
                        else:
                            print("Those coordinates are out of bounds! Please try again")
                    elif User_Input_list[0] == "u":
                        User_Input_list2 = (User_Input_list[1]).split(",")
                        XcOd = int(User_Input_list2[0])
                        YcOd = int(User_Input_list2[1])
                        if Convert_to_Square_ID(XcOd, YcOd) != "null":
                            if Flag_List[Convert_to_Square_ID(XcOd, YcOd)] == 1:
                                wee_coords = Map_Wee(XcOd, YcOd)
                                wee.penup()
                                wee.goto(wee_coords[0], wee_coords[1])
                                wee.pendown()
                                Fill_Square("white", "bruh", "bruhh", "bruhhh")
                                Flag_List[Convert_to_Square_ID(XcOd, YcOd)] = 0
                            elif Flag_List[Convert_to_Square_ID(XcOd, YcOd)] == "dug" or Flag_List[Convert_to_Square_ID(XcOd, YcOd)] == 0:
                                print("That space is already unflagged!")
                        else:
                            print("Those coordinates are out of bounds! Please try again")
                    else:
                        print("Invalid Action! Please Try Again")
                if Type_of_Input == 2:
                    Help_Needed = 0
                    Help_Lock = 1
                    User_Input_list = User_Input.split(",")
                    X_coordinate = int(User_Input_list[0])
                    Y_coordinate = int(User_Input_list[1])
                    if Convert_to_Square_ID(X_coordinate, Y_coordinate) != "null":
                        if Flag_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 1:
                            Exit_Flag = 0
                            while Exit_Flag == 0:
                                Flag_Inputt = input("You have flagged this area! Are you sure you want to dig it? ")
                                Flag_Check = Check_If_Valid_Input2(Flag_Inputt)
                                if Flag_Check == 0:
                                    print('Type "yes" or "no" to answer!')
                                if Flag_Check == 1:
                                    Exit_Flag = 1
                                if Flag_Check == 2:
                                    Exit_Flag = 2
                        if Exit_Flag == 1:
                            if Dig_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == "bomb":
                                print("You failed! Game Over")
                                add_to_numba = 0
                                while add_to_numba < Total_Bombs:
                                    numba = Box_List.index("bomb")
                                    Box_List.pop(numba)
                                    numba2 = numba + add_to_numba
                                    wee_coords = Convert_to_Coordinates(numba2)
                                    wee_coords1 = Map_Wee(wee_coords[0], wee_coords[1])
                                    wee.penup()
                                    wee.goto(wee_coords1[0], wee_coords1[1])
                                    wee.pendown()
                                    Fill_Square("black", "bruh", "bruhh", "bruhhh")
                                    add_to_numba = add_to_numba + 1
                                Game_Over = True
                            elif Dig_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == "dug":
                                print("That space has already been dug!")
                            else:
                                if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 0:
                                    wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                    wee.penup()
                                    wee.goto(wee_coords[0], wee_coords[1])
                                    wee.pendown()
                                    odd_Or_even3 = (X_coordinate + Y_coordinate) % 2
                                    Fill_Square(colors_list[0], odd_Or_even3, X_coordinate, Y_coordinate)
                                    Dig_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] = "dug"
                                    Flag_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] = "dug"
                                    Has_Player_WonG = Has_Player_WonG + 1 + Check_Neighboring_Squares2(X_coordinate, Y_coordinate)
                                    while len(Temp_Zero_List) > 0:
                                        Temp_XY = Convert_to_Coordinates(Temp_Zero_List[0])
                                        weeCoRdas = Map_Wee(Temp_XY[0],Temp_XY[1])
                                        wee.penup()
                                        wee.goto(weeCoRdas[0], weeCoRdas[1])
                                        wee.pendown()
                                        odd_Or_even4 = (Temp_XY[0] + Temp_XY[1]) % 2
                                        Fill_Square(colors_list[Box_List[Temp_Zero_List[0]]], odd_Or_even4, Temp_XY[0], Temp_XY[1])
                                        Dig_List[Temp_Zero_List[0]] = "dug"
                                        Flag_List[Temp_Zero_List[0]] = "dug"
                                        Has_Player_WonG = Has_Player_WonG + 1
                                        Has_Player_WonG = Has_Player_WonG + Check_Neighboring_Squares2(Temp_XY[0],Temp_XY[1])
                                        Temp_Zero_List.pop(0)
                                else:
                                    if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 1:
                                        wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                        wee.penup()
                                        wee.goto(wee_coords[0], wee_coords[1])
                                        wee.pendown()
                                        odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                        Fill_Square(colors_list[1], odd_Or_even, X_coordinate, Y_coordinate)
                                        Dig_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                        Flag_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                    if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 2:
                                        wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                        wee.penup()
                                        wee.goto(wee_coords[0], wee_coords[1])
                                        wee.pendown()
                                        odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                        Fill_Square(colors_list[2], odd_Or_even, X_coordinate, Y_coordinate)
                                        Dig_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                        Flag_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                    if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 3:
                                        wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                        wee.penup()
                                        wee.goto(wee_coords[0], wee_coords[1])
                                        wee.pendown()
                                        odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                        Fill_Square(colors_list[3], odd_Or_even, X_coordinate, Y_coordinate)
                                        Dig_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                        Flag_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                    if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 4:
                                        wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                        wee.penup()
                                        wee.goto(wee_coords[0], wee_coords[1])
                                        wee.pendown()
                                        odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                        Fill_Square(colors_list[4], odd_Or_even, X_coordinate, Y_coordinate)
                                        Dig_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                        Flag_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                    if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 5:
                                        wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                        wee.penup()
                                        wee.goto(wee_coords[0], wee_coords[1])
                                        wee.pendown()
                                        odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                        Fill_Square(colors_list[5], odd_Or_even, X_coordinate, Y_coordinate)
                                        Dig_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                        Flag_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                    if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 6:
                                        wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                        wee.penup()
                                        wee.goto(wee_coords[0], wee_coords[1])
                                        wee.pendown()
                                        odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                        Fill_Square(colors_list[6], odd_Or_even, X_coordinate, Y_coordinate)
                                        Dig_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                        Flag_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                    if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 7:
                                        wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                        wee.penup()
                                        wee.goto(wee_coords[0], wee_coords[1])
                                        wee.pendown()
                                        odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                        Fill_Square(colors_list[7], odd_Or_even, X_coordinate, Y_coordinate)
                                        Dig_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                        Flag_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                    if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 8:
                                        wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                        wee.penup()
                                        wee.goto(wee_coords[0], wee_coords[1])
                                        wee.pendown()
                                        odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                        Fill_Square(colors_list[8], odd_Or_even, X_coordinate, Y_coordinate)
                                        Dig_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                        Flag_List[
                                            Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                        ] = "dug"
                                    Has_Player_WonG = Has_Player_WonG + 1
                        else: pass
                    else:
                        print("Those coordinates are out of bounds! Please try again")
                if Type_of_Input == 0:
                    if Help_Lock == 0:
                        if Help_Needed < 2:
                            print("Invalid Action! Please try again")
                        Help_Needed = Help_Needed + 1
                    elif Help_Lock == 1:
                        print("Invalid Action! Please try again")
                if Type_of_Input == 3:
                    print("Those coordinates are out of bounds! Please try again")
                if Type_of_Input == 4:
                    print("Quitting Game...")
                    Game_Over = True
    # Main Loop for mouse inputs
    elif settings_list[3] == "on":
        def TurtleClick(x, y):
            global Has_Player_WonG
            global Game_Over
            global turtle_drawing
            global show_win_message
            if turtle_drawing == False:
                if Game_Over == False:
                    Exit_Flag = 1
                    square_x = (x + ((Square_SizeG * Grid_Width) / 2)) / Square_SizeG + 1
                    square_y = (y + ((Square_SizeG * Grid_Height) / 2)) / Square_SizeG + 1

                    coordinate_list = [str(int(square_x)), str(int(square_y))]
                    User_Input = ",".join(coordinate_list)
                    Type_of_Input = Check_If_Valid_Input(User_Input)
                    if Type_of_Input == 2:
                        Help_Needed = 0
                        Help_Lock = 1
                        User_Input_list = User_Input.split(",")
                        X_coordinate = int(User_Input_list[0])
                        Y_coordinate = int(User_Input_list[1])
                        if Convert_to_Square_ID(X_coordinate, Y_coordinate) != "null":
                            if Flag_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 1:
                                print("You cannot dig an already flagged space! Unflag it first to dig it.")
                                Exit_Flag = 2
                            if Exit_Flag == 1:
                                if Dig_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == "bomb":
                                    Game_Over = True
                                    turtle_drawing = True
                                    print("You failed! Game Over")
                                    add_to_numba = 0
                                    while add_to_numba < Total_Bombs:
                                        numba = Box_List.index("bomb")
                                        Box_List.pop(numba)
                                        numba2 = numba + add_to_numba
                                        wee_coords = Convert_to_Coordinates(numba2)
                                        wee_coords1 = Map_Wee(wee_coords[0], wee_coords[1])
                                        wee.penup()
                                        wee.goto(wee_coords1[0], wee_coords1[1])
                                        wee.pendown()
                                        Fill_Square("black", "bruh", "bruhh", "bruhhh")
                                        add_to_numba = add_to_numba + 1
                                    turtle_drawing = False
                                elif Dig_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == "dug":
                                    print("That space has already been dug!")
                                else:
                                    if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 0:
                                        turtle_drawing = True
                                        wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                        wee.penup()
                                        wee.goto(wee_coords[0], wee_coords[1])
                                        wee.pendown()
                                        odd_Or_even3 = (X_coordinate + Y_coordinate) % 2
                                        Fill_Square(colors_list[0], odd_Or_even3, X_coordinate, Y_coordinate)
                                        Dig_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] = "dug"
                                        Flag_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] = "dug"
                                        Has_Player_WonG += 1 + Check_Neighboring_Squares2(X_coordinate, Y_coordinate)
                                        while len(Temp_Zero_List) > 0:
                                            Temp_XY = Convert_to_Coordinates(Temp_Zero_List[0])
                                            weeCoRdas = Map_Wee(Temp_XY[0],Temp_XY[1])
                                            wee.penup()
                                            wee.goto(weeCoRdas[0], weeCoRdas[1])
                                            wee.pendown()
                                            odd_Or_even4 = (Temp_XY[0] + Temp_XY[1]) % 2
                                            Fill_Square(colors_list[Box_List[Temp_Zero_List[0]]], odd_Or_even4, Temp_XY[0], Temp_XY[1])
                                            Dig_List[Temp_Zero_List[0]] = "dug"
                                            Flag_List[Temp_Zero_List[0]] = "dug"
                                            Has_Player_WonG = Has_Player_WonG + 1
                                            Has_Player_WonG = Has_Player_WonG + Check_Neighboring_Squares2(Temp_XY[0],Temp_XY[1])
                                            Temp_Zero_List.pop(0)
                                        turtle_drawing = False
                                    else:
                                        if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 1:
                                            turtle_drawing = True
                                            wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                            wee.penup()
                                            wee.goto(wee_coords[0], wee_coords[1])
                                            wee.pendown()
                                            odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                            Fill_Square(colors_list[1], odd_Or_even, X_coordinate, Y_coordinate)
                                            Dig_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            Flag_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            turtle_drawing = False
                                        if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 2:
                                            turtle_drawing = True
                                            wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                            wee.penup()
                                            wee.goto(wee_coords[0], wee_coords[1])
                                            wee.pendown()
                                            odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                            Fill_Square(colors_list[2], odd_Or_even, X_coordinate, Y_coordinate)
                                            Dig_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            Flag_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            turtle_drawing = False
                                        if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 3:
                                            turtle_drawing = True
                                            wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                            wee.penup()
                                            wee.goto(wee_coords[0], wee_coords[1])
                                            wee.pendown()
                                            odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                            Fill_Square(colors_list[3], odd_Or_even, X_coordinate, Y_coordinate)
                                            Dig_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            Flag_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            turtle_drawing = False
                                        if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 4:
                                            turtle_drawing = True
                                            wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                            wee.penup()
                                            wee.goto(wee_coords[0], wee_coords[1])
                                            wee.pendown()
                                            odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                            Fill_Square(colors_list[4], odd_Or_even, X_coordinate, Y_coordinate)
                                            Dig_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            Flag_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            turtle_drawing = False
                                        if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 5:
                                            turtle_drawing = True
                                            wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                            wee.penup()
                                            wee.goto(wee_coords[0], wee_coords[1])
                                            wee.pendown()
                                            odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                            Fill_Square(colors_list[5], odd_Or_even, X_coordinate, Y_coordinate)
                                            Dig_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            Flag_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            turtle_drawing = False
                                        if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 6:
                                            turtle_drawing = True
                                            wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                            wee.penup()
                                            wee.goto(wee_coords[0], wee_coords[1])
                                            wee.pendown()
                                            odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                            Fill_Square(colors_list[6], odd_Or_even, X_coordinate, Y_coordinate)
                                            Dig_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            Flag_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            turtle_drawing = False
                                        if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 7:
                                            turtle_drawing = True
                                            wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                            wee.penup()
                                            wee.goto(wee_coords[0], wee_coords[1])
                                            wee.pendown()
                                            odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                            Fill_Square(colors_list[7], odd_Or_even, X_coordinate, Y_coordinate)
                                            Dig_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            Flag_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            turtle_drawing = False
                                        if Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 8:
                                            turtle_drawing = True
                                            wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                            wee.penup()
                                            wee.goto(wee_coords[0], wee_coords[1])
                                            wee.pendown()
                                            odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                            Fill_Square(colors_list[8], odd_Or_even, X_coordinate, Y_coordinate)
                                            Dig_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            Flag_List[
                                                Convert_to_Square_ID(X_coordinate, Y_coordinate)
                                            ] = "dug"
                                            turtle_drawing = False
                                        Has_Player_WonG = Has_Player_WonG + 1
                            else: pass
                        else:
                            print("You have clicked outside the map! Please try again")
                    if Type_of_Input == 0:
                        print("You have clicked outside the map! Please try again")
                    if Type_of_Input == 3:
                        print("Those coordinates are out of bounds! Please try again")
                    if Type_of_Input == 4:
                        print("Quitting Game...")
                        Game_Over = True
                else: print('The game is over! Press "e" to exit')
            else:
                if Game_Over == False:
                    print('The turtle is still drawing! Please wait before clicking another square.')
            if Has_Player_WonG == Win_VariableG and show_win_message == True:
                print("You WON!!!")
                Game_Over = True
                show_win_message = False

        def TurtleClick2(x, y):
            global Has_Player_WonG
            global Game_Over
            global turtle_drawing
            if turtle_drawing == False:
                if Game_Over == False:
                    square_x = (x + ((Square_SizeG * Grid_Width) / 2)) / Square_SizeG + 1
                    square_y = (y + ((Square_SizeG * Grid_Height) / 2)) / Square_SizeG + 1
                    if Convert_to_Square_ID(int(square_x), int(square_y)) != "null":
                        if Flag_List[Convert_to_Square_ID(int(square_x), int(square_y))] == 0:
                            coordinate_list = ["f:" + str(int(square_x)), str(int(square_y))]
                            User_Input = ",".join(coordinate_list)
                        elif Flag_List[Convert_to_Square_ID(int(square_x), int(square_y))] == 1:
                            coordinate_list = ["u:" + str(int(square_x)), str(int(square_y))]
                            User_Input = ",".join(coordinate_list)
                        elif Flag_List[Convert_to_Square_ID(int(square_x), int(square_y))] == "dug":
                            print("You cannot flag an already dug space!")
                            User_Input = "f37"
                    else: User_Input = "f37"
                    Type_of_Input = Check_If_Valid_Input(User_Input)
                    if Type_of_Input == 1:
                        Help_Needed = 0
                        Help_Lock = 1
                        User_Input_list = User_Input.split(":")
                        if User_Input_list[0] == "f":
                            User_Input_list2 = (User_Input_list[1]).split(",")
                            XcOd = int(User_Input_list2[0])
                            YcOd = int(User_Input_list2[1])
                            if Convert_to_Square_ID(XcOd, YcOd) != "null":
                                if Flag_List[Convert_to_Square_ID(XcOd, YcOd)] == 0:
                                    turtle_drawing = True
                                    wee_coords = Map_Wee(XcOd, YcOd)
                                    wee.penup()
                                    wee.goto(wee_coords[0], wee_coords[1])
                                    wee.pendown()
                                    Fill_Square(colors_list[10], "bruh", "bruhh", "bruhhh")
                                    Flag_List[Convert_to_Square_ID(XcOd, YcOd)] = 1
                                    turtle_drawing = False
                                elif Flag_List[Convert_to_Square_ID(XcOd, YcOd)] == "dug":
                                    print("You cannot flag an already dug space!")
                                elif Flag_List[Convert_to_Square_ID(XcOd, YcOd)] == 1:
                                    print("That space is already flagged!")
                            else:
                                print("Those coordinates are out of bounds! Please try again")
                        elif User_Input_list[0] == "u":
                            User_Input_list2 = (User_Input_list[1]).split(",")
                            XcOd = int(User_Input_list2[0])
                            YcOd = int(User_Input_list2[1])
                            if Convert_to_Square_ID(XcOd, YcOd) != "null":
                                if Flag_List[Convert_to_Square_ID(XcOd, YcOd)] == 1:
                                    turtle_drawing = True
                                    wee_coords = Map_Wee(XcOd, YcOd)
                                    wee.penup()
                                    wee.goto(wee_coords[0], wee_coords[1])
                                    wee.pendown()
                                    Fill_Square("white", "bruh", "bruhh", "bruhhh")
                                    Flag_List[Convert_to_Square_ID(XcOd, YcOd)] = 0
                                    turtle_drawing = False
                                elif Flag_List[Convert_to_Square_ID(XcOd, YcOd)] == "dug" or Flag_List[Convert_to_Square_ID(XcOd, YcOd)] == 0:
                                    print("That space is already unflagged!")
                            else:
                                print("Those coordinates are out of bounds! Please try again")
                        else:
                            print("Invalid Action! Please Try Again")
                    if Type_of_Input == 0:
                        print("You have clicked outside the map! Please try again")
                    if Type_of_Input == 3:
                        print("Those coordinates are out of bounds! Please try again")
                    if Type_of_Input == 4:
                        print("Quitting Game...")
                        Game_Over = True
                else: print('The game is over! Press "e" to exit')
            else:
                if Game_Over == False:
                    print('The turtle is still drawing! Please wait before clicking another square.')

        def Exit():
            if turtle_drawing == False:
                turtle.bye()
            elif turtle_drawing == True and Game_Over == True:
                print("The bombs are still exploding! You cannot exit yet")

        while Game_Over == False:
            try:
                turtle.onscreenclick(TurtleClick)
                turtle.onscreenclick(TurtleClick2, btn= 3)
                turtle.onkeypress(Exit, "e")
                turtle.listen()
                turtle.mainloop()
            except turtle.Terminator: break
        turtle.done

        Type_of_Input = 3

    # Exit Loop
    Exit_Game = False
    while Exit_Game == False:
        if Type_of_Input != 4:
            Would_Play_Again = 0
            while Would_Play_Again == 0:
                Play_Again = input("Would you like to play again? ")
                if Check_If_Valid_Input2(Play_Again) == 1:
                    Would_Play_Again = 1
                    if settings_list[3] == "off":
                        turtle.clearscreen()
                    Exit_Game = True
                elif Check_If_Valid_Input2(Play_Again) == 2:
                    Would_Play_Again = 2
                else:
                    print('Type "yes" or "no" to answer!')
        elif Type_of_Input == 4:
            Would_Play_Again = 2
        if Exit_Game == False:
            Exit_Input = input("Type anything here and press enter to exit to the main menu: ")
            print("---------------------------------------------------------------------")
            if settings_list[3] == "off":
                turtle.clearscreen()
            Exit_Game = True

    return Would_Play_Again

def Tutorial():
    Tutorial_Finished = False
    while Tutorial_Finished == False:
        print("---------------------------------------------------------------------")
        print("TurtleSweeper! - On the sandy dunes of turtle island, your task is to")
        print("collect enough sand for your glass-making businness.")
        print("However, you must be careful to not to dig up any turtle nests!")
        print("Not only is it bad for the turtles, but this species of turtle is")
        print("known to explode upon contact with their eggs!")
        read = input("Type anything here and press enter to continue: ")
        print("---------------------------------------------------------------------")
        print("KEYBOARD controls:")
        print("To dig a square, write the coordinates of the square in the format X,Y")
        print('To flag a square, write "f:" followed by the coordinates of the square')
        print("Example: f:3,4")
        print('To unflag a square, write "u:" followed by the coordinates of the square')
        print("Example: u:3,4")
        print('To quit the game at any time, type "end" or "quit"')
        read2 = input("Type anything here and press enter to continue: ")
        print("---------------------------------------------------------------------")
        print("MOUSE controls:")
        print("To dig a square, left click it")
        print('To flag or unflag a square, right click it')
        print('To quit the game at any time, press "e" on the keyboard')
        read3 = input("Type anything here and press enter to return to the main menu: ")
        print("---------------------------------------------------------------------")
        print("Use flagging to your advantage - to mark possibly dangerous squares!")
        print("Each square (with surrounding nests) will have a number indicating")
        print("the total number of nests surrounding it!")
        print("Dig all of the squares in the board, without touching any nests!")
        print("Good Luck!")
        read4 = input("Type anything here and press enter to return to the main menu: ")
        print("---------------------------------------------------------------------")
        Tutorial_Finished = True

def Credits():
    print("---------------------------------------------------------------------")
    print("TurtleSweeper! version - 1.3")
    print(" ")
    print("Release Notes:")
    print(" ")
    print(" - MOUSE CONTROLS ADDED!:")
    print("   Use the settings menu to switch between mouse and keyboard inputs")
    print(" - NEW COLOR THEMES ADDED: RAINBOW & ORIGINAL MICROSOFT")
    print('   Try out the new "rainbow" theme - the first DARK theme of')
    print("   TurtleSweeper!")
    print('   Want a more nostalgic theme instead? Try the "original-microsoft"')
    print("   theme to get the look and feel of microsoft's original game of")
    print("   minesweeper!")
    print("   Simply switch themes in the settings menu!")
    print(" ")
    print("Created by Sheerabdhi Niranjan")
    print("All Rights Reserved")
    print(" ")
    read = input("Type anything here and press enter to continue: ")
    print("---------------------------------------------------------------------")

def Settings():
    print("---------------------------------------------------------------------")
    number_color_theme = settings_list[0]
    turtle_shown = settings_list[1]
    connected_texture_on = settings_list[2]
    mouse_controls = settings_list[3]
    setting_exit = False
    Settings_Help = 0
    while setting_exit == False:
        if Settings_Help == 0:
            print("Standalone Settings:")
            if number_color_theme == "old":
                print("1 - Color Theme: [old] new rainbow original-microsoft")
            if number_color_theme == "new":
                print("1 - Color Theme: old [new] rainbow original-microsoft")
            if number_color_theme == "rainbow":
                print("1 - Color Theme: old new [rainbow] original-microsoft")
            if number_color_theme == "microsoft":
                print("1 - Color Theme: old new rainbow [original-microsoft]")
            if turtle_shown == "shown":
                print("2 - Drawing Turtle: [shown] hidden")
            if turtle_shown == "hidden":
                print("2 - Drawing Turtle: shown [hidden]")
            if connected_texture_on == "on":
                print("3 - Connected Grid Texture (Experimental!): [on] off")
            if connected_texture_on == "off":
                print("3 - Connected Grid Texture (Experimental!): on [off]")
            print(" ")
            print("Mutually Exclusive Settings:")
            if mouse_controls == "on":
                print("4 - Mouse Controls: [on] off")
            elif mouse_controls == "off":
                print("4 - Mouse Controls: on [off]")
            if mouse_controls == "on":
                print("5 - Keyboard Controls: on [off]")
            elif mouse_controls == "off":
                print("5 - Keyboard Controls: [on] off")
            print(" ")
            print("6 - Exit Settings")
            print(" ")
        setting_change = input("Type the number of the setting you would like to change, or 6 to exit: ")
        if setting_change == "1":
            settingchange1exit = False
            while settingchange1exit == False:
                print(" ")
                print("1 - old")
                print("2 - new")
                print("3 - rainbow")
                print("4 - microsoft")
                print(" ")
                setting1input = input("Type the number of the option you would like to switch this setting to: ")
                if setting1input == "1":
                    print("Setting switched!")
                    number_color_theme = "old"
                    settingchange1exit = True
                elif setting1input == "2":
                    print("Setting switched!")
                    number_color_theme = "new"
                    settingchange1exit = True
                elif setting1input == "3":
                    print("Setting switched!")
                    number_color_theme = "rainbow"
                    settingchange1exit = True
                elif setting1input == "4":
                    print("Setting switched!")
                    number_color_theme = "microsoft"
                    settingchange1exit = True
                else:
                    print("Invalid input! Please try again")
        elif setting_change == "2":
            print("Setting switched!")
            if turtle_shown == "shown":
                turtle_shown = "hidden"
            elif turtle_shown == "hidden":
                turtle_shown = "shown"
        elif setting_change == "3":
            print("Setting switched!")
            if connected_texture_on == "on":
                connected_texture_on = "off"
            elif connected_texture_on == "off":
                connected_texture_on = "on"
        elif setting_change == "4" or setting_change == "5":
            print("Setting switched!")
            if mouse_controls == "on":
                mouse_controls = "off"
            elif mouse_controls == "off":
                mouse_controls = "on"
        elif setting_change == "6":
            setting_exit = True
        else:
            print("Invalid input! Please try again")
            Settings_Help = 1
    return [number_color_theme, turtle_shown, connected_texture_on, mouse_controls]

# Main main loop
Help_Needed_Main = 0
Game_Exit = False
while Game_Exit == False:
    # Game Intro
    if Help_Needed_Main ==  0:
        if First_Intro_Done == True:
            print("TurtleSweeper!")
        elif First_Intro_Done == False:
            First_Intro_Done = True
        print('Type "1" to play')
        print('Type "2" for help')
        print('Type "3" for release notes and credits')
        print('Type "4" to change settings')
        print('Type "5" to exit')
        Main_Input = input ("What would you like to do? ")
    elif Help_Needed_Main == 1:
        Main_Input = input ('Type "1", "2", "3", "4", or "5" and press enter to continue: ')
    if Main_Input == "1":
        Help_Needed_Main = 0
        Game_Finished = False
        while Game_Finished == False:
            Does_Player_Play_Again = Play()
            Played_Once = True
            if Does_Player_Play_Again == 1:
                Has_Player_WonG = 0
                Game_Over = False
            elif Does_Player_Play_Again == 2:
                Has_Player_WonG = 0
                Game_Over = False
                Game_Finished = True
            else:
                print("An error has occurred!")
                print("Error Code: 1")
                readinfinity = input("Type anything here and press enter to exit: ")
                Game_Finished = True
                Game_Exit = True
    elif Main_Input == "2":
        Help_Needed_Main = 0
        Tutorial()
    elif Main_Input == "3":
        Help_Needed_Main = 0
        Credits()
    elif Main_Input == "4":
        Help_Needed_Main = 0
        settings_list = Settings()
    elif Main_Input == "5":
        Help_Needed_Main = 0
        Game_Exit = True
    else:
        Help_Needed_Main = 1

