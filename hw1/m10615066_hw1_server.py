# server
import socket

serverPort = 4000
ipaddr = '127.0.0.1'

# use IPv4 and TCP
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverSocket.bind((ipaddr,serverPort))
serverSocket.listen(1)

print("The server is ready to receive...")
print("=================================")
print()

while True:
     connectionSocket, addr = serverSocket.accept()
     print ('Connection address: ', addr)
     
     calculation = connectionSocket.recv(1024)

     # if expression is operable string, then this func calculate the expression
     answer = str(eval(calculation))

     ans_encode = answer.encode()
     print("\nThe answer of {} is {}".format(calculation.decode(), answer))

     connectionSocket.send(ans_encode)
     break


serverSocket.close()


# if console print this error
# OSError: [WinError 10048] 一次只能用一個通訊端位址 (通訊協定/網路位址/連接埠)。
# go cmd and type 
# $netstat -ano|findstr 4000   
# and then you can see 
#  TCP    127.0.0.1:4000      0.0.0.0:0       LISTENING     9776
# the last number is PID, kill this task
# $taskkill /PID 9776 /F