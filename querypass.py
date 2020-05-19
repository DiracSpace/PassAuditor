#!/usr/bin/env python
import requests, os, subprocess
from sys import platform

api = 'https://api.pwnedpasswords.com/range/'
gitlist = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt'

def cURL(url, h):
    query = f'curl -s {url} >> {h}.txt'
    data = subprocess.check_output(query, shell=True)
    return h
    print ('\n')

def requestLib(url, h):
    list = []
    f = open(f'{h}.txt', 'w+')
    response = requests.get(url)
    list.append(response.text)
    for line in list:
        f.write(line)
        f.close()
    return h

def searchPwn(hash):
    # need to be able to add requests
    # if it fails, try cURL
    h = hash[:5]
    url = f'{api}{h}'
    try:
        if platform == 'linux':
            answer = input('Use requests or cURL? (r/c) -> ')
            print ('\n')
            if answer == 'r':
                try:
                    return requestLib(url, h)
                except Exception as requests:
                    print ('Error, switching to cURL')
                    print ('\n')
                    return cURL(url, h)
                    print (f'Error -> {requests}')
            else:
                try:
                    return cURL(url, h)
                except Exception as curl:
                    print ('Error, switching to Requests')
                    print ('\n')
                    return requestLib(url, h)
                    print (f'Error -> {curl}')
        else:
            answer = input('Use requests or cURL? (r/c) -> ')
            print ('\n')
            if answer == 'r':
                try:
                    return requestLib(url, h)
                except Exception as requests:
                    print ('Error, switching to cURL')
                    print ('\n')
                    return cURL(url, h)
                    print (f'Error -> {requests}')
            else:
                try:
                    return cURL(url, h)
                except Exception as curl:
                    print ('Error, switching to Requests')
                    print ('\n')
                    return requestLib(url, h)
                    print (f'Error -> {curl}')
            print ('\n')
    except Exception as e:
        print (f'Search problem -> {e}')
        print ('\n')
