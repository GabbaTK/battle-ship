import socket

tmpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocketIp = socket.gethostbyname(socket.gethostname())
format = "utf-8"
header = 64

def hostName():
    return socket.gethostname()

def hostIp():
    return socket.gethostbyname(hostName())

def awaitConnection(port):
    tmpSocket.bind((serverSocketIp, port))
    tmpSocket.listen()

    # Connection, (Address, Port)
    return tmpSocket.accept()

def connect(ip, port):
    # Check to see if its IP or PC name
    ip = socket.gethostbyname(ip)
    addr = (ip, port)

    tmpSocket.connect(addr)

def serverSendData(connection, msg):
    #try:
    msg = msg.encode(format)
    msgLenght = str(len(msg)).encode(format) + b" " * (header - (len(str(len(msg)).encode(format))))
    connection.send(msgLenght)
    connection.send(msg)
    #except:
    #    print("The connection was unexpectadly terminated")
    #    exit()

def serverReceiveData(connection):
    try:
        lenght = connection.recv(header).decode(format)
        data = connection.recv(int(lenght)).decode(format)

        return data
    except:
        print("The connection was unexpectadly terminated")
        exit()

def clientSendData(msg):
    try:
        msg = msg.encode(format)
        msgLength = str(len(msg)).encode(format) + b" " * (header - (len(str(len(msg)).encode(format))))
        tmpSocket.send(msgLength)
        tmpSocket.send(msg)
    except:
        print("The connection was unexpectadly terminated")
        exit()

def clientReceiveData():
    try:
        legnth = tmpSocket.recv(header).decode(format)
        data = tmpSocket.recv(int(legnth)).decode(format)

        return data
    except:
        print("The connection was unexpectadly terminated")
        exit()

def requestSyncS(connection):
    serverSendData(connection, "SYNC")
    serverReceiveData(connection)

def requestSyncC():
    clientSendData("SYNC")
    clientReceiveData()
