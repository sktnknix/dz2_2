# -*- coding: utf-8 -*-

from hashlib import md5

def hash_strings(file):
    start = 0
    with open(file) as f:
        list_strings = f.readlines()
    end = len(list_strings) - 1
    while start < end:
        hs = md5((list_strings[start]).encode('utf-8')).hexdigest()
        yield start, hs
        start += 1

if __name__ == '__main__':
    file = 'countries.json'
    for start, hash in hash_strings(file):
        print(str(start) + ': ' + hash)