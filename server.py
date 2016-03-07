import socket
import sys
import threading
import thread

sockdict={}
#Creating server socket.
sckt = socket.socket()
sckt.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server_address = ('127.0.0.1', 9999)
sckt.bind((server_address))
sckt.listen(5) 

print "Server is running"

#Connecting to the three sockets.
c1 , addr1=sckt.accept()
username1=c1.recv(1024)
if username1:
        sockdict[username1]=c1
        print username1+ " is connected"

c2, addr2=sckt.accept()
username2=c2.recv(1024)
if username2:
        print username2+ " is  connected"
        sockdict[username2]=c2

c3, addr3=sckt.accept()
username3=c3.recv(1024)
if username3:
        print username3+ " is connected"
        sockdict[username3]=c3




#Functions of sending message to client,broadcasting and receiving.
def client_send(sock,message,socket):
	user= [key for key, value in sockdict.iteritems() if value == socket][0]
        sock.send('Message from ' +user +':'+message)
	print user +':' + message

def send_all(message,socket):
	for user in sockdict.values():
		if user!=socket:
			user.send('Broadcast message:'+message)

def client_recv(socket,reply):
	if reply=='':
		return
	else: 
        	username=reply.split(':')[0]
		if username in sockdict.keys():
        		sock=sockdict[username]
        		message=reply.split(':')[1]
        		thread.start_new_thread((client_send),(sock,message,socket))
		elif username=='broadcast':
			message=reply.split(':')[1]
			thread.start_new_thread((send_all),(message,socket))
		else:
			socket.send('Sorry '+username+ 'is not online')


while True:
	data1=c1.recv(1024)
	data2=c2.recv(1024)
       	data3=c3.recv(1024)
	if data1 or data2 or data3:
		if data1:
			thread.start_new_thread(client_recv,(c1,data1))
		if data2:
			thread.start_new_thread(client_recv,(c2,data2))
		if data3:
			thread.start_new_thread(client_recv,(c3,data3))
			
