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
piecesLeft = {"4":1,
              "3":2,
              "2":3,
              "1":4}
letterSet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def funcCall(func):
    func()

def setupShips():
    global serverPositionBoard

    returnBoard = globalVars.setupShips(serverPositionBoard)
    serverPositionBoard = returnBoard

def init(dev, defaultShipPosition):
    global serverPositionBoard
    global boardHitText
    global boardPositionText

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
    else:
        setupShips()

    print("Waiting for ther person...")
    connectionManager.requestSyncS(playerConnection)

if __name__ == "__main__":
    init()
