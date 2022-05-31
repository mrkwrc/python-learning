#! python3
# StrongPasswordDetection.py - check if password is strong enough.

import re

passwrdRegex = re.compile(r'''(
    ^
    (?=.*[A-Z])            # at least 1 capital letter
    (?=.*[0-9])            # at least 1 numeric digit
    (?=.*[a-z])            # at least 1 lowercase letter
    .{8,}                  # length is at least 8
	$
    )''', re.VERBOSE)

def StrongPasswordDetection():	
    match = passwrdRegex.search(input())
    if match == None:
        print('weak password')
        StrongPasswordDetection()
        return False
    else:
        print('strong enough password (use for test only)')
        return True
        
StrongPasswordDetection()
