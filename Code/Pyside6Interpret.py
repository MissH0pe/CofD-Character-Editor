#currently using @ to separate grid sections and : to separate element sections with @!!! to separate those sections



def maker(input, currentGrid):
    if input[0] + input[1] + input[2] + input[3] + input[4] == "grid:":
        gridMaker() #make a grid to place things into (give a name too)
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

def gridPlacer(input, parentGrid): #store the names of children grids in an dictionary (that links to the dict) in each grid also store the parent grid of each grid
    strings = input.split("@")
    for k in range(len(strings)):
        if strings[k] in parentGrid.childGrids:
            parentGrid = parentGrid.childGrids[strings[k]]
        elif strings[k][0] + strings[k][1] + strings[k][2] == "!!!":
            strings2 = input.split("!!!")
            maker(strings2[1], parentGrid)
        else:
            print("GNFE1: grid not found to place element in in line: " + input)






    # if input[0] + input[1] + input[2] == "p1@":
    #     input = input[3:]
