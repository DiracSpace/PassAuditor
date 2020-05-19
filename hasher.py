#!/usr/bin/env python
import hashlib

def sha1(pwd):
    hash = hashlib.sha1(pwd.encode('UTF-8')).hexdigest()
    return hash
def sha224(pwd):
    hash = hashlib.sha224(pwd.encode('UTF-8')).hexdigest()
    return hash
def sha256(pwd):
    hash = hashlib.sha256(pwd.encode('UTF-8')).hexdigest()
    return hash
def sha384(pwd):
    hash = hashlib.sha384(pwd.encode('UTF-8')).hexdigest()
    return hash
def sha512(pwd):
    hash = hashlib.sha512(pwd.encode('UTF-8')).hexdigest()
    return hash
def md5(pwd):
    hash = hashlib.md5(pwd.encode('UTF-8')).hexdigest()
    return hash

def algorithmSelection(algorithm, pwd):
    try:
        if algorithm == "SHA1":
            return sha1(pwd)
        elif algorithm == "SHA224":
            return sha224(pwd)
        elif algorithm == "SHA256":
            return sha256(pwd)
        elif algorithm == "SHA384":
            return sha384(pwd)
        elif algorithm == "SHA512":
            return sha512(pwd)
        elif algorithm == "MD5":
            return md5(pwd)
        else:
            print ('Nothing')
    except Exception as e:
        print (f'Hasher problem -> {e}')
