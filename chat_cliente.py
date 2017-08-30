#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:24:52 2017

@author: root
"""

import socket, os

HOST, PORT = "", 50007
cliente =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

nome = input("Digite seu nick: ")
os.system('clear')
cliente.send(nome.encode())
nick_servidor = cliente.recv(1024)

while True:
	msg = input("Você: ")
	cliente.send(msg.encode())
	data = cliente.recv(1024)  
	print(nick_servidor.decode(),": ", data.decode())
	
cliente.close()