import sys
import os
from twilio.rest import TwilioRestClient

def main():
	#Enter your Twilio account information below:
	ACCOUNT_SID = os.environ["ACCOUNT_SID"]
	AUTH_TOKEN = os.environ["API_KEY"]
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

	client.messages.create(
		to = os.environ["TO"],
		from_ = os.environ["FROM"],
		body = "Take your multivitamins now",
	)

if __name__ == "__main__":
	main()
