import socket
from  threading import Thread
from pynput.mouse import Button, Controller
from screeninfo import get_monitors
from pynput.keyboard import Key, Controller

SERVER = None
PORT=8000
IP_ADDRESS = '192.168.0.111'
screen_width=None
screen_height=None

keyboard= Controller()



def acceptConnections():
    global SERVER
    while True:
        client_socket,addr=SERVER.accept()
        print(f'Connection established with{client_socket}:{addr}')
        thread1=Thread(target=recMessage,args=(client_socket))
        thread1.start()

def getDeviseSize():
    global screen_height
    global screen_width
    for m in get_monitors():
        screen_width=int(str(m).split(',')[2].strip().split('width=')[1])
        screen_height=int(str(m).split(',')[3].strip().split('height=')[1])

def recMessage(client_socket):
    global keyboard
    while True:
        try:
            message=client_socket.recv(2048).decode()
            if(message):
                keyboard.press(message)
                keyboard.release(message)
                print(message)
        except Exception as error:
            pass


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    print('\n\n\n\n*** Welcome To Remote Keyboard***\n\n\n')
    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))
    SERVER.listen(100)
    print('\n\n\n\n\nSERVER IS WAITING FOR INCOMING CONNECTIONS\n\n\n\n\n')
    acceptConnections()
    getDeviseSize()

setup()

