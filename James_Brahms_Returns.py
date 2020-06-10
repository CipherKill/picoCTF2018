#!/usr/bin/python3
import os
import time
from pwn import *
global s

context.log_level='error'
f=open('log','r')
final=f.read()
#print(final)

def form(data):
	cache=[data[i:32+i] for i in range(0,len(data),32)]
	return cache


def xfind(v1,v2):
	cache=int(v1,16)^int(v2,16)^int(16)
	cache=chr(cache)
	return cache

def comb(data):
	cache=''.join(data[i] for i in range(0,len(data)))
	cache=cache+'\n'
	return cache

def send(payload,payloadtrail):
	global s
	s=remote('2018shell.picoctf.com', 15608)
	#print("[-]Connected to server")
	s.recvuntil('Send & verify (S)\n')
	s.send(b'e\n')
	s.recvuntil('Please enter your situation report: ')
	s.send((payload+'\n').encode())
	s.recvuntil('Anything else? ')
	s.send((payloadtrail+'\n').encode())
	data=(s.recv())[11:]
	data=form(data.decode())
	return data

def test(payload):
	global s
	s.recvuntil('Send & verify (S)\n')
	s.send('s\n'.encode())
	s.recvuntil('Please input the encrypted message: ')
	s.send(comb(payload).encode())
	r=s.recv()
	#print(r.decode())
	if(r.find(b'Successful decryption')!=-1):
		#os.system('spd-say "Found a match"')
		print("\n[!]Found!")
		return True
	else:
		#print("\n[-]Not Found\n----------------------------------\n")
		return False

def log(data):
	f=open('log','w')
	f.write(data)
	f.close()

def main():
	global final
	hex='0123456789abcdef'
	print("[-]Program will begin")
	i=len(final) #STARTS AT ZERO
	count=0
	#final=''
	while(i<32):
		if(count%50==0):
			print('][')
			time.sleep(20)
		os.system('clear')
		print("-"*64+"\n[!]Running Brute Force\n[-]Trials:\t{}\n[-]Index:\t{}\n[#]Decrypted:\t{}\n".format(count,i,final)+"-"*64)
		val=''
		payload='b'*(59-i) #59
		payloadtrail='a'*(i+3)
		print("-"*64+"\n[!]Running Brute Force\n[-]Trials:\t{}\n[-]Index:\t{}\n[#]Decrypted:\t{}\n".format(count,i,final)+"-"*64)
		data=send(payload,payloadtrail)
		bb=data[8]
		hash=data[len(data)-2]
		data[len(data)-1]=data[9]
		flag=False
		flag=test(data)
		s.close()
		if(flag==True):
			val=xfind(bb[-2:],hash[-2:])
			os.system('spd-say "found"'.format(val))
			final=final+val
			log(final)
			if(val=='}'):
				print('ended')
				exit()
			#time.sleep(30)
			i=i+1
			count=0
		count=count+1
while(True):
	try:
		main()
	except:
		time.sleep(120)
		pass
#print("-"*64+"[-]Program Completed"+'-'*64)
