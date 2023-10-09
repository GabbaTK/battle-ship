import connectionManager
import globalVars
import os
import time

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
piecesLeft = {"4":1,
              "3":2,
              "2":3,
              "1":4}
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

def setupShips():
    global playerPositionBoard

    returnBoard = globalVars.setupShips(playerPositionBoard)
    playerPositionBoard = returnBoard

def init(defaultShipPosition):
    global playerPositionBoard
    global boardHitText
    global boardPositionText

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
    else:
        playerPositionBoard, shipCoords = setupShips()

    print("Waiting for ther person...")
    connectionManager.requestSyncC()

    os.system("cls")

    globalVars.printBoardHit(playerHitBoard, True)
    print()
    globalVars.printBoardPosition(playerPositionBoard, True)

    gameLoop()

def gameLoop():
    while True:
        data = connectionManager.clientReceiveData()

        if data == "DEV_STAT_BOARD":
            connectionManager.clientSendData(sendTable())
        elif data.startswith("SHOOT_TEST"):
            data = data.split("_")

            shootPoint = data[-1]
            shootPoint = list(shootPoint)
            shootPoint = [int(shootPoint[0]), int(shootPoint[1])]

            if playerPositionBoard[shootPoint[0]][shootPoint[1]] == "+":
                playerPositionBoard[shootPoint[0]][shootPoint[1]] = "X"

                connectionManager.clientSendData("SHOOT_ACK_HIT")

            elif playerPositionBoard[shootPoint[0]][shootPoint[1]] == "X":
                connectionManager.clientSendData("SHOOT_ACK_HIT")

            elif playerPositionBoard[shootPoint[0]][shootPoint[1]] == "#":
                connectionManager.clientSendData("SHOOT_ACK_MISS")

            elif playerPositionBoard[shootPoint[0]][shootPoint[1]] == " ":
                playerPositionBoard[shootPoint[0]][shootPoint[1]] = "#"

                connectionManager.clientSendData("SHOOT_ACK_MISS")
        elif data == "SHOOT_TURN_NEXT":
            os.system("cls")

            globalVars.printBoardHit(playerHitBoard, True)
            print()
            globalVars.printBoardPosition(playerPositionBoard, True)
            print("Where do you want to shoot")
            hitPosition = input(">")
            hitPosition = hitPosition.upper()

            shootPoint = list(hitPosition)
            shootPoint = [shootPoint[0], int("".join(shootPoint[1:]))]
            shootPoint = [letterSet.index(shootPoint[0]), shootPoint[1] - 1]

            connectionManager.clientSendData(f"SHOOT_TEST_{str(hitPosition[0]) + str(hitPosition[1])}")
            hitMiss = connectionManager.clientReceiveData()

            if hitMiss == "SHOOT_ACK_HIT":
                playerHitBoard[shootPoint[0]][shootPoint[1]] = "X"
            elif hitMiss == "SHOOT_ACK_MISS":
                playerHitBoard[shootPoint[0]][shootPoint[1]] = "#"

if __name__ == "__main__":
    init()
