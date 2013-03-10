php-eval-shell
==============

PHP Eval() Shell and Testing Kit
v1.0.0
Created by infodox - Insecurety Research
http://insecurety.net/

This is designed to be a rather simple way to remotely check (via an uploaded "eval() shell")
which of PHP's "system" functions are available to a remote attacker during a pentest.

tester.py takes the URL of the uploaded shell as its only arguement, and tells you which functions
seem to be enabled, and which appear to be disabled. It does this in a bruteforce manner.

shell.py takes the URL of the uploaded shell, and offers you a selection of different code execution
methods to use. It then emulates a "terminal" on the remote host, giving you command execution.

The reason for writing this software was as a possible extension for "webhandler".
If you want a *real* PHP backdooring framework, check out webhandler or Weevely.
github.com/epinna/Weevely
github.com/lnxg33k/webhandler

Maybe I will develop this some more, maybe not. It was as a test.
~infodox

LICENCE: "Buy Me A Beer and Give Me Credit" licence. i.e. if you like it, consider getting me a beer
if we ever meet, and if you reuse this code in some project, give credit (or beer!) ;)
