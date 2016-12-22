#!/usr/bin/evn python 
import socket,sys,select
port =  51423
host = 'localhost'

spinsize = 10
spinpos  = 0
spindir  = 1

def spin():
	global spinsize ,spinpos, spindir
	spinstr = '.'*spinpos +\
		'|'+'.'*(spinsize-spinpos-1)
	sys.stdout.write('\r'+spinstr+'')
	sys.stdout.flush()
	
	spinpos+=spindir
	if spinpos <0:
		spindir =1
		spinpos =1
	elif spinpos>=spinsize:
		spinpos-=2
		spindir=-1
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

p = select.poll()
p.register(s.fileno(),select.POLLIN|select.POLLERR|select.POLLHUP)
while 1:
	results = p.poll(50):
	if len(results):
		if results[0][1]==select.POLLIN:
			data = s.recv(4096)
