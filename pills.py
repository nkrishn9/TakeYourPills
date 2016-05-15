import sys
import os
from twilio.rest import TwilioRestClient

phoneNumber = -1

def main():
	choice = printMenu()
	while choice != 6:
		print(choice)
		if choice == 1:
			print("1 selected")
		elif choice == 2:
			print("2 selected")
		elif choice == 3:
			print("3 selected")
		elif choice == 4:
			print("4 selected")
		else:
			print("5 selected")
		choice = printMenu()


def printMenu():
	if phoneNumber == -1:
		print("\nPhone Number: NOT SET")
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