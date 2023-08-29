#!/usr/bin/env python3

import argparse
import getpass
from pcmobilityprint import *

def main(args):

	pcmp = PCMobilityPrint(server=args.server, domain=args.domain)

	if args.verify_ssl:
		pcmp.verify_ssl = True
	else:
		pcmp.verify_ssl = False

	if args.action == "list":

		printers = pcmp.get_printers()

		print("Printer Name             | Printer Description")
		print("-------------------------+---------------------")
		for printer in printers:
			print(f"{printer['name']:24} | {printer['description']}")

	elif args.action == "get":

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

	elif args.action == "desc":

		desc = pcmp.get_description(args.arg[0])
		print(desc)

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

		pcmp.add_printer(args.arg[0])

if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument("action", help="list, get, desc, add")
	parser.add_argument("arg", nargs="*", help="i.e. 'action <printername>'")
	parser.add_argument("-t", "--verifytls", action="store_true", default=False, dest="verify_ssl", help="Verify server TLS certificate")
	parser.add_argument("-s", "--server", action="store", dest="server", default=None)
	parser.add_argument("-d", "--domain", action="store", dest="domain", default=None)
	parser.add_argument("-u", "--username", action="store", dest="username", default=None)
	parser.add_argument("-p", "--password", action="store", dest="password", default=None)
	parser.add_argument("-v", "--version", action="version", version=version)

	args = parser.parse_args()

	main(args)
