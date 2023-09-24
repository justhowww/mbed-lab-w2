import socket
import json
import numpy as np
import matplotlib.pyplot as plot

HOST = '192.168.50.141'  # IP地址
PORT = 8889  # 聆聽的埠號（請使用大於1023的埠號）

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("正在啟動伺服器，位於：", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print("已連接至", addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print("從套接字伺服器接收到數據：", data)
            if (data.count('{') != 1):
                # 收到不完整的數據。
                choose = 0
                buffer_data = data.split('}')
                while buffer_data[choose][0] != '{':
                    choose += 1
                data = buffer_data[choose] + '}'
            obj = json.loads(data)
            t = obj['s']
            plot.scatter(t, obj['x'], c='blue')  # x, y, z, gx, gy, gz
            plot.scatter(t, obj['y'], c='yellow')  # x, y, z, gx, gy, gz
            plot.scatter(t, obj['z'], c='red')  # x, y, z, gx, gy, gz
            plot.xlabel("x, y, z acceleratoin")
            plot.pause(0.0001)

