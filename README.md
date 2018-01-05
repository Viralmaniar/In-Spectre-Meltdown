# In-Spectre-Meltdown
This tool allows to check speculative execution side-channel attacks that affect many modern processors and operating systems designs. CVE-2017-5754 (Meltdown) and CVE-2017-5715 (Spectre) allows unprivileged processes to steal secrets from privileged processes. These attacks present 3 different ways of attacking data protection measures on CPUs enabling attackers to read data they shouldn't be able to. <br>
<br>
This tool is originally based on Microsoft: https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in 

![image](https://user-images.githubusercontent.com/3501170/34603779-710a93b6-f259-11e7-9707-f2145e106e46.png)

# Please note:
This solution has been tested successfully using Python 3.6.3 & PowerShell version 5.1.

# How do I use this?
- Run the python code or download the executable from the releases section and run it as an administrator user.
- Press Number 1, 2, 3 & 4 in sequence to see the results.
- Press 1: Sets the execution policy to unrestricted.
- Press 2: Imports necessary PowerShell modules
- Press 3: Installs Spectre related modules within PowerShell
- Press 4: Inspects control settings for Spectre & Meltdown and displays result
- Press 5: Exit from the program

# Do I need to run the executable as administrator?
- Yes, Right click on the "In-Spectre_meltdown.exe" and run as administrator to get the results.

# Questions?
Twitter: https://twitter.com/maniarviral <br>
LinkedIn: https://au.linkedin.com/in/viralmaniar

