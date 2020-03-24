#!/usr/bin/python3
import sys
import time
import socket
tlapse1=time.time()
print("Brute Forcing in progress...")
cryptdata=[]
decrypted_data=str('')
f=0
l=str(':>[')
ch="picoCTF{@g3nt6_1$}t0nqrabcdefhjklmsuvwxyz1245789"
def sortdatasol(data,index):
	global cryptdata,decrypted_data,f,s2,i,msg
	a=data
	while(True):
		cryptdata.append(a[:32])
		a=a[32:]
		if(a==''):
			break
	#print(len(decrypted_data))
	#for i in range(5,len(decrypted_data)):
	if(cryptdata[6]==cryptdata[11]):
		file=open('log','w')
		decrypted_data=decrypted_data+ch[index]
		file.write('Found! :'+decrypted_data)
		file.close()
		f=1
#	else:
#		print("not found")

def test(msg,inx):
	s=socket.socket()
	s.connect(('2018shell.picoctf.com',31123))
	#time.sleep(1)
	while(True):
		data = s.recv(4096).decode().strip()
		if not data:
			continue
		if 'Welcome, Agent 006!' in data:
			pass
		elif 'Please enter your situation report:' in data:
			s.send(msg.encode())
			s.send(b'\n')
			break
	#time.sleep(0.5)
	while(True):
		data=s.recv(4096).decode().strip()
		if data:
			break
	s.close()
	sortdatasol(data,inx)

try:
	print(l)
	j=0
	s1='a'*11+'a'*32
	b='fying code is: '
	#b='picoCTF{@g3nt6_'
	for i in range(0,49):
		buff='c'*(48-i)
		l=str('{}>:['.format(i))
		for j in range(0,len(ch)+1):
			l=l+'#'
			sys.stdout.write('\033[F')
			print(l)
			buffer=decrypted_data
			if(i>=16):
				buffer=buffer[i-15:]
				s2=buffer+ch[j]
			else:
				
				s2=b[i:]+decrypted_data+ch[j]
#			print('\n\n'+s2+'\n\n')
#			time.sleep(5)
			msg=s1+s2+buff
			#print(str('\n\n')+s2+str('\n\n'))
#			time.sleep(2)
			test(msg,j)
			cryptdata=[]
			if(f==1 and ch[j]=='}'):
				l=l+']'
				sys.stdout.write('\033[F')
				print(l)
				#print('\n')
				print("Flag extraction completed....")
				print("Found : {}".format(decrypted_data))
				print("Time taken: {}".format(time.time()-tlapse1))
				exit()
			elif(f==1):
				l=l+']'
				sys.stdout.write('\033[F')
				print(l)
				#print('\n')
				f=0
				break
		s2=s2[1:]
		#time.sleep(5)
		#print('\t'+s2)
except:
	raise
	print("[!]Error")
