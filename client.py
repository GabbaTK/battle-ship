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

def funcCall(func):
    func()

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
        setupShips()

    print("Waiting for ther person...")
    connectionManager.requestSyncC()

if __name__ == "__main__":
    init()
