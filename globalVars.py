# \033[  m
# 90 - Gray
# 91 - Red
# 92 - Green
# 93 - Yellow
# 94 - Blue
# 95 - Pink
# 96 - Cyan
# 97 - White

import os

logoBattleShip = "\033[97m██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗  ░██████╗██╗░░██╗██╗██████╗░\n██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝  ██╔════╝██║░░██║██║██╔══██╗\n██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░  ╚█████╗░███████║██║██████╔╝\n██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░  ░╚═══██╗██╔══██║██║██╔═══╝░\n██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗  ██████╔╝██║░░██║██║██║░░░░░\n╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝  ╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░\n\033[97m                  Made by \033[91mGabi\033[97m (https://github.com/GabbaTK)\n\033[97m"
logoBattleShipDev = "\033[97m██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗  ░██████╗██╗░░██╗██╗██████╗░\n██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝  ██╔════╝██║░░██║██║██╔══██╗\n██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░  ╚█████╗░███████║██║██████╔╝\n██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░  ░╚═══██╗██╔══██║██║██╔═══╝░\n██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗  ██████╔╝██║░░██║██║██║░░░░░\n╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝  ╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░\n\033[97m                  Made by \033[91mGabi\033[97m (https://github.com/GabbaTK)\n\033[90m                                                                    ──╔╗──────────────╔╗\n                                                                    ──║║──────────────║║\n                                                                    ╔═╝╠══╦╗╔╗╔╗╔╦══╦═╝╠══╗\n                                                                    ║╔╗║║═╣╚╝║║╚╝║╔╗║╔╗║║═╣\n                                                                    ║╚╝║║═╬╗╔╝║║║║╚╝║╚╝║║═╣\n                                                                    ╚══╩══╝╚╝─╚╩╩╩══╩══╩══╝\n\033[97m"
boardHit = "\033[97m██╗░░██╗██╗████████╗  ██████╗░░█████╗░░█████╗░██████╗░██████╗░\n██║░░██║██║╚══██╔══╝  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗\n███████║██║░░░██║░░░  ██████╦╝██║░░██║███████║██████╔╝██║░░██║\n██╔══██║██║░░░██║░░░  ██╔══██╗██║░░██║██╔══██║██╔══██╗██║░░██║\n██║░░██║██║░░░██║░░░  ██████╦╝╚█████╔╝██║░░██║██║░░██║██████╔╝\n╚═╝░░╚═╝╚═╝░░░╚═╝░░░  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░\n"
boardPosition = "\033[97m██████╗░░█████╗░░██████╗██╗████████╗██╗░█████╗░███╗░░██╗  ██████╗░░█████╗░░█████╗░██████╗░██████╗░\n██╔══██╗██╔══██╗██╔════╝██║╚══██╔══╝██║██╔══██╗████╗░██║  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗\n██████╔╝██║░░██║╚█████╗░██║░░░██║░░░██║██║░░██║██╔██╗██║  ██████╦╝██║░░██║███████║██████╔╝██║░░██║\n██╔═══╝░██║░░██║░╚═══██╗██║░░░██║░░░██║██║░░██║██║╚████║  ██╔══██╗██║░░██║██╔══██║██╔══██╗██║░░██║\n██║░░░░░╚█████╔╝██████╔╝██║░░░██║░░░██║╚█████╔╝██║░╚███║  ██████╦╝╚█████╔╝██║░░██║██║░░██║██████╔╝\n╚═╝░░░░░░╚════╝░╚═════╝░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░\n"
boardOtherPlayerPosition = "\033[97m░█████╗░████████╗██╗░░██╗███████╗██████╗░  ██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░░██████╗ ██████╗░░█████╗░░█████╗░██████╗░██████╗░\n██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗\n██║░░██║░░░██║░░░███████║█████╗░░██████╔╝  ██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝╚█████╗░ ██████╦╝██║░░██║███████║██████╔╝██║░░██║\n██║░░██║░░░██║░░░██╔══██║██╔══╝░░██╔══██╗  ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗░╚═══██╗ ██╔══██╗██║░░██║██╔══██║██╔══██╗██║░░██║\n╚█████╔╝░░░██║░░░██║░░██║███████╗██║░░██║  ██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║██████╔╝ ██████╦╝╚█████╔╝██║░░██║██║░░██║██████╔╝\n░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░ ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░\n"
letterSet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
logoHit = "\033[91m█░█ █ ▀█▀\n█▀█ █ ░█░\033[97m"
LogoMiss = "\033[91m█▀▄▀█ █ █▀ █▀\n█░▀░█ █ ▄█ ▄█\033[97m"
opponentHitYou = "\033[91m▀▀█▀▀ ▒█░▒█ ▒█▀▀▀ 　 ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▒█▄░▒█ ▒█▀▀▀ ▒█▄░▒█ ▀▀█▀▀ 　 ▒█░▒█ ▀█▀ ▀▀█▀▀ 　 ▒█░░▒█ ▒█▀▀▀█ ▒█░▒█\n░▒█░░ ▒█▀▀█ ▒█▀▀▀ 　 ▒█░░▒█ ▒█▄▄█ ▒█▄▄█ ▒█░░▒█ ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ░▒█░░ 　 ▒█▀▀█ ▒█░ ░▒█░░ 　 ▒█▄▄▄█ ▒█░░▒█ ▒█░▒█\n░▒█░░ ▒█░▒█ ▒█▄▄▄ 　 ▒█▄▄▄█ ▒█░░░ ▒█░░░ ▒█▄▄▄█ ▒█░░▀█ ▒█▄▄▄ ▒█░░▀█ ░▒█░░ 　 ▒█░▒█ ▄█▄ ░▒█░░ 　 ░░▒█░░ ▒█▄▄▄█ ░▀▄▄▀\033[97m"
youWin = "\033[97m██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗\n╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║\n░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║\n░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║\n░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║\n░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝"
youLose = "\033[97m██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗\n╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝\n░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░\n░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░\n░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗\n░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝"
enemyShipDestroyed = "\033[91m█▀▀ █▄░█ █▀▀ █▀▄▀█ █▄█   █▀ █░█ █ █▀█   █▀▄ █▀▀ █▀ ▀█▀ █▀█ █▀█ █▄█ █▀▀ █▀▄\n██▄ █░▀█ ██▄ █░▀░█ ░█░   ▄█ █▀█ █ █▀▀   █▄▀ ██▄ ▄█ ░█░ █▀▄ █▄█ ░█░ ██▄ █▄▀"

