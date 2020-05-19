#!/usr/bin/env python
import hashlib
from pyfiglet import Figlet
import hasher
import querypass

algorithms = ["SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "MD5"]

def banner():
    custom_fig = Figlet(font = 'big')
    print (custom_fig.renderText('PassAuditor'))
    print ('\n')
    try:
        for index, algorithm in enumerate(algorithms):
            print (f'[{index}]', algorithm)
    except Exception as e:
        print (f'Printing list problem -> {e}')
    print ('\n')

def mainProcess(pwd):
    ocurrences = []
    n = 36
    answer = input('Do you know the algorithm? (y/N) -> ')
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
        print ('How come? Let me do some processing to find out')
        # hash the same password with all methods and search

def main():
    pwd = str(input('Give me your password -> '))
    if len(pwd) == 0:
        print ('Try again, but bring a real password')
        print ('\n')
        exit()
    else:
        print ('Got it, chief!')
        print ('\n')
        mainProcess(pwd)

if __name__ == '__main__':
    banner()
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\n\n\tBye!")
            exit()
