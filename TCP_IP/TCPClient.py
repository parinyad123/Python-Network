import socket

def mainRun():
    host='127.0.0.1'
    port=5000

    # build object => server
    server=socket.socket()
    # สร้างการเชื่อมต่อ
    server.connect((host,port))
    # สร้างตัวแปร data ขึ้นมารับข้อมูลจากผู้ใช้
    data=input("Input your Message : ")

    # รับส่งข้อมูล
    while data!="q": # ถ้าข้อมูลไม่ใช่ q ให้ส่งข้อมูล
        server.send(data.encode('utf-8')) # ส่งข้อมูล
        
        data=server.recv(1024).decode('utf-8') # รับข้อมูล
        print("Data From Server : " +data)

        data=input("Input your Message : ")

    server.close()

if __name__=="__main__":
    mainRun()