def funcCall(func):
    return func()

def printBoardPosition(board, prntLogo, otherPlayersBoard=False):
    if prntLogo and not otherPlayersBoard:
        print(boardPosition)
    if prntLogo and otherPlayersBoard:
        print(boardOtherPlayerPosition)

    print("    1   2   3   4   5   6   7   8   9   10")
    print("  -----------------------------------------")
    for line in range(10):
        print(f"{letterSet[line]} | ", end="")
        for square in range(10):
            colorPrint = board[line][square]

            if board[line][square] == "+":
                colorPrint = "\033[34m+\033[97m"
            elif board[line][square] == "X":
                colorPrint = "\033[31mX\033[97m"

            print(f"{colorPrint} | ", end="")
        print()
        print("  -----------------------------------------")

def printBoardHit(board, prntLogo):
    if prntLogo:
        print(boardHit)

    print("    1   2   3   4   5   6   7   8   9   10")
    print("  -----------------------------------------")
    for line in range(10):
        print(f"{letterSet[line]} | ", end="")
        for square in range(10):
            colorPrint = board[line][square]

            if board[line][square] == "X":
                colorPrint = "\033[31mX\033[97m"

            print(f"{colorPrint} | ", end="")
        print()
        print("  -----------------------------------------")

def intListToStrList(intList):
    strList = []

    for item in intList:
        strList.append(str(item))

    return strList

def setupShips(board):
    shipCoords = {"4": [], "3": [], "2": [], "1": []}
    shipsLeft = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    while len(shipsLeft) > 0:       
        printBoardPosition(board, False)
        print(f"You have ships of lenght (\033[91m{' '.join(intListToStrList(shipsLeft))}\033[97m) to be placed, place the starting and ending points seperated by a '-'")

        position = input(">")
        position = position.upper()
        position = position.split("-")
        position[0] = [position[0][0], position[0][1:]]
        if len(position) == 2:
            position[1] = [position[1][0], position[1][1:]]

        #if len(position) == 2:
        #    if 0 < int(position[0][1]) < 11 and 0 < int(position[1][1]) < 11:
        #        pass
        #    else:
        #        print("\033[91mThat is an invalid position, please check your ship lenght and/or position\033[97m")
        #else:
        #    if 0 < int(position[0][1]) < 11:
        #        pass
        #    else:
        #        print("\033[91mThat is an invalid position, please check your ship lenght and/or position\033[97m")

        if len(position) == 1:
            os.system("cls")

            position.append(position[0])
            success = ssPlotShips(position, 1, board)

            if success:
                shipsLeft.remove(1)
                shipCoords["1"].append(position[0])

            continue

        leftRightShipLenght = int(position[1][1]) - int(position[0][1]) + 1
        topBottopShipLenght = letterSet.index(position[1][0]) - letterSet.index(position[0][0]) + 1

        if leftRightShipLenght != 1:
            if leftRightShipLenght in shipsLeft:
                success = ssPlotShips(position, leftRightShipLenght, board)

                if success:
                    shipsLeft.remove(leftRightShipLenght)

                    shipCoords[str(leftRightShipLenght)].append([])
                    for point in range(int(position[0][1]), int(position[1][1])):
                        shipCoords[str(leftRightShipLenght)][-1].append(position[0][0] + str(point))
                    shipCoords[str(leftRightShipLenght)][-1].append(position[1])
            else:
                print("\033[91mThat is an invalid position, please check your ship lenght and/or position\033[97m")
        elif topBottopShipLenght != 1:
            if topBottopShipLenght in shipsLeft:
                success = ssPlotShips(position, topBottopShipLenght, board)

                if success:
                    shipsLeft.remove(topBottopShipLenght)

                    shipCoords[str(topBottopShipLenght)].append([])
                    for point in range(letterSet.index(position[0][0]), letterSet.index(position[1][0])):
                        shipCoords[str(topBottopShipLenght)][-1].append(letterSet[point] + str(position[0][1]))
                    shipCoords[str(topBottopShipLenght)][-1].append(position[1])
            else:
                print("\033[91mThat is an invalid position, please check your ship lenght and/or position\033[97m")

        os.system("cls")

    return board, shipCoords

