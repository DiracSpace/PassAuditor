#!/usr/bin/env python
bad = '\033[91m[-]\033[0m'
info = '\033[93m[!]\033[0m'
good = '\033[92m[+]\033[0m'

algorithms = ["SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "MD5"]

def findHashFunction(hashvalue):
    if len(hashvalue) == 32:
        print (f'%s Hash function: {algorithms[5]}' % info)
        return 5
    elif len(hashvalue) == 40:
        print (f'%s Hash function: {algorithms[0]}' % info)
        return 0
    elif len(hashvalue) == 64:
        print (f'%s Hash function: {algorithm[2]}' % info)
        return 2
    elif len(hashvalue) == 96:
        print (f'%s Hash function: {algorithms[3]}' % info)
        return 3
    elif len(hashvalue) == 128:
        print (f'%s Hash function: {algorithms[4]}' % info)
        return 4
    else:
        print ('%s Hash not supported, try again with a supported function' % bad)
        quit()
