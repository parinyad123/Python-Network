import socket

def mainRun():
    host="127.0.0.1"
    port=5000

    server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server.bind((host,port))

    # UCP จะไม่มีการรอยืนยันเหมือน TCP
    # โดยเมื่อ server ทำการ run เราจะ start รอได้เลย
    print("Start Server")

    while True:
        data,addr=server.recv(1024) # รับข้อมมูลมาจาก client
        data=data.decode('utf-8') # เปลี่ยน data จาก binary ให้กลายเป็น string
        print("Message From Client : "+data)
        data=data.upper()
        print("Convert String : "+data)

        # ส่งข้อความไปหา client
        server.sendto(data.encode('utf-8'),addr) # ส่ง data ไปที่ addr

    server.close()

if __name__=="__main__":
    mainRun()
