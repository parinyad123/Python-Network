import socket

def mainRun():
    host="127.0.0.1"
    port=20001
    databind=(host,port)

    server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server.connect((host,port))

    data=input("Input Message :")

    while data!="q":
        server.sendto(data.encode('utf-8'),databind)
        data,addr=server.recvfrom(1024)
        data=data.decode('utf-8')
        print("Message From Server : " +data)
        data=input("Input Message :")

    server.close()

if __name__=="__main__":
    mainRun()


