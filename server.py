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
serverPositionBoard = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
serverHitBoard = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
shipCoords = {}
letterSet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def funcCall(func):
    return func()

def tableDataToTable(formatedData):
    convertedTable = []

    formatedData = formatedData.split("-")
    for line in formatedData:
        convertedTable.append(list(line))

    return convertedTable

def setupShips():
    global serverPositionBoard

    returnBoard, returnCoords = globalVars.setupShips(serverPositionBoard)
    serverPositionBoard = returnBoard

    return returnBoard, returnCoords

def init(dev, defaultShipPosition):
    global serverPositionBoard
    global boardHitText
    global boardPositionText
    global shipCoords

    os.system("cls")

    logoBattleShip = globalVars.logoBattleShip
    logoBattleShipDev = globalVars.logoBattleShipDev
    boardHitText = globalVars.boardHit
    boardPositionText = globalVars.boardPosition

    if not dev:
        print(logoBattleShip)
    else:
        print(logoBattleShipDev)
    print(f"Awaiting connection from player on: {connectionManager.hostName()} / {connectionManager.hostIp()}")

    playerConnection, address = connectionManager.awaitConnection(10800)

    connectionManager.serverSendData(playerConnection, f"CONN_DEV_{str(dev).upper()}")

    print("Joining in progress...")

    clientJoinConfirmation = connectionManager.serverReceiveData(playerConnection)

    if clientJoinConfirmation == "CONN_DEV_DEN":
        print("Player has denied joining this server, maybe because you are running in developer mode")
        exit()

    print(f"New connection for {address[0]}")
    print("\033[97mGame is starting \033[96msoon\033[97m")
    time.sleep(5)

    os.system("cls")

    if defaultShipPosition == "Disable":
        serverPositionBoard = [["+", " ", "+", " ", "+", " ", "+", " ", " ", " "],
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
    else:
        serverPositionBoard, shipCoords = setupShips()

    print("Waiting for ther person...")
    connectionManager.requestSyncS(playerConnection)

    gameLoop(dev, playerConnection)

def gameLoop(dev, playerConnection):
    while True:
        os.system("cls")

        while True:
            if dev:
                connectionManager.serverSendData(playerConnection, "DEV_STAT_BOARD")
                formatedPlayerPositionBoard = connectionManager.serverReceiveData(playerConnection)
                playerPositionBoard = tableDataToTable(formatedPlayerPositionBoard)
                connectionManager.serverSendData(playerConnection, "DEV_STAT_SHIPS")
                enemyShipsLeft = connectionManager.serverReceiveData(playerConnection)

                globalVars.printBoardPosition(playerPositionBoard, True, True)
                print()

            globalVars.printBoardHit(serverHitBoard, True)
            print()
            globalVars.printBoardPosition(serverPositionBoard, True)
            print("Where do you want to shoot")
            hitPosition = input(">")
            hitPosition = hitPosition.upper()

            shootPoint = list(hitPosition)
            shootPoint = [shootPoint[0], int("".join(shootPoint[1:]))]
            shootPoint = [letterSet.index(shootPoint[0]), shootPoint[1] - 1]
            
            connectionManager.serverSendData(playerConnection, f"SHOOT_TEST_{str(shootPoint[0]) + str(shootPoint[1])}")
            hitMiss = connectionManager.serverReceiveData(playerConnection)
            shipDestroyed = connectionManager.serverReceiveData(playerConnection)

            os.system("cls")
            
            if hitMiss == "SHOOT_ACK_HIT":
                os.system("cls")

                serverHitBoard[shootPoint[0]][shootPoint[1]] = "X"

                print(globalVars.logoHit)
                print()

                if shipDestroyed == "SHOOT_SHIP_DEST":
                    print(globalVars.enemyShipDestroyed)
                    print()
            elif hitMiss == "SHOOT_ACK_MISS":
                os.system("cls")

                serverHitBoard[shootPoint[0]][shootPoint[1]] = "#"

                print(globalVars.LogoMiss)
                print()

                if dev:
                    connectionManager.serverSendData(playerConnection, "DEV_STAT_BOARD")
                    formatedPlayerPositionBoard = connectionManager.serverReceiveData(playerConnection)
                    playerPositionBoard = tableDataToTable(formatedPlayerPositionBoard)

                    globalVars.printBoardPosition(playerPositionBoard, True, True)
                    print()

                globalVars.printBoardHit(serverHitBoard, True)
                print()
                globalVars.printBoardPosition(serverPositionBoard, True)

                break

        connectionManager.serverSendData(playerConnection, "SHOOT_TURN_NEXT")

        while True:
            #os.system("cls")

            data = connectionManager.serverReceiveData(playerConnection)

            if data == "SHOOT_TURN_NEXT":
                break

            data = data.split("_")

            shootPoint = data[-1]
            shootPoint = list(shootPoint)
            shootPoint = [int(shootPoint[0]), int(shootPoint[1])]

            if serverPositionBoard[shootPoint[0]][shootPoint[1]] == "+":
                os.system("cls")

                serverPositionBoard[shootPoint[0]][shootPoint[1]] = "X"

                print(globalVars.opponentHitYou)
                print()
                globalVars.printBoardPosition(serverPositionBoard, False)

                coordsShootPoint = letterSet[shootPoint[0]] + str(shootPoint[1] + 1)
                shipDestroyed = "SHOOT_SHIP_NDEST"
                for shipLenght in shipCoords:
                    for shipIndex, ship in enumerate(shipCoords[shipLenght]):
                        if coordsShootPoint in ship:
                            shipCoords[shipLenght][shipIndex].remove(coordsShootPoint)

                            if len(shipCoords[shipLenght][shipIndex]) == 0:
                                shipDestroyed = "SHOOT_SHIP_DEST"

                connectionManager.serverSendData(playerConnection, "SHOOT_ACK_HIT")
                connectionManager.serverSendData(playerConnection, shipDestroyed)

            elif serverPositionBoard[shootPoint[0]][shootPoint[1]] == "X":
                os.system("cls")

                print(globalVars.opponentHitYou)
                print()
                globalVars.printBoardPosition(serverPositionBoard, False)

                connectionManager.serverSendData(playerConnection, "SHOOT_ACK_HIT")
                connectionManager.serverSendData(playerConnection, "SHOOT_SHIP_NDEST")

            elif serverPositionBoard[shootPoint[0]][shootPoint[1]] == "#":
                connectionManager.serverSendData(playerConnection, "SHOOT_ACK_MISS")
                connectionManager.serverSendData(playerConnection, "SHOOT_SHIP_NDEST")

            elif serverPositionBoard[shootPoint[0]][shootPoint[1]] == " ":
                serverPositionBoard[shootPoint[0]][shootPoint[1]] = "#"

                connectionManager.serverSendData(playerConnection, "SHOOT_ACK_MISS")
                connectionManager.serverSendData(playerConnection, "SHOOT_SHIP_NDEST")

if __name__ == "__main__":
    init()
