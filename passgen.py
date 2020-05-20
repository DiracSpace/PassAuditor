#!/usr/bin/env python
import string, random, sys

r = random.SystemRandom()

def generatePassword():
    if len(sys.argv) > 1:
        length = sys.argv[1]
        generatedpassword = ""
        charset = "¡*ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-/~!.{}[]|¿?=&#¡*$%<>°¬"
        for i in range(int(length)):
            generatedpassword += r.choice(charset)
    else:
        generatedpassword = ""
        charset = "¡*ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-/~!.{}[]|¿?=&#¡*$%<>°¬"
        for i in range(12):
            generatedpassword += r.choice(charset)

    return generatedpassword
