# build Socket of server

import socket


def mainRun():
    # ทำการทดสอบ program ผ่านเครืองเรา host กำหนดผ่าน host
    host="127.0.0.1" #ip local host
    port=5000
    # สร้าง object ของ socket เพื่อใช้รับส่งข้อมูล
    server=socket.socket()
    # ทำการผูก(bind) object socket ไว้กับ host
    server.bind((host,port))
    # กำหนดจำนวน client
    server.listen(1)
    print("Waiting to connect from Client:")

    # สร้าง object 2 ตัว เมื่อมีการเครื่องต่อ (accept) กับ client แล้วจะเก็บค่าไว้ใน object ทั้ง 2
    client,addr=server.accept()
    # print บอก สถานะ
    print("Connect From :"+ str(addr))


    # กระบวนการรับส่งข้อมูลระหว่างเครื่อง 
    while True: # ทำการรับส่งข้อมูลไปเรื่อยๆ
        # ข้อมูลที่รับส่งเป็นข้อมูลแบบ byte
        # รับข้อมูลจาก client
        data=client.recv(1024).decode('utf-8') 
        # รับข้อมูล 1024 ตัวอักษร (1024 byte = 1kbyte) # decode แปลง byte เป็น string
        # client ส่งข้อมูลมาจะถูกเก็บไว้ในตัวแปร string

        if not data:
            break # ถ้าไม่มี data ให้ออกจาก loop
        
        print("Message From Client : "+data)

        # ส่งข้อมูลไปหา Client
        data=str(data.upper()) # ถ้า client ส่งข้อมูลเป็นตัวพิมพ์เล็ก จะแปลงเป็นตัวพิมพ์ใหญ่และส่งไปให้ client
        client.send(data.encode('utf-8')) # ข้อมูลที่ส่งมีการแปลงจาก string เป็น byte

    client.close() # สั่ง client ให้ปิด



if __name__=="__main__":
    mainRun()
