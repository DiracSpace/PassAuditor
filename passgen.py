#!/usr/bin/env python
import string, random, sys, passeval, re, requests

r = random.SystemRandom()

bad = '\033[91m[-]\033[0m'
info = '\033[93m[!]\033[0m'
good = '\033[92m[+]\033[0m'

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

def printCool(numbers):
    if numbers[1] >= '17':
        print (f'%s Your password is {numbers[0]} characters long' % info)
        print (f'%s With a total of {numbers[1]} combinations' % info)
        print (f'%s It will take {numbers[2]} hours or {numbers[3]} days to brute force your password' % info)
        print (f'%s A computer that trys {numbers[4]} passwords per hour' % info)
    elif numbers[1] > '20':
        print (f'%s Your password is {numbers[0]} characters long' % good)
        print (f'%s With a total of {numbers[1]} combinations' % good)
        print (f'%s It will take {numbers[2]} hours or {numbers[3]} days to brute force your password' % good)
        print (f'%s A computer that trys {numbers[4]} passwords per hour' % good)
    elif numbers[1] < '10':
        print (f'%s Your password is {numbers[0]} characters long' % bad)
        print (f'%s With a total of {numbers[1]} combinations' % bad)
        print (f'%s It will take {numbers[2]} hours or {numbers[3]} days to brute force your password' % bad)
        print (f'%s A computer that trys {numbers[4]} passwords per hour' % bad)

def passTimeDefiner(pwd):
    p = re.compile('<p>(.*?)</p>')
    b = re.compile('<b>(.*?)</b>')
    special = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    try:
        uc = sum(1 for c in pwd if c.isupper())
        lc = sum(1 for c in pwd if c.islower())
        nu = sum(c.isdigit() for c in pwd)
        sc = special.findall(pwd)
        sc = len(sc)
        ran = 0
        ransc = 0
        dt = 0
        #url = passeval.geturl("eval")
        url = f'https://tmedweb.tulane.edu/content_open/bfcalc.php?uc={uc}&lc={lc}&nu={nu}&sc={sc}&ran={ran}&rans={ransc}&dict={dt}'
        response = requests.get(url)
        if response:
            numbers = b.findall(str(p.findall(response.text)))
            printCool(numbers)
        else:
            print ("Didn't get a response")
            exit()
        print ('\n')
    except Exception as e:
        print (f'Password strength definer problem -> {e}')
        print ('\n')
        exit()
