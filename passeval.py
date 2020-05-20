#!/usr/bin/env python
import requests, re, json, base64, querypass
from pathlib import Path

json = json.loads(open('links.json').read())

def geturl(key):
    try:
        value = json[f'{key}']
        url = base64.b64decode(value.encode('utf-8'))
        return url.decode('utf-8').rstrip()
    except Exception as e:
        print (f'Error getting url -> {e}')
        print ('\n')
        exit()

def getList(pwd):
    try:
        print ('\n')
        answer = input('Do you want to give a custom filename? (y/N) -> ')
        if answer == 'y':
            filename = input('Input -> ')
        else:
            file = 'default'
        url = geturl("git")
        querypass.requestLib(url, filename)
        parseText(pwd)
        print ('\n')
    except Exception as e:
        print (f'Error getting list -> {e}')

def findCombinations(pwd, filename):
    combinations = []
    pattern = re.compile(f'.*{pwd}.*')
    f = open(filename, 'r')
    if f.mode == 'r':
        contents = f.read()
        result = pattern.findall(contents)
    for data in result:
        combinations.append(data)
    for index, combination in enumerate(combinations):
        print (f'{index},   {combination}')
    print ('\n')

def parseText(pwd):
    try:
        filename = Path(geturl("path"))
        if filename.exists():
            findCombinations(pwd, filename)
        else:
            filename = input('Input custom filename -> ')
            print ('\n')
            if filename != f'{filename}.txt':
                filename = filename+'.txt'
                findCombinations(pwd, filename)
            else:
                findCombinations(pwd, filename)
    except Exception as e:
        print (f'Parse text error -> {e}')
        print ('\n')
        exit()

def searchList(pwd):
    list = []
    combinations = []
    pattern = re.compile(f'.*{pwd}.*')
    url = geturl("git")
    response = requests.get(url)
    if response:
        print (f'These are similarities or combinations with {pwd}')
        result = pattern.findall(response.text)
        for data in result:
            combinations.append(data)
        for index, combination in enumerate(combinations):
            print (f'{index},   {combination}')
        print ('\n')
    else:
        print ('errr')
