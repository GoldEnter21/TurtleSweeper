import turtle
import random
import math

settings_list = ["new", "shown", "unconnected", "on", "fixed", "new", "enabled"]
settings_list2 = ["Color Theme:", "Drawing Turtle:", "Grid Textures:", "Mouse Controls:", "# of Bombs:", "Flag Textures:", "Flag Counter:"]
Color_Theme_list = ["old", "new", "microsoft", "rainbow"]
Drawing_Turtle_list = ["shown", "hidden"]
Grid_Texture_list = ["connected (old)", "connected (new)", "unconnected"]
Mouse_Control_list = ["on", "off"]
Bomb_Number_list = ["fixed", "random"]
Flag_Animation_list = ["new", "old"]
Flag_Counter_list = ["enabled", "disabled"]
settings_list_list = [Color_Theme_list, Drawing_Turtle_list, Grid_Texture_list, Mouse_Control_list, Bomb_Number_list, Flag_Animation_list, Flag_Counter_list]

Has_Player_WonG = 0
Game_Over = False
Played_Once = False
turtle_drawing = False
show_win_message = True
Grid_Width = 0
Grid_Height = 0
Difficulty_Choose = False
Would_Play_Again = 0
continue_working = True
Exit_Once = False
Draw_Settings_Menu = False
num_settings = len(settings_list)
setting_width = 480/(num_settings + 1)
Settings_Exit = False
First_Intro_Done = False
Flag_Count = 0
# time = 0

