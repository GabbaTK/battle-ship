import globalVars
import server
import client
import os

options = "\033[97m[\033[96m1\033[97m] Start a server\n\033[97m[\033[96m2\033[97m] Connect to a server"
optionsDev = "\033[97m[\033[96m1\033[97m] Start a server\n\033[97m[\033[96m2\033[97m] Connect to a server\n\033[97m[\033[96m3\033[97m] Exit developer mode\n\033[97m[\033[96m4\033[97m] [DEF_SHIP_POS_STATE] default ship positioning\n\033[97m[\033[96m5\033[97m] Call a server function\n\033[97m[\033[96m6\033[97m] Call a client function"
dev = False
defaultShipPositionState = "Enable"
logoBattleShip = globalVars.logoBattleShip
logoBattleShipDev = globalVars.logoBattleShipDev


def start(dev):
    global defaultShipPositionState

    os.system("cls")

    if not dev:
        print(logoBattleShip)
        print(options)
    else:
        print(logoBattleShipDev)
        print(optionsDev.replace("[DEF_SHIP_POS_STATE]", defaultShipPositionState))
    print()

    selectedInput = int(input(">"))

    if selectedInput == 1:
        server.init(dev, defaultShipPositionState)
        exit()
    elif selectedInput == 2:
        client.init(defaultShipPositionState)
        exit()
    elif selectedInput == 3:
        dev = not dev
    elif selectedInput == 4 and dev:
        if defaultShipPositionState == "Enable":
            defaultShipPositionState = "Disable"
        else:
            defaultShipPositionState = "Enable"
    elif selectedInput == 5 and dev:
        function = input("S_FUNC_CALL>")
        print(f"Return value: {server.funcCall(getattr(server, function))}")
        exit()
    elif selectedInput == 6 and dev:
        function = input("C_FUNC_CALL>")
        print(f"Return value: {client.funcCall(getattr(client, function))}")
        exit()

    start(dev)

try:
    start(dev)
except KeyboardInterrupt:
    print()
    print("Exiting!")
