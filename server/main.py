import json
import os
import socket
import uuid
from _thread import start_new_thread
from game import Game
from player import Player

_game = None

server = "0.0.0.0"
port = 8086

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


os.system("cls")
print("[= Starting App]==")
s.listen(2)
print("  Waiting for a connection, Server Started")


def send(conn: socket.socket, msg: str) -> None:
    msg = f"{msg}\r\n"
    conn.send(str.encode(msg))


def sendall(conn: socket.socket, msg: str) -> None:
    msg = f"{msg}\r\n"
    conn.sendall(str.encode(msg))


def threaded_client(conn: socket.socket, _player: Player):
    msg = "CONNECTED\r\n"
    send(conn, msg)

    msg = f"ID:{_player.number}:{_player.id}\r\n"
    send(conn, msg)

    msg = f"NAME?\r\n"
    send(conn, msg)

    reply = ""

    while True:
        try:
            data = conn.recv(4096).decode("utf-8").replace("\r\n", "")

            if data:
                print(f"{_player.number} - {data}")

                split = data.split(":", 1)

                for i, s in enumerate(split):
                    split[i] = s.strip()

                split[0] = split[0].upper()

                if split[0] == "NAME":
                    _player.name = split[1]
                    send(conn, "MSG:S:Waiting on Player 2")

        #    conn.send(str.encode(str(split)))
        #           sendall(conn, reply)
        except Exception as e:
            # Handle the exception
            print(f"An error occurred: {e}")
            break

    print("Lost connection")
    conn.close()


while True:
    conn: socket.socket
    addr: tuple[str, int]

    conn, addr = s.accept()
    print(f"  Connected detected from {addr[0]}:{addr[1]}")

    if _game == None:
        _game = Game()
        id = uuid.uuid4()
        p1 = Player(id, 1, "Player 1")
        _game.assign_player_1(p1)
        print("  Creating Player 1 and assigning to game")
        start_new_thread(threaded_client, (conn, p1))
    elif _game.player_count == 1:
        id = uuid.uuid4()
        p2 = Player(id, 2, "Player 2")
        print("  Creating Player 2 and assigning to game")
        _game.assign_player_2(p2)
        start_new_thread(threaded_client, (conn, p2))

print("==[ End Run]==")

##  What should the server do?
"""
    Allow the connection of exactly two players
        if a 3rd connects, reject it nicely
    
    when two players are connected, it should start a game and notify players

    it should store the game state (3x3 grid), player ids, etc.

    it should detect winning or losing and notify players

    it should reject invalid moves

    
"""