def Play():
    global Has_Player_WonG
    global Game_Over
    global Difficulty_Choose
    global Grid_Width
    global Grid_Height
    global Would_Play_Again
    global show_win_message
    if settings_list[3] == "off":
        print("---------------------------------------------------------------------")

    def Difficulty_Choose_Screen():
        turtle.TurtleScreen._RUNNING = True

        wheat = turtle.Turtle()
        wheat.hideturtle()
        wheat.speed("fastest")

        def CreateBox(x, y):
            wheat.penup()
            wheat.goto(x,y)
            wheat.pendown()
            wheat.right(90)
            wheat.forward(40)
            wheat.left(90)
            wheat.forward(200)
            wheat.left(90)
            wheat.forward(40)
            wheat.left(90)
            wheat.forward(200)
            wheat.right(180)

        CreateBox(-100, 103)
        wheat.penup()
        wheat.goto(0,71)
        wheat.write("EASY", align="center", font=("Baloo Chettan 2", 12, "normal"))
        CreateBox(-100, 48)
        wheat.penup()
        wheat.goto(0,16)
        wheat.write("MEDIUM", align="center", font=("Baloo Chettan 2", 12, "normal"))
        CreateBox(-100, -7)
        wheat.penup()
        wheat.goto(0,-39)
        wheat.write("HARD", align="center", font=("Baloo Chettan 2", 12, "normal"))
        CreateBox(-100, -62)
        wheat.penup()
        wheat.goto(0,-94)
        wheat.write("CUSTOM", align="center", font=("Baloo Chettan 2", 12, "normal"))

        wheat.penup()
        wheat.goto(0, 205)
        wheat.write("CHOOSE A DIFFICULTY:", align="center", font=("Baloo Chettan 2", 30, "bold"))

    def Check_If_Valid_Input3(Input):
        Valid_Input = 0
        if Input == "easy":
            Valid_Input = 1
        elif Input == "medium":
            Valid_Input = 2
        elif Input == "hard":
            Valid_Input = 3
        return Valid_Input

    turtle.TurtleScreen._RUNNING = True

    turtle.clearscreen()

    # Grid Parameters (to change difficulty)
    if settings_list[3] == "on":
        while Difficulty_Choose == False:
            Difficulty_Choose_Screen()
            def GetCoords2(x, y):
                global Grid_Width
                global Grid_Height
                global Difficulty_Choose
                if -100 < x < 100:
                    if 63 < y < 103:
                        Difficulty_Input = "1"
                    elif 8 < y < 48:
                        Difficulty_Input = "2"
                    elif -47 < y < -7:
                        Difficulty_Input = "3"
                    elif -102 < y < -62:
                        Difficulty_Input = "4"
                else:
                    Difficulty_Input = "big bruh"
                try:
                    if Difficulty_Input == "1":
                        Grid_Width = 10
                        Grid_Height = 8
                        Difficulty_Choose = True
                        turtle.bye()
                    elif Difficulty_Input == "2":
                        Grid_Width = 18
                        Grid_Height = 14
                        Difficulty_Choose = True
                        turtle.bye()
                    elif Difficulty_Input == "3":
                        Grid_Width = 24
                        Grid_Height = 20
                        Difficulty_Choose = True
                        turtle.bye()
                    elif Difficulty_Input == "4":
                        Difficulty_Choose = True
                        turtle.bye()
                        turtle.TurtleScreen._RUNNING = True
                        turtle.setup(720, 675)
                        GridWchosen = False
                        GridHchosen = False
                        Grid_Width = turtle.numinput("Grid Width", "Type the grid width for your custom game. Non-integers will be rounded!", minval = 8, maxval = 50)
                        while GridWchosen == False:
                            hmm = (type(Grid_Width) is not float)
                            if hmm == True:
                                Grid_Width = turtle.numinput("Grid Width", "Please type a number from 8 to 50 to set the grid width for your custom game", minval = 8, maxval = 50)
                            elif hmm == False:
                                Grid_Width = int(round(Grid_Width))
                                GridWchosen = True
                        Grid_Height = turtle.numinput("Grid Height", "Type the grid height for your custom game. Non-integers will be rounded!", minval = 8, maxval = 50)
                        while GridHchosen == False:
                            hmm = (type(Grid_Height) is not float)
                            if hmm == True:
                                Grid_Height = turtle.numinput("Grid Height", "Please type a number from 8 to 50 to set the grid height for your custom game", minval = 8, maxval = 50)
                            elif hmm == False:
                                Grid_Height = int(round(Grid_Height))
                                GridHchosen = True
                        turtle.bye()
                    else: pass
                except UnboundLocalError: pass
            try:
                turtle.onscreenclick(GetCoords2)
                turtle.listen()
                turtle.mainloop()
            except turtle.Terminator: break
    elif settings_list[3] == "off":
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

    turtle.setup(720, 675)

    # The turtle that does all the work
    wee = turtle.Turtle()
    wee.shape("turtle")
    wee.speed("fastest")
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

    # Literally a list of numbers counting to the max bombs (used for pseudorandom sampling)
    Nums_List = []
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
                wee.write(number, align="center", font=("Lato", int(Square_Size / 4), "normal"))
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
                wee.write(number, align="center", font=("Lato", int(Square_Size / 4), "normal"))
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
        global Flag_Count
        if settings_list[4] == "random":
            num_Box_List = 0
            while num_Box_List < Max_Squares:
                NextAppend = random.random()
                if NextAppend > Bomb_Probability:
                    TheAppend = 0
                if NextAppend <= Bomb_Probability:
                    TheAppend = "bomb"
                    Flag_Count = Flag_Count + 1
                Box_List.append(TheAppend)
                num_Box_List = num_Box_List + 1
        elif settings_list[4] == "fixed":
            num_Bomb = round((0.000210883 * (Max_Squares ** 2)) + (0.104405 * Max_Squares) + 0.297919)
            Flag_Count = num_Bomb
            num_Box_List = 0
            while num_Box_List < Max_Squares:
                Nums_List.append(num_Box_List)
                Box_List.append(0)
                num_Box_List = num_Box_List + 1
            Bomb_List = random.sample(Nums_List, num_Bomb)
            while len(Bomb_List) > 0:
                Box_List[Bomb_List[0]] = "bomb"
                Bomb_List.pop(0)

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
        yiay = [-1, 0, 1]
        oxen = [-1, 0, 1]
        yiayI = 0
        oxenI = 0
        itera = 1
        while itera <= 9:
            Y_y = y + yiay[yiayI]
            X_x = x + oxen[oxenI]
            if Convert_to_Square_ID(X_x, Y_y) != "null":
                if Box_List[Convert_to_Square_ID(X_x, Y_y)] == "bomb":
                    num_Surrounding_Bomb = num_Surrounding_Bomb + 1
            if itera % 3 == 0:
                oxenI = 0
                yiayI = yiayI + 1
            else:
                oxenI = oxenI + 1
            itera = itera + 1
        return num_Surrounding_Bomb

    def Check_Neighboring_Squares2(x,y):
        add_to_Player1 = 0
        yiay = [-1, 0, 1]
        oxen = [-1, 0, 1]
        yiayI = 0
        oxenI = 0
        itera = 1
        while itera <= 9:
            Y_y = y + yiay[yiayI]
            X_x = x + oxen[oxenI]
            if Convert_to_Square_ID(X_x, Y_y) != "null":
                if Dig_List[Convert_to_Square_ID(X_x,Y_y)] == 0:
                    if Flag_List[Convert_to_Square_ID(X_x,Y_y)] != 1:
                        if Box_List[Convert_to_Square_ID(X_x,Y_y)] > 0:
                            Dig_List[Convert_to_Square_ID(X_x,Y_y)] = "dug"
                            Flag_List[Convert_to_Square_ID(X_x,Y_y)] = "dug"
                            wee_cords = Map_Wee(X_x,Y_y)
                            wee.penup()
                            wee.goto(wee_cords[0],wee_cords[1])
                            wee.pendown()
                            odd_Or_even2 = (X_x + Y_y) % 2
                            Fill_Square(colors_list[Box_List[Convert_to_Square_ID(X_x,Y_y)]], odd_Or_even2, X_x, Y_y)
                            add_to_Player1 = add_to_Player1 + 1
                        if Box_List[Convert_to_Square_ID(X_x,Y_y)] == 0:
                            if Temp_Zero_List.count(Convert_to_Square_ID(X_x,Y_y)) == 0:
                                Temp_Zero_List.append(Convert_to_Square_ID(X_x,Y_y))
            if itera % 3 == 0:
                oxenI = 0
                yiayI = yiayI + 1
            else:
                oxenI = oxenI + 1
            itera = itera + 1
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
        global continue_working
        def Fill_Square_Old():
            if continue_working == True:
                if -1 < colors_list.index(color) < 9:
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
                    if continue_working == True and colors_list.index(color) != 0:
                        if Grid_Width > 10 or Grid_Height > 8:
                            wee.write(str(colors_list.index(color)), align = "center", font = ("Sans", int(Square_SizeG / 2), "bold"))
                        else:
                            wee.write(str(colors_list.index(color)), align = "center", font = ("Sans", int(Square_SizeG / 2), "normal"))
                    wee.backward(Square_SizeG / 10)
                    wee.right(90)
                    wee.backward(Square_SizeG / 2)
                    wee.pendown()
                    wee.pencolor("black")

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
                    if settings_list[5] == "old":
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

                    elif settings_list[5] == "new":
                        wee.penup()
                        wee.forward(1/6 * Square_SizeG)
                        wee.left(90)
                        wee.forward(1/8 * Square_SizeG)
                        wee.pendown()
                        wee.begin_fill()
                        wee.pensize(2)
                        wee.pencolor("black")
                        wee.fillcolor(colors_list[10])
                        wee.forward(3/4 * Square_SizeG)
                        wee.right(110.5555555555555555555555)
                        wee.forward(math.sqrt((1/4 * Square_SizeG)**2 + (2/3 * Square_SizeG)**2))
                        wee.right(138.8888888888888888888)
                        wee.forward(math.sqrt((1/4 * Square_SizeG)**2 + (2/3 * Square_SizeG)**2))
                        wee.end_fill()
                        wee_cards = Map_Wee(x, y)
                        wee.penup()
                        wee.goto(wee_cards[0], wee_cards[1])
                        wee.pendown()
                        wee.seth(0)
                        wee.pensize(1)
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

        def Fill_Square_Unconnected():
            if continue_working == True:
                if -1 < colors_list.index(color) < 9:
                    if settings_list[0] == "new" or settings_list[0] == "old":
                        if value == 1:
                            wee.fillcolor("#d7b889")
                        if value == 0:
                            wee.fillcolor("#e5c29f")
                    elif settings_list[0] == "rainbow":
                        wee.fillcolor("black")
                    elif settings_list[0] == "microsoft":
                        wee.fillcolor(colors_list[0])
                    if settings_list[0] == "rainbow":
                        wee.pencolor("white")
                    else:
                        wee.pencolor("black")
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
                    wee.penup()
                    wee.forward(Square_SizeG / 2)
                    wee.left(90)
                    wee.forward(Square_SizeG / 10)
                    wee.pencolor(color)
                    if continue_working == True and colors_list.index(color) != 0:
                        if Grid_Width > 10 or Grid_Height > 8:
                            wee.write(str(colors_list.index(color)), align = "center", font = ("Sans", int(Square_SizeG / 2), "bold"))
                        else:
                            wee.write(str(colors_list.index(color)), align = "center", font = ("Sans", int(Square_SizeG / 2), "normal"))
                    wee.backward(Square_SizeG / 10)
                    wee.right(90)
                    wee.backward(Square_SizeG / 2)
                    wee.pendown()
                    wee.pencolor("black")
                elif colors_list.index(color) == 9:
                    if settings_list[0] != "rainbow":
                        wee.pencolor("black")
                        wee.fillcolor("black")
                    elif settings_list[0] == "rainbow":
                        wee.pencolor("white")
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
                    if settings_list[5] == "old":
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

                    elif settings_list[5] == "new":
                        wee.penup()
                        wee.forward(1/6 * Square_SizeG)
                        wee.left(90)
                        wee.forward(1/8 * Square_SizeG)
                        wee.pendown()
                        wee.begin_fill()
                        wee.pensize(2)
                        wee.pencolor("black")
                        wee.fillcolor(colors_list[10])
                        wee.forward(3/4 * Square_SizeG)
                        wee.right(110.5555555555555555555555)
                        wee.forward(math.sqrt((1/4 * Square_SizeG)**2 + (2/3 * Square_SizeG)**2))
                        wee.right(138.8888888888888888888)
                        wee.forward(math.sqrt((1/4 * Square_SizeG)**2 + (2/3 * Square_SizeG)**2))
                        wee.end_fill()
                        wee_cards = Map_Wee(x, y)
                        wee.penup()
                        wee.goto(wee_cards[0], wee_cards[1])
                        wee.pendown()
                        wee.seth(0)
                        wee.pensize(1)
                elif colors_list.index(color) == 11:
                    if settings_list[0] != "rainbow":
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
                    else:
                        wee.pencolor("white")
                        wee.fillcolor("white")
                        wee.begin_fill()
                        sides_Checked = 0
                        Cx = 0
                        Cy = -1
                        Black_List = []
                        while sides_Checked < 4:
                            if Convert_to_Square_ID(x + Cx, y + Cy) != "null":
                                if Dig_List[Convert_to_Square_ID(x + Cx, y + Cy)] == "dug":
                                    if settings_list[5] == "old":
                                        if Flag_List[Convert_to_Square_ID(x + Cx, y + Cy)] == 1:
                                            wee.pencolor("white")
                                            Black_List.append(str(Cx) + str(Cy))
                                    else:
                                        wee.pencolor("white")
                                        Black_List.append(str(Cx) + str(Cy))
                                else:
                                    wee.pencolor("black")
                            else:
                                wee.pencolor("black")
                            wee.forward(Square_SizeG)
                            wee.left(90)
                            if Cy == -1:
                                Cy = 0
                                Cx = 1
                            elif Cx == 1:
                                Cy = 1
                                Cx = 0
                            elif Cy == 1:
                                Cy = 0
                                Cx = -1
                            sides_Checked = sides_Checked + 1
                        wee.end_fill()
                        wee_coordsF = Map_Wee(x ,y)
                        wee.pencolor("white")
                        wee.penup()
                        while len(Black_List) > 0:
                            if Black_List[0] == "0-1":
                                wee.goto(wee_coordsF[0],wee_coordsF[1])
                                wee.pendown()
                                wee.seth(0)
                            if Black_List[0] == "10":
                                wee.goto(wee_coordsF[0] + Square_SizeG,wee_coordsF[1])
                                wee.pendown()
                                wee.seth(90)
                            if Black_List[0] == "01":
                                wee.goto(wee_coordsF[0] + Square_SizeG,wee_coordsF[1] + Square_SizeG)
                                wee.pendown()
                                wee.seth(180)
                            if Black_List[0] == "-10":
                                wee.goto(wee_coordsF[0],wee_coordsF[1] + Square_SizeG)
                                wee.pendown()
                                wee.seth(270)
                            wee.forward(Square_SizeG)
                            wee.penup()
                            Black_List.pop(0)
                        wee.goto(wee_coordsF[0],wee_coordsF[1])
                        wee.seth(0)

        def Fill_Square_Regular():
            if continue_working == True:
                if -1 < colors_list.index(color) < 9:
                    if settings_list[0] == "new" or settings_list[0] == "old":
                        if value == 1:
                            wee.fillcolor("#d7b889")
                        if value == 0:
                            wee.fillcolor("#e5c29f")
                    elif settings_list[0] == "microsoft":
                        wee.fillcolor(colors_list[0])
                    wee.begin_fill()
                    sides_Checked = 0
                    Cx = 0
                    Cy = -1
                    Black_List = []
                    while sides_Checked < 4:
                        if Convert_to_Square_ID(x + Cx, y + Cy) != "null":
                            if Dig_List[Convert_to_Square_ID(x + Cx, y + Cy)] == "dug":
                                if settings_list[0] == "new" or settings_list[0] == "old":
                                    if value == 1:
                                        wee.pencolor("#e5c29f")
                                    elif value == 0:
                                        wee.pencolor("#d7b889")
                                elif settings_list[0] == "microsoft":
                                    wee.pencolor(colors_list[0])
                            else:
                                wee.pencolor("white")
                                Black_List.append(str(Cx) + str(Cy))
                        else:
                            wee.pencolor("white")
                            Black_List.append(str(Cx) + str(Cy))
                        wee.forward(Square_SizeG)
                        wee.left(90)
                        if Cy == -1:
                            Cy = 0
                            Cx = 1
                        elif Cx == 1:
                            Cy = 1
                            Cx = 0
                        elif Cy == 1:
                            Cy = 0
                            Cx = -1
                        sides_Checked = sides_Checked + 1
                    wee.end_fill()
                    wee_coordsF = Map_Wee(x ,y)
                    wee.pencolor("black")
                    wee.penup()
                    while len(Black_List) > 0:
                        if Black_List[0] == "0-1":
                            wee.goto(wee_coordsF[0],wee_coordsF[1])
                            wee.pendown()
                            wee.seth(0)
                        if Black_List[0] == "10":
                            wee.goto(wee_coordsF[0] + Square_SizeG,wee_coordsF[1])
                            wee.pendown()
                            wee.seth(90)
                        if Black_List[0] == "01":
                            wee.goto(wee_coordsF[0] + Square_SizeG,wee_coordsF[1] + Square_SizeG)
                            wee.pendown()
                            wee.seth(180)
                        if Black_List[0] == "-10":
                            wee.goto(wee_coordsF[0],wee_coordsF[1] + Square_SizeG)
                            wee.pendown()
                            wee.seth(270)
                        wee.forward(Square_SizeG)
                        wee.penup()
                        Black_List.pop(0)
                    wee.goto(wee_coordsF[0],wee_coordsF[1])
                    wee.seth(0)
                    wee.penup()
                    wee.forward(Square_SizeG / 2)
                    wee.left(90)
                    wee.forward(Square_SizeG / 10)
                    wee.pencolor(color)
                    if continue_working == True and colors_list.index(color) != 0:
                        if Grid_Width > 10 or Grid_Height > 8:
                            wee.write(str(colors_list.index(color)), align = "center", font = ("Sans", int(Square_SizeG / 2), "bold"))
                        else:
                            wee.write(str(colors_list.index(color)), align = "center", font = ("Sans", int(Square_SizeG / 2), "normal"))
                    wee.backward(Square_SizeG / 10)
                    wee.right(90)
                    wee.backward(Square_SizeG / 2)
                    wee.pendown()
                    wee.pencolor("black")
                elif colors_list.index(color) == 9:
                    wee.pencolor("black")
                    wee.fillcolor("black")
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
                    if settings_list[5] == "old":
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

                    elif settings_list[5] == "new":
                        wee.penup()
                        wee.forward(1/6 * Square_SizeG)
                        wee.left(90)
                        wee.forward(1/8 * Square_SizeG)
                        wee.pendown()
                        wee.begin_fill()
                        wee.pensize(2)
                        wee.pencolor("black")
                        wee.fillcolor(colors_list[10])
                        wee.forward(3/4 * Square_SizeG)
                        wee.right(110.5555555555555555555555)
                        wee.forward(math.sqrt((1/4 * Square_SizeG)**2 + (2/3 * Square_SizeG)**2))
                        wee.right(138.8888888888888888888)
                        wee.forward(math.sqrt((1/4 * Square_SizeG)**2 + (2/3 * Square_SizeG)**2))
                        wee.end_fill()
                        wee_cards = Map_Wee(x, y)
                        wee.penup()
                        wee.goto(wee_cards[0], wee_cards[1])
                        wee.pendown()
                        wee.seth(0)
                        wee.pensize(1)
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

        def Fill_Square_Rainbow():
            if continue_working == True:
                if -1 < colors_list.index(color) < 9:
                    wee.pencolor("white")
                    wee.fillcolor("black")
                    wee.begin_fill()
                    sides_Checked = 0
                    Cx = 0
                    Cy = -1
                    Black_List = []
                    while sides_Checked < 4:
                        if Convert_to_Square_ID(x + Cx, y + Cy) != "null":
                            if Dig_List[Convert_to_Square_ID(x + Cx, y + Cy)] == "dug":
                                wee.pencolor("black")
                            else:
                                wee.pencolor("white")
                                Black_List.append(str(Cx) + str(Cy))
                        else:
                            wee.pencolor("white")
                            Black_List.append(str(Cx) + str(Cy))
                        wee.forward(Square_SizeG)
                        wee.left(90)
                        if Cy == -1:
                            Cy = 0
                            Cx = 1
                        elif Cx == 1:
                            Cy = 1
                            Cx = 0
                        elif Cy == 1:
                            Cy = 0
                            Cx = -1
                        sides_Checked = sides_Checked + 1
                    wee.end_fill()
                    wee_coordsF = Map_Wee(x ,y)
                    wee.pencolor("white")
                    wee.penup()
                    while len(Black_List) > 0:
                        if Black_List[0] == "0-1":
                            wee.goto(wee_coordsF[0],wee_coordsF[1])
                            wee.pendown()
                            wee.seth(0)
                        if Black_List[0] == "10":
                            wee.goto(wee_coordsF[0] + Square_SizeG,wee_coordsF[1])
                            wee.pendown()
                            wee.seth(90)
                        if Black_List[0] == "01":
                            wee.goto(wee_coordsF[0] + Square_SizeG,wee_coordsF[1] + Square_SizeG)
                            wee.pendown()
                            wee.seth(180)
                        if Black_List[0] == "-10":
                            wee.goto(wee_coordsF[0],wee_coordsF[1] + Square_SizeG)
                            wee.pendown()
                            wee.seth(270)
                        wee.forward(Square_SizeG)
                        wee.penup()
                        Black_List.pop(0)
                    wee.goto(wee_coordsF[0],wee_coordsF[1])
                    wee.seth(0)
                    wee.penup()
                    wee.forward(Square_SizeG / 2)
                    wee.left(90)
                    wee.forward(Square_SizeG / 10)
                    wee.pencolor(color)
                    if continue_working == True and colors_list.index(color) != 0:
                        if Grid_Width > 10 or Grid_Height > 8:
                            wee.write(str(colors_list.index(color)), align = "center", font = ("Sans", int(Square_SizeG / 2), "bold"))
                        else:
                            wee.write(str(colors_list.index(color)), align = "center", font = ("Sans", int(Square_SizeG / 2), "normal"))
                    wee.backward(Square_SizeG / 10)
                    wee.right(90)
                    wee.backward(Square_SizeG / 2)
                    wee.pendown()
                elif colors_list.index(color) == 9:
                    wee.pencolor("white")
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
                    if settings_list[5] == "old":
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

                    elif settings_list[5] == "new":
                        wee.penup()
                        wee.forward(1/6 * Square_SizeG)
                        wee.left(90)
                        wee.forward(1/8 * Square_SizeG)
                        wee.pendown()
                        wee.begin_fill()
                        wee.pensize(2)
                        wee.pencolor("black")
                        wee.fillcolor(colors_list[10])
                        wee.forward(3/4 * Square_SizeG)
                        wee.right(110.5555555555555555555555)
                        wee.forward(math.sqrt((1/4 * Square_SizeG)**2 + (2/3 * Square_SizeG)**2))
                        wee.right(138.8888888888888888888)
                        wee.forward(math.sqrt((1/4 * Square_SizeG)**2 + (2/3 * Square_SizeG)**2))
                        wee.end_fill()
                        wee_cards = Map_Wee(x, y)
                        wee.penup()
                        wee.goto(wee_cards[0], wee_cards[1])
                        wee.pendown()
                        wee.seth(0)
                        wee.pensize(1)
                elif colors_list.index(color) == 11:
                    wee.pencolor("white")
                    wee.fillcolor("white")
                    wee.begin_fill()
                    sides_Checked = 0
                    Cx = 0
                    Cy = -1
                    Black_List = []
                    while sides_Checked < 4:
                        if Convert_to_Square_ID(x + Cx, y + Cy) != "null":
                            if Dig_List[Convert_to_Square_ID(x + Cx, y + Cy)] == "dug":
                                if settings_list[5] == "old":
                                    if Flag_List[Convert_to_Square_ID(x + Cx, y + Cy)] == 1:
                                        wee.pencolor("white")
                                        Black_List.append(str(Cx) + str(Cy))
                                else:
                                    wee.pencolor("white")
                                    Black_List.append(str(Cx) + str(Cy))
                            else:
                                wee.pencolor("black")
                        else:
                            wee.pencolor("black")
                        wee.forward(Square_SizeG)
                        wee.left(90)
                        if Cy == -1:
                            Cy = 0
                            Cx = 1
                        elif Cx == 1:
                            Cy = 1
                            Cx = 0
                        elif Cy == 1:
                            Cy = 0
                            Cx = -1
                        sides_Checked = sides_Checked + 1
                    wee.end_fill()
                    wee_coordsF = Map_Wee(x ,y)
                    wee.pencolor("white")
                    wee.penup()
                    while len(Black_List) > 0:
                        if Black_List[0] == "0-1":
                            wee.goto(wee_coordsF[0],wee_coordsF[1])
                            wee.pendown()
                            wee.seth(0)
                        if Black_List[0] == "10":
                            wee.goto(wee_coordsF[0] + Square_SizeG,wee_coordsF[1])
                            wee.pendown()
                            wee.seth(90)
                        if Black_List[0] == "01":
                            wee.goto(wee_coordsF[0] + Square_SizeG,wee_coordsF[1] + Square_SizeG)
                            wee.pendown()
                            wee.seth(180)
                        if Black_List[0] == "-10":
                            wee.goto(wee_coordsF[0],wee_coordsF[1] + Square_SizeG)
                            wee.pendown()
                            wee.seth(270)
                        wee.forward(Square_SizeG)
                        wee.penup()
                        Black_List.pop(0)
                    wee.goto(wee_coordsF[0],wee_coordsF[1])
                    wee.seth(0)

        if settings_list[2] == "connected (new)":
            if settings_list[0] == "new" or settings_list[0] == "old" or settings_list[0] == "microsoft":
                Fill_Square_Regular()
            elif settings_list[0] == "rainbow":
                Fill_Square_Rainbow()
        elif settings_list[2] == "connected (old)":
            Fill_Square_Old()
        elif settings_list[2] == "unconnected":
            Fill_Square_Unconnected()

    if settings_list[6] == "enabled":
        Relative_loc = wee.ycor()

        Square_Siz = 35
        tree = turtle.Turtle()
        tree.hideturtle()
        tree.speed("fastest")
        if settings_list[5] == "new":
            tree.penup()
            tree.goto(-41, Relative_loc + 12)
            tree.forward(1/6 * Square_Siz)
            tree.left(90)
            tree.forward(1/8 * Square_Siz)
            tree.pendown()
            tree.begin_fill()
            tree.pensize(2)
            tree.pencolor("black")
            tree.fillcolor(colors_list[10])
            tree.forward(3/4 * Square_Siz)
            tree.right(110.5555555555555555555555)
            tree.forward(math.sqrt((1/4 * Square_Siz)**2 + (2/3 * Square_Siz)**2))
            tree.right(138.8888888888888888888)
            tree.forward(math.sqrt((1/4 * Square_Siz)**2 + (2/3 * Square_Siz)**2))
            tree.end_fill()
            tree.seth(0)
            tree.pensize(1)
        elif settings_list[5] == "old":
            tree.penup()
            tree.goto(-45, Relative_loc + 12)
            tree.pendown()
            if settings_list[0] == "rainbow":
                tree.pencolor("white")
            tree.fillcolor(colors_list[10])
            tree.begin_fill()
            tree.forward(Square_Siz)
            tree.left(90)
            tree.forward(Square_Siz)
            tree.left(90)
            tree.forward(Square_Siz)
            tree.left(90)
            tree.forward(Square_Siz)
            tree.left(90)
            tree.end_fill()
        tree.pencolor("white")
        tree.fillcolor("white")
        tree.penup()
        if Flag_Count > 1000:
            flag_locx = 34
        else:
            flag_locx = 25
        flag_locy = Relative_loc + 5.5

    # Failed Timer:

    # def Timer():
    #     global time
    #     tree.penup()
    #     tree.goto(flag_locx - 50, flag_locy + 25)
    #     tree.pendown()
    #     tree.begin_fill()
    #     tree.forward(100)
    #     tree.right(90)
    #     tree.forward(50)
    #     tree.right(90)
    #     tree.forward(100)
    #     tree.right(90)
    #     tree.forward(50)
    #     tree.right(90)
    #     tree.end_fill()
    #     tree.penup()
    #     tree.goto(flag_locx, flag_locy)
    #     tree.pencolor("black")
    #     tree.write(time, align= "center", font= ("Baloo Chettan 2", 14, "normal"))
    #     tree.pencolor("white")
    #     time = time + 1
    #     turtle.ontimer(Timer, 1000)

    # Timer()

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
                                Fill_Square(colors_list[10], "bruh", XcOd, YcOd)
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
                                Fill_Square("white", "bruh", XcOd, YcOd)
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
                                        Has_Player_WonG = Has_Player_WonG + 1 + Check_Neighboring_Squares2(Temp_XY[0],Temp_XY[1])
                                        Temp_Zero_List.pop(0)
                                elif Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
                                    wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                    wee.penup()
                                    wee.goto(wee_coords[0], wee_coords[1])
                                    wee.pendown()
                                    odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                    Fill_Square(colors_list[Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)]], odd_Or_even, X_coordinate, Y_coordinate)
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
        if settings_list[6] == "enabled":
            def Flag_Counter():
                tree.goto(flag_locx - 34, flag_locy + 55)
                tree.pendown()
                tree.begin_fill()
                tree.forward(80)
                tree.right(90)
                tree.forward(50)
                tree.right(90)
                tree.forward(80)
                tree.right(90)
                tree.forward(50)
                tree.right(90)
                tree.end_fill()
                tree.penup()
                tree.goto(flag_locx, flag_locy)
                tree.pencolor("black")
                tree.write(Flag_Count, align= "center", font= ("Baloo Chettan 2", 24, "normal"))
                tree.pencolor("white")

            Flag_Counter()

        def Player_Play_Again():

            weed = turtle.Turtle()
            weed.hideturtle()
            weed.speed("fastest")

            weed.penup()
            weed.goto(-151, 100)
            weed.pendown()
            weed.fillcolor("white")
            weed.begin_fill()
            weed.right(90)
            weed.forward(200)
            weed.left(90)
            weed.forward(302)
            weed.left(90)
            weed.forward(200)
            weed.left(90)
            weed.forward(302)
            weed.end_fill()

            weed.penup()
            weed.goto(0,40)
            weed.write("WOULD YOU LIKE", align="center", font=("Baloo Chettan 2", 18, "normal"))
            weed.goto(0,5)
            weed.write("TO PLAY AGAIN?", align="center", font=("Baloo Chettan 2", 18, "normal"))
            weed.goto(-116,-25)
            weed.pendown()
            weed.left(90)
            weed.forward(50)
            weed.left(90)
            weed.forward(100)
            weed.left(90)
            weed.forward(50)
            weed.left(90)
            weed.forward(100)
            weed.penup()
            weed.goto(-67,-60)
            weed.pencolor("green")
            weed.write("YES", align="center", font=("Baloo Chettan 2", 12, "normal"))
            weed.goto(17,-25)
            weed.pendown()
            weed.pencolor("black")
            weed.left(90)
            weed.forward(50)
            weed.left(90)
            weed.forward(100)
            weed.left(90)
            weed.forward(50)
            weed.left(90)
            weed.forward(100)
            weed.penup()
            weed.goto(67,-60)
            weed.pencolor("red")
            weed.write("NO", align="center", font=("Baloo Chettan 2", 12, "normal"))

        def Player_Won_Again():
            weed = turtle.Turtle()
            weed.hideturtle()
            weed.speed("fastest")

            weed.penup()
            weed.goto(-151, 100)
            weed.pendown()
            weed.fillcolor("white")
            weed.begin_fill()
            weed.right(90)
            weed.forward(200)
            weed.left(90)
            weed.forward(302)
            weed.left(90)
            weed.forward(200)
            weed.left(90)
            weed.forward(302)
            weed.end_fill()

            weed.penup()
            weed.goto(0,40)
            weed.write("YOU WON!!!", align="center", font=("Baloo Chettan 2", 18, "normal"))
            weed.goto(0,5)
            weed.write("PLAY AGAIN?", align="center", font=("Baloo Chettan 2", 18, "normal"))
            weed.goto(-116,-25)
            weed.pendown()
            weed.left(90)
            weed.forward(50)
            weed.left(90)
            weed.forward(100)
            weed.left(90)
            weed.forward(50)
            weed.left(90)
            weed.forward(100)
            weed.penup()
            weed.goto(-67,-60)
            weed.pencolor("green")
            weed.write("YES", align="center", font=("Baloo Chettan 2", 12, "normal"))
            weed.goto(17,-25)
            weed.pendown()
            weed.pencolor("black")
            weed.left(90)
            weed.forward(50)
            weed.left(90)
            weed.forward(100)
            weed.left(90)
            weed.forward(50)
            weed.left(90)
            weed.forward(100)
            weed.penup()
            weed.goto(67,-60)
            weed.pencolor("red")
            weed.write("NO", align="center", font=("Baloo Chettan 2", 12, "normal"))

        def TurtleClick(x, y):
            global Has_Player_WonG
            global Game_Over
            global turtle_drawing
            global show_win_message
            global Would_Play_Again
            global continue_working
            if turtle_drawing == False:
                if Game_Over == False:
                    Exit_Flag = 1
                    square_x = (x + ((Square_SizeG * Grid_Width) / 2)) / Square_SizeG + 1
                    square_y = (y + ((Square_SizeG * Grid_Height) / 2)) / Square_SizeG + 1

                    coordinate_list = [str(int(square_x)), str(int(square_y))]
                    X_coordinate = int(coordinate_list[0])
                    Y_coordinate = int(coordinate_list[1])
                    if Convert_to_Square_ID(X_coordinate, Y_coordinate) != "null":
                        if Flag_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 1:
                            Exit_Flag = 2
                        if Exit_Flag == 1:
                            if Dig_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == "bomb":
                                Game_Over = True
                                turtle_drawing = True
                                print("You failed! Game Over")
                                add_to_numba = 0
                                while add_to_numba < Total_Bombs:
                                    if continue_working == False: break
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
                                if continue_working == True:
                                    Player_Play_Again()
                                turtle_drawing = False
                            elif Dig_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == "dug": pass
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
                                    Has_Player_WonG = Has_Player_WonG + 1 + Check_Neighboring_Squares2(X_coordinate, Y_coordinate)
                                    while len(Temp_Zero_List) > 0:
                                        if continue_working == False: break
                                        Temp_XY = Convert_to_Coordinates(Temp_Zero_List[0])
                                        weeCoRdas = Map_Wee(Temp_XY[0],Temp_XY[1])
                                        wee.penup()
                                        wee.goto(weeCoRdas[0], weeCoRdas[1])
                                        wee.pendown()
                                        odd_Or_even4 = (Temp_XY[0] + Temp_XY[1]) % 2
                                        Fill_Square(colors_list[Box_List[Temp_Zero_List[0]]], odd_Or_even4, Temp_XY[0], Temp_XY[1])
                                        Dig_List[Temp_Zero_List[0]] = "dug"
                                        Flag_List[Temp_Zero_List[0]] = "dug"
                                        Has_Player_WonG = Has_Player_WonG + 1 + Check_Neighboring_Squares2(Temp_XY[0],Temp_XY[1])
                                        Temp_Zero_List.pop(0)
                                    turtle_drawing = False
                                elif Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)] == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
                                    turtle_drawing = True
                                    wee_coords = Map_Wee(X_coordinate, Y_coordinate)
                                    wee.penup()
                                    wee.goto(wee_coords[0], wee_coords[1])
                                    wee.pendown()
                                    odd_Or_even = (X_coordinate + Y_coordinate) % 2
                                    Fill_Square(colors_list[Box_List[Convert_to_Square_ID(X_coordinate, Y_coordinate)]], odd_Or_even, X_coordinate, Y_coordinate)
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
                    if -116 < x < -16:
                        if -75 < y < -25:
                            Would_Play_Again = 1
                            turtle.bye()
                    if 17 < x < 117:
                        if -75 < y < -25:
                            Would_Play_Again = 2
                            turtle.bye()
            else: pass
            if Has_Player_WonG == Win_VariableG and show_win_message == True:
                Player_Won_Again()
                Game_Over = True
                show_win_message = False

        def TurtleClick2(x, y):
            global Has_Player_WonG
            global Game_Over
            global turtle_drawing
            global Flag_Count
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
                            User_Input = "null"
                    else: User_Input = "null"
                    if User_Input != "null":
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
                                    Fill_Square(colors_list[10], "bruh", XcOd, YcOd)
                                    Flag_List[Convert_to_Square_ID(XcOd, YcOd)] = 1
                                    Flag_Count = Flag_Count - 1
                                    if settings_list[6] == "enabled":
                                        Flag_Counter()
                                    turtle_drawing = False
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
                                    Fill_Square("white", "bruh", XcOd, YcOd)
                                    Flag_List[Convert_to_Square_ID(XcOd, YcOd)] = 0
                                    Flag_Count = Flag_Count + 1
                                    if settings_list[6] == "enabled":
                                        Flag_Counter()
                                    turtle_drawing = False
            else: pass

        def Exit():
            global turtle_drawing
            global Game_Over
            global continue_working
            global Exit_Once
            if Exit_Once == False:
                wee.hideturtle()
                wee.penup()
                continue_working = False
                Player_Play_Again()
                turtle_drawing = False
                Game_Over = True
                Exit_Once = True
            else: pass

        while Game_Over == False:
            try:
                turtle.onscreenclick(TurtleClick)
                turtle.onscreenclick(TurtleClick2, btn= 3)
                turtle.onkey(Exit, "e")
                turtle.listen()
                turtle.mainloop()
            except turtle.Terminator: break
        turtle.done

    # Exit Loop for keyboard play
    if settings_list[3] == "off":
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
        read3 = input("Type anything here and press enter to continue: ")
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

