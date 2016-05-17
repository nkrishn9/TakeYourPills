import sys
import os
from twilio.rest import TwilioRestClient
import sqlite3 as lite

phoneSet = False
phoneNumber = 0;
con = lite.connect('data.db')
with con:
	cur = con.cursor()
	cur.execute("SELECT * FROM sqlite_master WHERE name ='phoneNumber' and type='table'; ")
	if len(cur.fetchall()) is not 0:
		phoneSet = True
		cur.execute("SELECT * FROM phoneNumber")
		phoneNumber = int(cur.fetchone()[0])


def main():
	os.system('clear')
	choice = printMenu()
	while choice != 6:
		os.system('clear')
		if choice == 1:
			print("Set phone number")
			addNumber(input("New number: "))
		elif choice == 2:
			print("Add a medication")
		elif choice == 3:
			print("Delete a medication")
		elif choice == 4:
			print("View all medications")
		else:
			print("Start Listening")
		os.system('clear')
		choice = printMenu()

def printMenu():
	global phoneSet, phoneNumber
	if not phoneSet:
		print("Phone Number: NOT SET\n")
	else:
		print("Phone Number: (" + str(phoneNumber)[0:3] + ") " + str(phoneNumber)[3:6] + "-" + str(phoneNumber)[6:] + "\n")
	print("1) Set phone number\n2) Add a medication\n3) Delete a medication\n4) View all medications\n5) Start Listening\n6) Quit")
	while True:
		try:
			choice = int(input("Pick a menu option: "))
			if 0 < choice <= 6:
				return choice
			else:
				print("Enter an option from 1 to 6")
		except BaseException:
			print("Invalid Input-- try again")

def addNumber(numToAdd):
	global phoneSet, phoneNumber
	while True:
		try:
			numToAdd = int(numToAdd)
			break
		except BaseException:
			numToAdd = input("Enter a valid phone number: ")
	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS phoneNumber")
		cur.execute("CREATE TABLE phoneNumber(number INT)")
		cur.execute("INSERT INTO phoneNumber VALUES(" + str(numToAdd) + ")")
		phoneSet = True
		cur.execute("SELECT * FROM phoneNumber")
		phoneNumber = int(cur.fetchone()[0])


if __name__ == "__main__":
	main()