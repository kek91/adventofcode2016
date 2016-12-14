# adventofcode.com
# Day 5 - Part 1
# github.com/kek91

import hashlib

doorid = "wtnhxymk"
password = ""

for i in range(300000,2147483647):
    string = doorid + str(i)
    md5hash = hashlib.md5(string.encode('utf-8')).hexdigest()
    if(md5hash[:5] == "00000"):
        password += md5hash[5:6]
    if i % 100 == 0:
        print("Bruteforce progress: " + password)


print("\n\n\tBruteforce progress: " + password)

'''
2414bc77
'''