def SettingsNew():
    global Draw_Settings_Menu

    turtle.TurtleScreen._RUNNING = True

    wheel = turtle.Turtle()
    wheel.hideturtle()
    wheel.speed("fastest")

    def Settings_Screen():
        global turtle_drawing
        if turtle_drawing == False:
            if Settings_Exit == False:
                wheel.penup()
                wheel.goto(-230, 240)
                wheel.pendown()
                wheel.goto(230, 240)
                wheel.goto(230, -240)
                wheel.goto(-230, -240)
                wheel.goto(-230, 240)
                wheel.penup()
                i = 0
                turtle_drawing = True
                for i in range (num_settings):
                    if continue_working == False: break
                    wheel.goto(-200, 240 - setting_width * (i + 1))
                    wheel.write(settings_list2[i], align= "left", font= ("Baloo Chettan 2", 18, "normal"))
                    wheel.goto(20, 240 - setting_width * (i + 1))
                    wheel.write("◀", align= "center", font= ("Baloo Chettan 2", 18, "normal"))
                    wheel.goto(105, 240 - setting_width * (i + 1))
                    if len(settings_list[i]) >= 11:
                        wheel.goto(105, 243 - setting_width * (i + 1))
                        wheel.write(settings_list[i], align= "center", font= ("Baloo Chettan 2", 14, "normal"))
                    else:
                        wheel.write(settings_list[i], align= "center", font= ("Baloo Chettan 2", 18, "normal"))
                    wheel.goto(190, 240 - setting_width * (i + 1))
                    wheel.write("▶", align= "center", font= ("Baloo Chettan 2", 18, "normal"))
                    i = i + 1
                turtle_drawing = False

    def GetCoordsSettings(x, y):
        global turtle_drawing
        if turtle_drawing == False:
            if Settings_Exit == False:
                turtle_drawing = True
                wheel.penup()
                wheel.pencolor("white")
                wheel.fillcolor("white")
                i2 = 0
                if 5 < x < 35:
                    while i2 < num_settings:
                        if (240 - (setting_width * (i2 + 1)) + 1) < y < (240 - (setting_width * (i2 + 1)) + 31):
                            Setting_Change = i2 + 1
                        i2 = i2 + 1
                elif 173 < x < 203:
                    while i2 < num_settings:
                        if (240 - (setting_width * (i2 + 1)) + 1) < y < (240 - (setting_width * (i2 + 1)) + 31):
                            Setting_Change = i2 + num_settings + 1
                        i2 = i2 + 1
                try:
                    if Setting_Change > num_settings:
                        Setting_Change = Setting_Change - num_settings
                        set_index = (settings_list_list[(Setting_Change - 1)]).index(settings_list[Setting_Change - 1])
                        if set_index + 2 > len(settings_list_list[(Setting_Change - 1)]):
                            set_index = -1
                        settings_list[Setting_Change - 1] = (settings_list_list[(Setting_Change - 1)])[set_index + 1]
                        list_change = Setting_Change - 1
                    elif Setting_Change <= num_settings:
                        set_index = (settings_list_list[(Setting_Change - 1)]).index(settings_list[Setting_Change - 1])
                        settings_list[Setting_Change - 1] = (settings_list_list[(Setting_Change - 1)])[set_index - 1]
                        list_change = Setting_Change - 1

                    wheel.goto(36, 240 - (setting_width * Setting_Change) + 31)
                    wheel.pendown()
                    wheel.begin_fill()
                    wheel.forward(136)
                    wheel.right(90)
                    wheel.forward(30)
                    wheel.right(90)
                    wheel.forward(136)
                    wheel.right(90)
                    wheel.forward(30)
                    wheel.right(90)
                    wheel.end_fill()
                    wheel.penup()
                    wheel.goto(105, 240 - (setting_width * Setting_Change))
                    wheel.pencolor("black")
                    if len(settings_list[list_change]) >= 11:
                        wheel.goto(105, 243 - (setting_width * Setting_Change))
                        wheel.write(settings_list[list_change], align= "center", font= ("Baloo Chettan 2", 14, "normal"))
                    else:
                        wheel.write(settings_list[list_change], align= "center", font= ("Baloo Chettan 2", 18, "normal"))
                except UnboundLocalError: pass
                turtle_drawing = False

    def Exit_Settings():
        global Settings_Exit
        global Draw_Menu
        global Draw_Settings_Menu
        global continue_working
        global turtle_drawing
        continue_working = False
        turtle_drawing = False
        Settings_Exit = True
        Draw_Menu = False
        Draw_Settings_Menu = False
        turtle.bye()

    while Settings_Exit == False:
        try:
            if Draw_Settings_Menu == False:
                Settings_Screen()
                Draw_Settings_Menu = True
            turtle.onscreenclick(GetCoordsSettings)
            turtle.onkey(Exit_Settings, "e")
            turtle.listen()
            turtle.mainloop()
        except turtle.Terminator: break

