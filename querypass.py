#!/usr/bin/env python
import requests, os, subprocess, passeval
from sys import platform

def cURL(url, h):
    query = f'curl -s {url} >> {h}.txt'
    data = subprocess.check_output(query, shell=True)
    return h
    print ('\n')

def requestLib(url, h):
    list = []
    f = open(f'{h}.txt', 'w+')
    response = requests.get(url)
    if response:
        list.append(response.text)
        for line in list:
            f.write(line)
            f.close()
        return h
    else:
        print ('Error in query')

def searchPwn(hash):
    h = hash[:5]
    url = f'{passeval.geturl("api")}{h}'
    try:
        if platform == 'linux':
            answer = input('Use requests or cURL? (r/c) -> ')
            print ('\n')
            if answer == 'r':
                try:
                    return requestLib(url, h)
                except Exception as requests:
                    print (f'Error -> {requests}, switching to cURL')
                    print ('\n')
                    return cURL(url, h)
            else:
                try:
                    return cURL(url, h)
                except Exception as curl:
                    print (f'Error -> {curl}, switching to Requests')
                    print ('\n')
                    return requestLib(url, h)
        else:
            answer = input('Use requests or cURL? (r/c) -> ')
            print ('\n')
            if answer == 'r':
                try:
                    return requestLib(url, h)
                except Exception as requests:
                    print (f'Error -> {requests}, switching to cURL')
                    print ('\n')
                    return cURL(url, h)
            else:
                try:
                    return cURL(url, h)
                except Exception as curl:
                    print (f'Error -> {curl}, switching to Requests')
                    print ('\n')
                    return requestLib(url, h)
            print ('\n')
    except Exception as e:
        print (f'Search problem -> {e}')
        print ('\n')
