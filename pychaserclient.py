import os
import socket

from logging import getLogger

BUF_SIZE = 4096

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

FLAG_CONNECTION_CLOSE = 0

class ConnectionCloseSignal(Exception):
    pass

def strarr_to_intarr(val):
    """
    文字列をintのリストにする
    """
    return [int(s) for s in val]

class PyChaserConnect
    def __init__(self, username, host, port):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._host = host
        self._port = port
        self._username = username
        self._client.connect((host, port))

    def disconnect(self):
        self._client.close()

    def username(self):
        return send(self._username)

    def send(self, msg):
        return self._client.send("%s\r\n" % msg)

    def recv(self):
        result = self._client.recv(BUF_SIZE).strip()
        return result

    def getReady(self):
        _ = self.recv()
        send("gr")
        msg = recv()

    def walk(self, direction):
        if direction is LEFT:
            send("wl")
        elif direction is RIGHT:
            send("wr")
        elif direction is UP:
            send("wu")
        elif direction is DOWN:
            send("wd")

        result = recv()
        info = strarr_to_intarr(result)
        turnEnd()

        return info
    
    def search(self, direction):
        if direction is LEFT:
            send("sl")
        elif direction is RIGHT:
            send("sr")
        elif direction is UP:
            send("su")
        elif direction is DOWN:
            send("sd")
        
        result = recv()
        info = strarr_to_intarr(result)
        turnEnd()
        
        return info

    def look(self, direction):
        if direction is LEFT:
            send("ll")
        elif direction is RIGHT:
            send("lr")
        elif direction is UP:
            send("lu")
        elif direction is DOWN:
            send("ld")

        result = recv()
        info = strarr_to_intarr(result)
        turnEnd()

    def put(self, direction):
        if direction is LEFT:
            send("pl")
        elif direction is RIGHT:
            send("pr")
        elif direction is UP:
            send("pu")
        elif direction is DOWN:
            send("pd")
        
        result = recv()
        info = strarr_to_intarr(result)
        turnEnd()

    def turnEnd(self):
        send(r"#")
        
        