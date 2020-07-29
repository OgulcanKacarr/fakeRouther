import os
import subprocess as sub
import time
import wget
from Func import func

os.system("clear")

print("""  

		[1] Hostapd-attack
		[2] Install

				

		""")
	
user_input = int(input("Please Select a Function: "))
if user_input == 1:
	func.hostapd_attack()
elif user_input == 2:
	func.installer()
	
		



	
	

	


	
















