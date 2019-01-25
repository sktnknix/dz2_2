# -*- coding: utf-8 -*-

import json
import chardet
import wikipedia

class Wiki:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            self.start += 1
            return self.start - 1

def get_countries():
    with open('countries.json', 'rb') as jfile:
        desc = []
        jdata = jfile.read()
        enc = chardet.detect(jdata)
        data = jdata.decode(encoding=enc['encoding'])
        jdict = json.loads(data)
        for dicts in jdict:
            desc.append(dicts['name']['common'])
    return desc

if __name__ == '__main__':
    countries = get_countries()
    start, end = 0, len(countries) - 1
    for country in Wiki(start, end):
        try:
            url = wikipedia.page(countries[country]).url
        except wikipedia.exceptions.DisambiguationError:
            url = 'https://en.wikipedia.org/wiki/' + str(countries[country]) + '_(country)'
        with open('result.txt', 'a', encoding='utf-8') as res_file:
            res_file.write(str(countries[country]) + ': ' + url + '\n')
            print(str(countries[country]) + ': ' + url)