def ssPlotShips(position, shipLenght, board):
    if position[0][0] == position[1][0]:
        if int(position[1][1]) - (shipLenght - 1) == int(position[0][1]):
            #alreadyPlaced = False
            #for shipX in range(int(position[0][1]), int(position[1][1]) + 1):
            #    if board[letterSet.index(position[0][0])][shipX - 1] == "+":
            #        alreadyPlaced = True

            if not ssNoShipClose(board, [letterSet.index(position[0][0]), int(position[0][1]) - 1], shipLenght, "h"):
                print("\033[91mThat is an invalid position, please check your ship lenght and/or position\033[97m")
                return False

            for shipX in range(int(position[0][1]), int(position[1][1]) + 1):
                board[letterSet.index(position[0][0])][shipX - 1] = "+"
            return True
        else:
            print("\033[91mThat is an invalid position, please check your ship lenght and/or position\033[97m")
            return False
    elif position[0][1] == position[1][1]:
        if letterSet.index(position[1][0]) - (shipLenght - 1) == letterSet.index(position[0][0]):
            #alreadyPlaced = False
            #for shipY in range(int(position[0][1]), int(position[1][1]) + 1):
            #    if board[shipY][int(position[0][1]) - 1] == "+":
            #        alreadyPlaced = True

            if not ssNoShipClose(board, [letterSet.index(position[0][0]), int(position[0][1]) - 1], shipLenght, "v"):
                print("\033[91mThat is an invalid position, please check your ship lenght and/or position\033[97m")
                return False
        
            for shipY in range(letterSet.index(position[0][0]), letterSet.index(position[1][0]) + 1):
                board[shipY][int(position[0][1]) - 1] = "+"
            return True
        else:
            print("\033[91mThat is an invalid position, please check your ship lenght and/or position\033[97m")
            return False
    else:
        print("\033[91mThat is an invalid position, please check your ship lenght and/or position\033[97m")
        return False

def ssNoShipClose(board, org, lenght, rotation):
    if rotation == "h":
        shipInRange = False
        for y in range(org[0] - 1, org[0] + 2):
            if shipInRange:
                return not shipInRange

            for x in range(org[1] - 1, org[1] + lenght + 1):

                if -1 < x < 10 and -1 < y < 10:
                    if board[y][x] == "+":
                        shipInRange = True
                        break

        return not shipInRange
    
    elif rotation == "v":
        shipInRange = False
        for y in range(org[0] - 1, org[0] + lenght + 1):
            if shipInRange:
                return not shipInRange

            for x in range(org[1] - 1, org[1] + 2):

                if -1 < x < 10 and -1 < y < 10:
                    if board[y][x] == "+":
                        shipInRange = True
                        break

        return not shipInRange

def shipDestroyedSurroundBlank(board, org, lenght, rotation):
    if rotation == "h":
        for y in range(org[0] - 1, org[0] + 2):
            for x in range(org[1] - 1, org[1] + lenght + 1):
                if -1 < x < 10 and -1 < y < 10:
                    if board[y][x] != "X":
                        board[y][x] = "#"
    
    elif rotation == "v":
        for y in range(org[0] - 1, org[0] + lenght + 1):
            for x in range(org[1] - 1, org[1] + 2):
                if -1 < x < 10 and -1 < y < 10:
                    if board[y][x] != "X":
                        board[y][x] = "#"

    return board

def checkGameWon(board):
    notWon = False
    for y in board:
        for x in y:
            if x == "+":
                notWon = True

    return not notWon
