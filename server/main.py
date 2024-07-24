import json
import os
import socket
import uuid
from _thread import start_new_thread
from typing import overload
from game import Game
from player import Player

_game = Game()
_clients = []

server = "0.0.0.0"
port = 8086


def send(conn: socket.socket, msg: str) -> None:
    msg = f"{msg}\r\n"
    conn.send(str.encode(msg))


def broadcast(msg: str, sender_socket=None):
    for client in _clients:
        if client != sender_socket:
            try:
                send(client, msg)
            except Exception as e:
                print(f"Error sending message to client: {e}")


def update_display() -> None:
    global _game

    if _game.is_ready == True:
        os.system("cls")
        print(f"{_game._player1.name}:")
        print(f"{_game._player2.name}:")
        print(f"Turn:xx")
        print(f"+===+===+===+")
        print(f"| {_game.board[0]} | {_game.board[1]} | {_game.board[2]} | ")
        print(f"+===+===+===+")
        print(f"| {_game.board[3]} | {_game.board[4]} | {_game.board[5]} | ")
        print(f"+===+===+===+")
        print(f"| {_game.board[6]} | {_game.board[7]} | {_game.board[8]} | ")
        print(f"+===+===+===+")


def threaded_client(conn: socket.socket, _player: Player):
    global _game

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
                print(f"  INCOMING MESSAGE: {_player.number} - {data}")

                split = data.split(":", 1)

                for i, s in enumerate(split):
                    split[i] = s.strip()

                cmd = split[0].upper()

                if cmd == "NAME":
                    _player.name = split[1]
                    send(conn, f"MSG:S:Greeting {split[1]}")
                    if _game.is_ready == True:
                        broadcast("STARTGAME\r\n")
                elif cmd == "MSG":
                    broadcast(f"MSG:{_player.id}:{split[1]}", conn)

            update_display()
        #    conn.send(str.encode(str(split)))
        #           sendall(conn, reply)
        except Exception as e:
            # Handle the exception
            print(f"An error occurred: {e}")
            break

    print("Lost connection")
    conn.close()


def main() -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    os.system("cls")
    print("[= Starting App]==")
    s.listen(2)
    print("  Waiting for a connection, Server Started")

    while True:
        conn: socket.socket
        addr: tuple[str, int]

        conn, addr = s.accept()
        print(f"  Connected detected from {addr[0]}:{addr[1]}")
        _clients.append(conn)

        if _game.player_count == 0:
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


if __name__ == "__main__":
    main()


##  What should the server do?
"""
    Allow the connection of exactly two players
        if a 3rd connects, reject it nicely
    
    when two players are connected, it should start a game and notify players

    it should store the game state (3x3 grid), player ids, etc.

    it should detect winning or losing and notify players

    it should reject invalid moves

    
"""
