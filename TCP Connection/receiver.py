import socket
import sys


# Connecting to the Socket
def connect():
    try:
        SOCKET.connect((HOST, PORT))

    except socket.error as error:
        print("Error in Connecting to the Socket: " + str(error))
        print("Let's try again\nRetrying...")
        connect()


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 55555
    USERNAME = str(input("What's Your Name: "))

    try:
        SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as error_message:
        print("There is an error in creating the SOCKET: "+str(error_message))

    connect()

    print("Connected to IP: " + HOST)

    FRIEND_NAME = SOCKET.recv(1024).decode('utf-8')             # receiving the sender's username
    print("You are now Chatting with " + FRIEND_NAME)           # printing the user's username

    SOCKET.send(USERNAME.encode('utf-8'))                       # sending the sender your username

    # Endless While Loop
    while True:
        recv = str(SOCKET.recv(1024).decode('utf-8'))           # receive the message
        print(f'{FRIEND_NAME}: {recv}')                         # print the message
        msg = str.encode(input(f'{USERNAME}: '), 'utf-8')       # take the input to be sent, and typecast it into string format

        if msg == '<<QUIT>>':
            SOCKET.close()
            sys.exit()

        elif len(msg) > 0:
            SOCKET.send(msg)                                    # send the message
