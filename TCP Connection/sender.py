"""
This is a 2 device connection for sending and receiving messages.
I did it using functional programming and a lot of exception handling, 
so please don't point out any mistakes. I did it after 2 months of failing to do a google search!
Also I'm a Rookie
Default size of received and sent texts is 1024 bytes or 1 KB.
Created on 17th September 2020
By Neelay Naman aka __bihari___
"""

import socket
import sys


# Binding the Socket and Listening for Connections for 10 times before throwing an exception
def bind():
    try:
        SOCKET.bind((HOST, PORT))
        SOCKET.listen(10)

    except socket.error as error:
        print("Error in Binding the Socket: " + str(error))
        print("Let's try again\nRetrying...")
        bind()


# Accepting the Connection
def accept():
    connection, client = SOCKET.accept()
    print("Connected to IP : " + client[0])

    connection.send(USERNAME.encode('utf-8'))                   # sending the receiver your username

    FRIEND_NAME = connection.recv(1024).decode('utf-8')         # receiving the receiver's username
    print("You are now Chatting with "+FRIEND_NAME)             # printing it at the start of the chat

    message(connection, FRIEND_NAME)                            # go to the message function till you exit
    connection.close()                                          # when you exit out of the while loop, the connection is closed


# Sending messages
def message(connection, name):
    while True:
        msg = str.encode(input(f'{USERNAME}: '), 'utf-8')       # take the input and typecast it in string format
        
        if msg == '<<QUIT>>':                                   # command to exit the connection
            SOCKET.close()                          
            connection.close()
            sys.exit()

        elif len(msg) > 0:
            connection.send(msg)                                # send the message
            response = str(connection.recv(1024), 'utf-8')      # store the response in string format
            print(f'{name}: {response}')


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 55555
    USERNAME = str(input("What's Your Name: "))
    
    try:
        SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as error_message:
        print("There is an error in creating the SOCKET: "+str(error_message))

    bind()
    accept()
