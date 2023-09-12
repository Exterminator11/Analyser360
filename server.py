
import socket
import pickle
import csv
HEADERSIZE = 10
def c(f,e,ff):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 9999))
    s.listen(5)
    with open(f,'a') as file:
        file.write(f'\n{e},{ff},{f}')
    while True:
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        with open(f,'r') as file:
            d = file.read()
        msg = pickle.dumps(d)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
        print(msg)
        clientsocket.send(msg)
        clientsocket.close()
        s.close()