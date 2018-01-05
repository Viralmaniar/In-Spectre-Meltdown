#!/usr/bin/python
'''
This tool allows to check speculative execution side-channel attacks that affect many modern processors and operating systems designs. CVE-2017-5754 (Meltdown) and CVE-2017-5715 (Spectre) allows unprivileged processes to steal secrets from privileged processes. These attacks present 3 different ways of attacking data protection measures on CPUs enabling attackers to read data they shouldn't be able to. This tool is originally based on Microsoft: https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in 
Author: Viral Maniar 
Twitter: https://twitter.com/maniarviral
Github: https://github.com/Viralmaniar
LinkedIn: https://au.linkedin.com/in/viralmaniar
'''
import os, sys
import subprocess
from subprocess import check_output
import time
	
def logo():
	logo = '''
  _____             _____                 _                   __  __      _ _      _                     
 |_   _|           / ____|               | |                 |  \/  |    | | |    | |                    
   | |  _ __ _____| (___  _ __   ___  ___| |_ _ __ ___ ______| \  / | ___| | |_ __| | _____      ___ __  
   | | | '_ |______\___ \| '_ \ / _ \/ __| __| '__/ _ |______| |\/| |/ _ | | __/ _` |/ _ \ \ /\ / | '_ \ 
  _| |_| | | |     ____) | |_) |  __| (__| |_| | |  __/      | |  | |  __| | || (_| | (_) \ V  V /| | | |
 |_____|_| |_|    |_____/| .__/ \___|\___|\__|_|  \___|      |_|  |_|\___|_|\__\__,_|\___/ \_/\_/ |_| |_|
                         | |                                                                             
                         |_|                                                                             
[+] Author: Viral Maniar
[+] Twitter: @ManiarViral
[+] Description: This tool allows to check speculative execution side-channel attacks that affect many modern processors and operating systems designs. CVE-2017-5754 (Meltdown) and CVE-2017-5715 (Spectre) allows unprivileged processes to steal secrets from privileged processes. These attacks present 3 different ways of attacking data protection measures on CPUs enabling attackers to read data they shouldn't be able to. This tool is originally based on Microsoft: https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
[+] Note: Administrator privileges required
[+] Python version: 3.6.3
[+] PowerShell version: 5.1
'''
	return logo

OPTIONS = '''
1. Set Execution Policy to Unrestricted
2. Import PowerShell Module 
3. Install Spectre related Module
4. Inspect Speculation control Setting for CVE-2017-5715 [branch target injection] & CVE-2017-5754 [rogue data cache load]
5.  Exit
'''

def menu():
	while True:
		try:
			choice = str(input('\n[?] Do you want to continue? \n> ')).lower()
			if choice[0] == 'y':
				return
			if choice[0] == 'n':
				sys.exit(0)
				break
		except ValueError:
			sys.exit(0)

def checkHostWindows():
	if os.name == "nt":
		print ('[+] All good....')
	else:
		print ('[!] Please run the application on Windows machine')
		sys.exit(0)

def cmd_exectionPolicy():

	process=subprocess.Popen(["powershell","Set-ExecutionPolicy Unrestricted"], shell=False);
	result=process.communicate()[0]
	print(result)
	print ("Execution Policy is now set to unrestricted...")

def cmd_importModule():
	
	process=subprocess.Popen(["powershell","Import-Module PowerShellGet"], shell=False);
	result1=process.communicate()[0]
	print(result1)
	print ("Module Imported Successfully...")

def cmd_specModule():
	
	process=subprocess.Popen(["powershell","Install-Module SpeculationControl"], shell=False);
	result2=process.communicate()[0]
	print(result2)
	print ("Spectre Module Imported Successfully...")

def cmd_showSpeculationControl():

	process=subprocess.Popen(["powershell","Get-SpeculationControlSettings"], shell=False);
	result3=process.communicate()[0]
	print(result3)
	print ("Output printed successfully...")
		
cmds = {
	"1" : cmd_exectionPolicy,
	"2" : cmd_importModule,
	"3" : cmd_specModule,
	"4" : cmd_showSpeculationControl,
	"5" : lambda: sys.exit(0)
}

def main():
	os.system('cls')
	print (logo())
	checkHostWindows()
	try:
		while True:
			choice = input("\n%s" % OPTIONS)
			if choice not in cmds:
				print ('[!] Invalid Choice')
				continue
			cmds.get(choice)()
	except KeyboardInterrupt:
		print ('[!] Ctrl + C detected\n[!] Exiting')
		sys.exit(0)
	except EOFError:
		print ('[!] Ctrl + D detected\n[!] Exiting')
		sys.exit(0)

if __name__ == "__main__":
	main()
