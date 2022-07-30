def maker(input, currentGrid):
    if input[0] + input[1] + input[2] + input[3] + input[4] == "grid:":
        currentGrid = gridMaker() #make a grid and have it return the grid to place things into (give a name too)
    elif input[0] + input[1] + input[2] + input[3] + input[4] + input[5] == "label:":
        labelMaker(input[6:], currentGrid) #add to current grid which is either the grid most recently created or its
    elif input[0] + input[1] + input[2] + input[3] + input[4] + input[5] + input[6] + input[7] == "textbox:":
        textboxMaker(input[8:], currentGrid)
    elif input[0] + input[1] + input[2] + input[3] + input[4] + input[5] + input[6] + input[7] + input[8] == "checkbox:":
        checkboxMaker(input[9:], currentGrid)
    elif input[0] + input[1] + input[2] + input[3] + input[4] + input[5] + input[6] == "button:":
        buttonMaker(input[7:])
    elif input[0] + input[1] + input[2] + input[3] + input[4] + input[5] + input[6] + input[7] + input[8] + input[9] + input[10] == "quadtoggle:":
        quadtoggleMaker(input[11:])
    elif input[0] + input[1] + input[2] + input[3] == "bod:":
        bodMaker(input[4:])

def gridPlacer(input):
    if input[0] + input[1] + input[2] == "p1:":
        input = input[3:]
