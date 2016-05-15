import sys
import os
from twilio.rest import TwilioRestClient

phoneNumber = -1

def main():
	os.system('clear')
	choice = printMenu()
	while choice != 6:
		os.system('clear')
		if choice == 1:
			print("Set phone number")
		elif choice == 2:
			print("Add a medication")
		elif choice == 3:
			print("Delete a medication")
		elif choice == 4:
			print("View all medications")
		else:
			print("Start Listening")
		choice = printMenu()


def printMenu():
	if phoneNumber == -1:
		print("Phone Number: NOT SET\n")
	else:
		print("Phone Number: " + phoneNumber)
	print("1) Set phone number\n2) Add a medication\n3) Delete a medication\n4) View all medications\n5) Start Listening\n6) Quit")
	takeInput = True
	while True:
		try:
			choice = int(input("Pick a menu option: "))
			if 0 < choice <= 6:
				return choice
			else:
				print("Invalid Input-- try again")
		except ValueError:
			print("Invalid Input-- try again")
		except NameError:
			print("Invalid Input-- try again")
		except SyntaxError:
			print("Invalid Input-- try again")


if __name__ == "__main__":
	main()