def SettingsOld():
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
            if connected_texture_on == "connected":
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
            if connected_texture_on == "connected":
                connected_texture_on = "normal"
            elif connected_texture_on == "normal":
                connected_texture_on = "connected"
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

def MainMenuScreen():

    turtle.TurtleScreen._RUNNING = True

    wheat = turtle.Turtle()
    wheat.hideturtle()
    wheat.speed("fastest")

    def CreateBox(x, y):
        wheat.penup()
        wheat.goto(x,y)
        wheat.pendown()
        wheat.right(90)
        wheat.forward(40)
        wheat.left(90)
        wheat.forward(200)
        wheat.left(90)
        wheat.forward(40)
        wheat.left(90)
        wheat.forward(200)
        wheat.right(180)

    CreateBox(-100, 130)
    wheat.penup()
    wheat.goto(0,98)
    wheat.write("PLAY", align="center", font=("Baloo Chettan 2", 12, "normal"))
    CreateBox(-100, 75)
    wheat.penup()
    wheat.goto(0,43)
    wheat.write("HELP", align="center", font=("Baloo Chettan 2", 12, "normal"))
    CreateBox(-100, 20)
    wheat.penup()
    wheat.goto(0,-12)
    wheat.write("CREDITS", align="center", font=("Baloo Chettan 2", 12, "normal"))
    CreateBox(-100, -35)
    wheat.penup()
    wheat.goto(0,-67)
    wheat.write("SETTINGS", align="center", font=("Baloo Chettan 2", 12, "normal"))
    CreateBox(-100, -90)
    wheat.penup()
    wheat.goto(0,-122)
    wheat.write("EXIT", align="center", font=("Baloo Chettan 2", 12, "normal"))

    wheat.penup()
    wheat.goto(0, 205)
    wheat.write("TURTLESWEEPER!", align="center", font=("Baloo Chettan 2", 30, "bold"))

