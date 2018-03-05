'''
author= Meghana Sathish (mxs7620@rit.edu)
Simple Web Server
'''
from socket import *

def webserver():
    server_socket = initialize()
    while True:
        connection,addr = server_socket.accept() #connecion from the client being established
        print('Address of the connection:\n',addr)
        try:
            name_of_file = connection.recv(1024)  #input filename
            print('file being processed:',name_of_file)
            parse = name_of_file.split()[1]  #parsing the request for the specific file
            file = open(parse[1:])
            data = file.read()
            print('data:',data)
            connection.send('\nHttp/1.1 200 OK\n\n') #Sending data to the client
            connection.sendall(data.encode('utf-8'))
            connection.close()
        except IOError:
            # throw 404 error if file not found in system
            connection.send('\HTTP/1.1 404 Not Found\n\n')
            connection.send('404 Not Found')
            print('404 File not Found')
            connection.close()
        break
    server_socket.close()

def initialize():
    # initializing server
    server_socket = socket(AF_INET, SOCK_STREAM)
    port = 6869
    server_socket.bind(('', port))
    server_socket.listen(3)
    print('Port being used',port)
    return server_socket

def main():
    webserver()

if __name__ == '__main__':
    main()
