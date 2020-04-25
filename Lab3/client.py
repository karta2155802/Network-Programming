import socket
import sys
import time
import boto3
import os

s3 = boto3.resource('s3')
target_bucket = None

def mkdir():
    Pdata = "./.data"
    Ppost = "./.data/post"
    Pcomment = "./.data/comment"
    try:
    	os.makedirs(Pdata)
    	os.makedirs(Ppost)
    	os.makedirs(Pcomment)
    except FileExistsError:
    	return

def receive():
	while True:
		try:
			msg_in = s.recv(1024).decode('utf-8')
			return msg_in
		except:
			pass

def CreateObject(cmd):
	cmd_list = cmd.split()
	content_position = cmd_list.index('--content')
	content = ' '.join(cmd_list[content_position+1:len(cmd_list)])

	fp = open("./.data/post/p{}".format(), "w")
	
def command(cmd, msg_in, s):
	if msg_in == 'Register successfully.\r\n':
		bucket_name = '0516319-' + cmd.split()[1] + '-0516319'		
		s3.create_bucket(Bucket = bucket_name)
	elif cmd.startswith('login') and msg_in.startswith('0516319'):
		target_bucket = s3.Bucket(msg_in)
		while True:
			try:
				msg_in = s.recv(12).decode('utf-8')
				print(msg_in)
				return msg_in
			except:
				pass
	elif cmd.startswith('logout') and msg_in.startswith('Bye'):
		target_bucket = None
	elif cmd.startswith('create-post') and msg_in.isdigit():
		while True:
			try:
				msg_in = s.recv(11).decode('utf-8')
				
				return msg_in
			except:
				pass



	elif cmd == 'exit':
		sys.exit()
	else:
		pass
	return msg_in


dst_ip = str(sys.argv[1])
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((dst_ip, port))
msg_in = s.recv(1024).decode('utf-8')
print(msg_in,end = "")
s.setblocking(0)
mkdir()

while True:
	msg_in = receive();	
	print(msg_in ,end = "")
	cmd = input()
	if not cmd or len(cmd.split()) == 0:
		cmd = 'enter&&space'
		s.send(cmd.encode('utf-8'))
	else:
		s.send(cmd.encode('utf-8'))
		msg_in = receive();
		msg_in = command(cmd, msg_in, s)
		print(msg_in ,end = "")


