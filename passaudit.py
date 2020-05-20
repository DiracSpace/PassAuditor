#!/usr/bin/env python
import hashlib, hasher, querypass, passgen, identifier, passeval
from pyfiglet import Figlet

options = ["Check pwnd password", "Eval your password", "Generate a new password", "Try to crack a hash", "Try to find hash function"]
algorithms = ["SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "MD5"]

def banner():
    custom_fig = Figlet(font = 'big')
    print (custom_fig.renderText('PassAuditor'))
    print ('\n')

def printAlgorithms():
    try:
        for index, algorithm in enumerate(algorithms):
            print (f'[{index}]', algorithm)
    except Exception as e:
        print (f'Printing list problem -> {e}')
    print ('\n')

def printOptions():
    try:
        for index, option in enumerate(options):
            print (f'[{index}]', option)
    except Exception as e:
        print (f'Printing options problem -> {e}')
    print ('\n')

def mainProcess(pwd):
    printAlgorithms()
    ocurrences = []
    n = 36
    answer = input('Do you want to try a hash function? (y/N) -> ')
    if answer == 'y':
        try:
            # need to search local space to see if file exists
            # else, do the search
            # also, add date to start of file
            # if it's too back, than do new search
            algorithm = algorithms[int(input('Number of algorithm -> '))]
            print ('\n')
            print (f'The algorithm is {algorithm} and your password is {pwd}')
            encryption = hasher.algorithmSelection(algorithm, pwd)
            print (f'Final encryption is {encryption}')
            print ('\n')
            try:
                file = querypass.searchPwn(str(encryption))

                # need to be able to detect file before trying to read
                hashes = open(f'{file}.txt').read().splitlines()

                for string in hashes:
                    ocurrences.append(int(string[n:]))

                counts = sum(ocurrences)
                print (f'Posible ocurrences of hash -> {counts}')
                print (f'File generated for cracking -> {file}.txt\n')
            except Exception as r:
                print (f'Results problem -> {r}')
        except Exception as e:
            print (f'Algorithm problem -> {e}')
            print ('\n')
    else:
        try:
            print ('\n')
            print (f'The default algorithm is SHA1 and your password is {pwd}')
            encryption = hasher.algorithmSelection(algorithms[0], pwd)
            print (f'Final encryption is {encryption}')
            print ('\n')
            try:
                file = querypass.searchPwn(str(encryption))

                # need to be able to detect file before trying to read
                hashes = open(f'{file}.txt').read().splitlines()

                for string in hashes:
                    ocurrences.append(int(string[n:]))

                counts = sum(ocurrences)
                print (f'Posible ocurrences of hash -> {counts}')
                print (f'File generated for cracking -> {file}.txt\n')
            except Exception as r:
                print (f'Results problem -> {r}')
        except Exception as e:
            print (f'Algorithm problem -> {e}')
            print ('\n')

def main():
    printOptions()
    option = int(input('What ya wanna do? '))
    print ('\n')
    if option == 0:
        pwd = str(input('Give me your password -> '))
        if len(pwd) == 0:
            print ('Try again, but bring a real password')
            print ('\n')
            exit()
        else:
            print ('Got it, chief!')
            print ('\n')
            mainProcess(pwd)
            exit()
    elif option == 1:
        pwd = str(input('Give me your password -> '))
        answer = input('Do you want to download list? (y/N) -> ')
        print ('\n')
        try:
            if answer == 'y':
                passeval.getList(pwd)
            else:
                print ('On it, man')
                passeval.searchList(pwd)
        except Exception as e:
            print (f'Password eval problem -> {e}')
            print ('\n')
    elif option == 2:
        print ('This is what I got, bruh -> ', passgen.generatePassword())
        print ('\n')
    elif option == 3:
        print ('Not finished, dude')
        print ('\n')
    elif option == 4:
        print ('How come? Let me do some processing to try and guess')
        print ('\n')
        pwd = str(input('Give me your hash -> '))
        result = identifier.findHashFunction(pwd)
        print ('Searching up')
        print ('\n')
    else:
        print ('Not an option, bruh')
        exit()

if __name__ == '__main__':
    banner()
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\n\n\tBye!")
            exit()
