import connectionManager
import globalVars
import os
import time
import copy

playerPositionBoard = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
playerHitBoard = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
letterSet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
shipCoords = {}
warning = """\033[91m
░██╗░░░░░░░██╗░█████╗░██████╗░███╗░░██╗██╗███╗░░██╗░██████╗░
░██║░░██╗░░██║██╔══██╗██╔══██╗████╗░██║██║████╗░██║██╔════╝░
░╚██╗████╗██╔╝███████║██████╔╝██╔██╗██║██║██╔██╗██║██║░░██╗░
░░████╔═████║░██╔══██║██╔══██╗██║╚████║██║██║╚████║██║░░╚██╗
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║██║░╚███║██║██║░╚███║╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░


The server is running in developer mode, statistic data will
be transmitted to the server! Join with caution!

Are you sure you want to join (y/n)\033[97m"""

def funcCall(func):
    return func()

def sendTable():
    convertedTable = ""

    for line in playerPositionBoard:
        convertedTable += "".join(line)
        convertedTable += "-"

    return convertedTable

def sendShipsData():
    convertedShips = ""

    for shipLenght in shipCoords:
        for ship in shipCoords[shipLenght]:
            convertedShips += "_".join(ship)
            convertedShips += "-"
        convertedShips += ":"

    return convertedShips

def setupShips():
    global playerPositionBoard

    returnBoard, returnCoords = globalVars.setupShips(playerPositionBoard)
    playerPositionBoard = returnBoard

    return returnBoard, returnCoords

