import socket
from time import sleep

c=socket.socket()

host ='127.0.0.1'
port=9999

#Connect to host.
c.connect((host,port))
name=raw_input('Enter username:')
c.send(name)
print 'Please enter your messages in the format Username : Message '

#Giving an input to the host and receiving messages from others.
flag=1
while flag:
	data=raw_input('->')
	if data=='quit':
		flag=0
	c.send(data)
	try:
		reply=c.recv(1024)
		if reply:
                	print reply
	except socket.error, e:
		if e.args[0]:
			continue
				
c.close()
