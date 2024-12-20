import socket


a = [1, 2, 3]

b = [4, 5, 6]

print((a.extend(b), a))

def getHostIP():
    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.gaierror as e:
        print(f"{e}")

print(getHostIP())