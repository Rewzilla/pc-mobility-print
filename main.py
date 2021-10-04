#!/usr/bin/env python3

import argparse
import getpass
from pcmobilityprint import *

def main(args):

	pcmp = PCMobilityPrint(args.domain)

	if args.insecure:
		pcmp.verify_ssl = False

	if args.action == "list":

		printers = pcmp.get_printers()

		print("Printer Name             | Printer Description")
		print("-------------------------+---------------------")
		for printer in printers:
			print(f"{printer['name']:24} | {printer['description']}")

	elif args.action == "add":

		if args.username == None:
			username = input("Username: ")
		else:
			username = args.username

		if args.password == None:
			password = getpass.getpass("Password: ")
		else:
			password = args.password

		if not pcmp.authenticate(username, password):
			print("Authentication error")
			return

		url = pcmp.get_printer(args.arg[0])

		print(url)

if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument("action", help="Required positional argument")
	parser.add_argument("arg", nargs="*", help="Optional positional argument")
	parser.add_argument("-i", "--insecure", action="store_true", default=False, help="Don't verify SSL")
	parser.add_argument("-d", "--domain", action="store", dest="domain")
	parser.add_argument("-u", "--username", action="store", dest="username", default=None)
	parser.add_argument("-p", "--password", action="store", dest="password", default=None)

	args = parser.parse_args()

	main(args)
