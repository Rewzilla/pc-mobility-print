
import json
import ssl
import socket
import base64
import urllib.request
import subprocess

class PCMobilityPrint:

	def __init__(self, server=None, domain=None):

		if server:
			self.host = server
		else:
			self.host = self.resolve_host(domain)

		# TODO: Error checking if host resolve failed

		self.socket = f"{self.host}:9164"
		self.baseurl = f"https://{self.socket}"
		self.username = None
		self.password = None
		self.verify_ssl = True

	def resolve_host(self, domain):

		try:

			d = "rpc.pc-printer-discovery"
			h = socket.gethostbyname(d)
			if h != None:
				return d

			for i in range(1, 21):
				d = f"rpc.pc-printer-discovery-{i}"
				h = socket.gethostbyname(d)
				if h != None:
					return d

			if domain is not None:

				d = f"rpc.pc-printer-discovery.{domain}"
				h = socket.gethostbyname(d)
				if h != None:
					return d

				for i in range(1, 21):
					d = f"rpc.pc-printer-discovery-{i}.{domain}"
					h = socket.gethostbyname(d)
					if h != None:
						return d

		except:

			return None

	def get_printers(self):

		# TODO: Error checking if host not set

		if self.verify_ssl:
			p = urllib.request.urlopen(f"{self.baseurl}/printers")
		else:
			ctx = ssl._create_unverified_context()
			p = urllib.request.urlopen(f"{self.baseurl}/printers", context=ctx)

		return json.loads(p.read())

	def	authenticate(self, username, password):

		# TODO: Error checking if host not set

		# https://stackoverflow.com/a/26236748
		if self.verify_ssl:
			ctx = ssl.create_default_context()
		else:
			ctx = ssl._create_unverified_context()

		b64creds = base64.b64encode(f"{username}:{password}".encode()).strip().decode()

		try:

			req = urllib.request.Request(f"{self.baseurl}/printer-url?printerName=AuthCheckThisShouldntExist&serverName=AuthCheckThisShouldntExist")
			req.add_header("Authorization", f"Basic {b64creds}")
			p = urllib.request.urlopen(req, context=ctx)

		except urllib.error.HTTPError as e:

			if e.code == 404:
				self.username = username
				self.password = password
				return True
			else:
				return False

	def get_printer(self, name):

		# TODO: Error checking if host not set
		# TODO: Error checking if not authenticated

		if self.verify_ssl:
			ctx = ssl.create_default_context()
		else:
			ctx = ssl._create_unverified_context()

		b64creds = base64.b64encode(f"{self.username}:{self.password}".encode()).strip().decode()

		try:

			req = urllib.request.Request(f"{self.baseurl}/printer-url?printerName={name}&serverName={self.socket}")
			req.add_header("Authorization", f"Basic {b64creds}")
			p = urllib.request.urlopen(req, context=ctx)

			return p.read().decode()

		except urllib.error.HTTPError as e:

			# TODO: better error handling
			return None

	def get_description(self, name):

		# TODO: Error checking if host not set

		printers = self.get_printers()

		for p in printers:
			if p["name"] == name:
				return p["description"]

		return False

	def add_printer(self, name):

		# TODO: Error checking if host not set
		# TODO: Error checking if not authenticated

		url = self.get_printer(name)
		desc = self.get_description(name)

		# TODO: Error checking if printer not found

		if not url:
			return False

		try:

			# TODO: -L<location> and -D<description> may not always be the same thing
			cmd = ["/usr/sbin/lpadmin", "-p", name, "-E", "-L", desc, "-D", desc, "-v", url]
			subprocess.call(cmd)

			return True

		except:

			# TODO: better error handling
			return False
