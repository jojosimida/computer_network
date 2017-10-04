# client
import socket

ipaddr = '127.0.0.1'
serverPort = 4000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((ipaddr,serverPort))

print("This is client")
print("==========================")

calculation = input("Input a Calculation formula: ")
clientSocket.send(calculation.encode('utf-8'))

answer = clientSocket.recv(1024).decode()
print ("Calcualte the answer from server:", answer)
clientSocket.close()
