import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

file = open("backup-08-05-2024-12-11-48.sql", "rb")
file_size = os.path.getsize("sql")

client.send("backupNV-08-05-2024-12-11-48.sql".encode())
client.send(str(file.size).encode())

data = file.read()
client.sendall(data)
client.send(b"<END>")

file.close()
client.close()


