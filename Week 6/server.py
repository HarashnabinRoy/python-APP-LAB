# server file 

import socket
# to create server socket
s=socket.socket()
s.bind(('localhost',9999))
print('waitng for connections')


# to accept clients
s.listen(2)
i=1
while True:
    i+=1
    print(i)

    # accepting clients 
    cli,port_cli=s.accept()

    print('connected with ',port_cli)
    cli.send(bytes('hello there','utf-8'))
    break

def send_to_ser(statement):
    cli.send(bytes(statement,'utf-8'))
def rec_frm_ser():
    return (cli.recv(1024).decode())

print('=============chat started===================')


while True:
    #print(i)
        i+=1
   
        statement=input('>>>')
        cli.send(bytes(statement,'utf-8'))
       
        print('\t\t\t {}'.format(cli.recv(1024).decode()))
    
# print('msg sent')