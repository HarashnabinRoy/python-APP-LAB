# client file 


import socket

cli=socket.socket()

cli.connect(('localhost',9999))

print(cli.recv(1024).decode())

def send_to_ser(statement):
    cli.send(bytes(statement,'utf-8'))
def rec_frm_ser():
    print(cli.recv(1024).decode())

print('========chat started===========')
while True:
    try:
        print('\t\t\t {}'.format(cli.recv(1024).decode()))
        statement=input('>>>')
        
        cli.send(bytes(statement,'utf-8'))
        
        #print(cli.recv(1024).decode())
    except:
        print('host has ended the connection')
        break