# Main main loop
Help_Needed_Main = 0
Game_Exit = False
Main_Menu_Exit = False
Draw_Menu = False
while Game_Exit == False:
    if settings_list[3] == "on":
        def GetCoords(x, y):
            global settings_list
            global Game_Exit
            global Played_Once
            global Has_Player_WonG
            global Game_Over
            global Difficulty_Choose
            global Main_Menu_Exit
            global Draw_Menu
            global continue_working
            global Exit_Once
            global show_win_message
            global Settings_Exit
            global Flag_Count
            if -100 < x < 100:
                if 90 < y < 130:
                    Main_Input = "1"
                elif 35 < y < 75:
                    Main_Input = "2"
                elif -20 < y < 20:
                    Main_Input = "3"
                elif -75 < y < -35:
                    Main_Input = "4"
                elif -120 < y < -90:
                    Main_Input = "5"
                else:
                    Main_Input = "bigger bruh"
            try:
                if Main_Input == "1":
                    turtle.resetscreen()
                    Game_Finished = False
                    while Game_Finished == False:
                        Difficulty_Choose = False
                        continue_working = True
                        Exit_Once = False
                        show_win_message = True
                        Flag_Count = 0
                        Play()
                        Played_Once = True
                        if Would_Play_Again == 1:
                            Has_Player_WonG = 0
                            show_win_message = True
                            Game_Over = False
                        elif Would_Play_Again == 2:
                            Has_Player_WonG = 0
                            show_win_message = True
                            Game_Over = False
                            Game_Finished = True
                            Draw_Menu = False
                        else:
                            print("An error has occurred!")
                            print("Error Code: 1")
                            readinfinity = input("Type anything here and press enter to exit: ")
                            Game_Finished = True
                            Game_Exit = True
                elif Main_Input == "2":
                    Tutorial()
                elif Main_Input == "3":
                    Credits()
                elif Main_Input == "4":
                    turtle.resetscreen()
                    turtle.bye()
                    Settings_Exit = False
                    continue_working = True
                    SettingsNew()
                elif Main_Input == "5":
                    Game_Exit = True
                    Main_Menu_Exit = True
                    turtle.bye()
                elif Main_Input == "bigger bruh": pass
            except UnboundLocalError: pass

        while Main_Menu_Exit == False:
            try:
                if Draw_Menu == False:
                    turtle.setup(720, 675)
                    turtle.title("TurtleSweeper! - Version 1.4")
                    MainMenuScreen()
                    Draw_Menu = True
                turtle.onscreenclick(GetCoords)
                turtle.listen()
                turtle.mainloop()
            except turtle.Terminator: break

    elif settings_list[3] == "off":
        if Help_Needed_Main ==  0:
            if First_Intro_Done == True:
                print("TurtleSweeper!")
            elif First_Intro_Done == False:
                print("TurtleSweeper - v.1.4")
                print("Welcome to TurtleSweeper!")
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
            settings_list = SettingsOld()
        elif Main_Input == "5":
            Help_Needed_Main = 0
            Game_Exit = True
        else:
            Help_Needed_Main = 1