def init(defaultShipPosition):
    global playerPositionBoard
    global boardHitText
    global boardPositionText
    global shipCoords
    global shipCoordsOrg

    os.system("cls")

    logoBattleShip = globalVars.logoBattleShip
    boardHitText = globalVars.boardHit
    boardPositionText = globalVars.boardPosition

    print(logoBattleShip)

    print("Enter the ip or pc name of the server to connect to")
    ip = input(">")

    connectionManager.connect(ip, 10800)

    os.system("cls")

    serverDevMode = connectionManager.clientReceiveData()
    if serverDevMode == "CONN_DEV_TRUE":
        print(warning)
        joinConfirm = input(">")

        if joinConfirm == "y":
            connectionManager.clientSendData("CONN_DEV_ACC")
        else:
            connectionManager.clientSendData("CONN_DEV_DEN")
            print("Connection terminated")
            exit()
    elif serverDevMode == "CONN_DEV_FALSE":
        connectionManager.clientSendData("CONN_DEV_ACC")
    else:
        print("There has been an error trying to connect to the server")
        exit()

    os.system("cls")

    print("\033[97mGame is starting \033[96msoon\033[97m")
    time.sleep(5)

    os.system("cls")

    if defaultShipPosition == "Disable":
        playerPositionBoard = [["+", " ", "+", " ", "+", " ", "+", " ", " ", " "],
                               ["+", " ", "+", " ", "+", " ", "+", " ", " ", " "],
                               ["+", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                               ["+", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                               ["+", " ", "+", " ", " ", " ", " ", " ", " ", " "],
                               ["+", " ", "+", " ", " ", " ", " ", " ", " ", " "],
                               ["+", " ", "+", " ", " ", " ", " ", " ", " ", " "],
                               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                               ["+", " ", "+", " ", "+", " ", "+", " ", " ", " "]]
        shipCoords = {"4": [["A1", "B1", "C1", "D1"]], "3": [["F1", "G1", "H1"], ["F3", "G3", "H3"]], "2": [["A3", "B3"], ["A5", "B5"], ["A7", "B7"]], "1": [["J1"], ["J3"], ["J5"], ["J7"]]}
        shipCoordsOrg = {"4": [["A1", "B1", "C1", "D1"]], "3": [["F1", "G1", "H1"], ["F3", "G3", "H3"]], "2": [["A3", "B3"], ["A5", "B5"], ["A7", "B7"]], "1": [["J1"], ["J3"], ["J5"], ["J7"]]}
    else:
        playerPositionBoard, shipCoords = setupShips()
        shipCoordsOrg = copy.deepcopy(shipCoords)

    print("Waiting for ther person...")
    connectionManager.requestSyncC()

    os.system("cls")

    globalVars.printBoardHit(playerHitBoard, True)
    print()
    globalVars.printBoardPosition(playerPositionBoard, True)

    gameLoop()

def gameLoop():
    global playerHitBoard

    while True:
        #os.system("cls")

        #globalVars.printBoardHit(playerHitBoard, True)
        #print()
        #globalVars.printBoardPosition(playerPositionBoard, True)

        data = connectionManager.clientReceiveData()

        if data == "DEV_STAT_BOARD":
            connectionManager.clientSendData(sendTable())
        elif data == "DEV_STAT_SHIPS":
            connectionManager.clientSendData(sendShipsData())
        elif data.startswith("SHOOT_TEST"):
            data = data.split("_")

            shootPoint = data[-1]
            shootPoint = list(shootPoint)
            shootPoint = [int(shootPoint[0]), int(shootPoint[1])]

            if playerPositionBoard[shootPoint[0]][shootPoint[1]] == "+":
                os.system("cls")

                playerPositionBoard[shootPoint[0]][shootPoint[1]] = "X"

                print(globalVars.opponentHitYou)
                print()
                globalVars.printBoardPosition(playerPositionBoard, False)

                coordsShootPoint = letterSet[shootPoint[0]] + str(shootPoint[1] + 1)
                shipDestroyed = "SHOOT_SHIP_NDEST"
                for shipLenght in shipCoords:
                    for shipIndex, ship in enumerate(shipCoords[shipLenght]):
                        if coordsShootPoint in ship:
                            shipCoords[shipLenght][shipIndex].remove(coordsShootPoint)

                            if len(shipCoords[shipLenght][shipIndex]) == 0:
                                gameWon = globalVars.checkGameWon(playerPositionBoard)
                                if gameWon:
                                    connectionManager.clientSendData("SHOOT_ACK_HIT")
                                    connectionManager.clientSendData("GAME_WIN")
                                    os.system("cls")
                                    print(globalVars.youLose)
                                    exit()
                                else:
                                    orgShootPoint = [str(letterSet.index(shipCoordsOrg[shipLenght][shipIndex][0][0])), str(int(shipCoordsOrg[shipLenght][shipIndex][0][1]) - 1)]
                                    if shipLenght == "1":
                                        shipRotation = "h"
                                    elif shipCoordsOrg[shipLenght][shipIndex][0][0] == shipCoordsOrg[shipLenght][shipIndex][1][0]:
                                        shipRotation = "h"
                                    elif shipCoordsOrg[shipLenght][shipIndex][0][1] == shipCoordsOrg[shipLenght][shipIndex][1][1]:
                                        shipRotation = "v"
                                    shipDestroyed = f"SHOOT_SHIP_DEST_{''.join(orgShootPoint)}_{shipLenght}_{shipRotation}"

                connectionManager.clientSendData("SHOOT_ACK_HIT")
                connectionManager.clientSendData(shipDestroyed)

            elif playerPositionBoard[shootPoint[0]][shootPoint[1]] == "X":
                os.system("cls")

                print(globalVars.opponentHitYou)
                print()
                globalVars.printBoardPosition(playerPositionBoard, False)

                connectionManager.clientSendData("SHOOT_ACK_HIT")
                connectionManager.clientSendData("SHOOT_SHIP_NDEST")

            elif playerPositionBoard[shootPoint[0]][shootPoint[1]] == "#":
                connectionManager.clientSendData("SHOOT_ACK_MISS")
                connectionManager.clientSendData("SHOOT_SHIP_NDEST")

            elif playerPositionBoard[shootPoint[0]][shootPoint[1]] == " ":
                playerPositionBoard[shootPoint[0]][shootPoint[1]] = "#"

                connectionManager.clientSendData("SHOOT_ACK_MISS")
                connectionManager.clientSendData("SHOOT_SHIP_NDEST")
        elif data == "SHOOT_TURN_NEXT":
            os.system("cls")

            while True:
                globalVars.printBoardHit(playerHitBoard, True)
                print()
                globalVars.printBoardPosition(playerPositionBoard, True)
                print("Where do you want to shoot")
                hitPosition = input(">")
                hitPosition = hitPosition.upper()

                shootPoint = list(hitPosition)
                shootPoint = [shootPoint[0], int("".join(shootPoint[1:]))]
                shootPoint = [letterSet.index(shootPoint[0]), shootPoint[1] - 1]

                connectionManager.clientSendData(f"SHOOT_TEST_{str(shootPoint[0]) + str(shootPoint[1])}")
                hitMiss = connectionManager.clientReceiveData()
                shipDestroyed = connectionManager.clientReceiveData()

                if shipDestroyed == "GAME_WIN":
                    os.system("cls")
                    print(globalVars.youWin)
                    exit()

                if hitMiss == "SHOOT_ACK_HIT":
                    os.system("cls")

                    playerHitBoard[shootPoint[0]][shootPoint[1]] = "X"

                    print(globalVars.logoHit)
                    print()

                    if shipDestroyed.startswith("SHOOT_SHIP_DEST"):
                        shipDestroyed = shipDestroyed.split("_")
                        destroyedShipOrg = shipDestroyed[3]
                        destroyedShipOrg = list(destroyedShipOrg)
                        destroyedShipOrg = [int(destroyedShipOrg[0]), int(destroyedShipOrg[1])]
                        destroyedShipLength = shipDestroyed[4]
                        destroyedShipLength = int(destroyedShipLength)
                        destroyedShipRotation = shipDestroyed[5]

                        print(globalVars.enemyShipDestroyed)
                        print()

                        playerHitBoard = globalVars.shipDestroyedSurroundBlank(playerHitBoard, destroyedShipOrg, destroyedShipLength, destroyedShipRotation)
                elif hitMiss == "SHOOT_ACK_MISS":
                    os.system("cls")

                    playerHitBoard[shootPoint[0]][shootPoint[1]] = "#"

                    print(globalVars.LogoMiss)
                    print()
                    globalVars.printBoardHit(playerHitBoard, True)
                    print()
                    globalVars.printBoardPosition(playerPositionBoard, True)

                    connectionManager.clientSendData("SHOOT_TURN_NEXT")
                    break

if __name__ == "__main__":
    init()
