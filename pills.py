import sys
import os
from twilio.rest import TwilioRestClient
import sqlite3 as lite

#Struct for basic medication
#Time is int of minutes past midnight
class Medication:
	def __init__(self, name, time):
		self.name = name
		self.time = time
medicationList = []
phoneSet = False
phoneNumber = 0;

#setup database if not there/ populate from database
con = lite.connect('data.db')
with con:
	cur = con.cursor()
	cur.execute("SELECT * FROM sqlite_master WHERE name ='phoneNumber' and type='table'; ")
	if len(cur.fetchall()) is not 0:
		phoneSet = True
		cur.execute("SELECT * FROM phoneNumber")
		phoneNumber = int(cur.fetchone()[0])
	cur.execute("SELECT * FROM sqlite_master WHERE name ='medications' and type='table'; ")
	if len(cur.fetchall()) is 0:
		cur.execute("CREATE TABLE medications(Name TEXT, Time INT)")
	else:
		cur.execute("SELECT * FROM medications")
		rows = cur.fetchall()
		for row in rows:
			temp = Medication(row[0], int(row[1]))
			medicationList.append(temp)
			

def main():
	os.system('clear')
	choice = printMenu()
	while choice != 5:
		os.system('clear')
		if choice == 1:
			print("Set phone number")
			addNumber(input("New number: "))
		elif choice == 2:
			print("Add a medication")
			addMedication()
		elif choice == 3:
			print("Delete a medication")
		else:
			print("Start Listening")
		os.system('clear')
		choice = printMenu()

def printMenu():
	global phoneSet, phoneNumber, medicationList
	if not phoneSet:
		print("Phone Number: NOT ASSIGNED")
	else:
		print("Phone Number: (" + str(phoneNumber)[0:3] + ") " + str(phoneNumber)[3:6] + "-" + str(phoneNumber)[6:])
	if (len(medicationList) == 0):
		print("Current Medications: NONE ASSIGNED")
	else:
		print("Current Medications: ")
		for medication in medicationList:
			print(medication.name + " at " + str(intToTime(medication.time)))
	print("")
	print("1) Set phone number\n2) Add a medication\n3) Delete a medication\n4) Start Listening\n5) Quit")
	while True:
		try:
			choice = int(input("Pick a menu option: "))
			if 0 < choice <= 5:
				return choice
			else:
				print("Enter an option from 1 to 5")
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
		con.commit()
		phoneSet = True
		cur.execute("SELECT * FROM phoneNumber")
		phoneNumber = int(cur.fetchone()[0])

def addMedication():
	medicationName = input("Medication name: ")
	#Error Check this later
	medicationName = "'" + medicationName + "'"
	time = input("When will you be taking " + medicationName + "(HH:MM AM/PM)? ")
	hours = time[0:2]
	minutes = time[3:5]
	beforeNoon = False
	if time[6:].upper() == "AM":
		beforeNoon = True
	aggregate = timeToInt(hours, minutes, beforeNoon)
	temp = Medication(medicationName, aggregate)
	medicationList.append(temp)
	medicationName = "'" + medicationName + "'"
	tup = (medicationName, str(aggregate))
	cur.execute("INSERT INTO medications VALUES(?, ?)", (tup))
	con.commit()


def timeToInt(hours, minutes, beforeNoon):
	hours = int(hours)
	minutes = int(minutes)
	if beforeNoon:
		return (hours * 60 + minutes)
	else:
		return (12 * 60 + (hours % 12) * 60 + minutes)

def intToTime(aggregate):
	minutes = aggregate % 60
	hours = int(aggregate / 60)
	beforeNoon = True
	if hours > 12:
		hours = hours % 12
		beforeNoon = False
	return [hours, minutes, beforeNoon]

if __name__ == "__main__":
	main()