# -*- coding: utf-8 -*-

import json
import chardet
import wikipedia

class Wiki:
    def __init__(self, countries, start, end):
        self.countries = countries
        self.start = start
        self.end =end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            try:
                url = wikipedia.page(self.countries[self.start]).url
            except wikipedia.exceptions.DisambiguationError:
                url = 'https://en.wikipedia.org/wiki/' + str(self.countries[self.start]) + '_(country)'
            self.start += 1
            return self.countries[self.start], url


if __name__ == '__main__':
    with open('countries.json', 'rb') as jfile:
        desc = []
        jdata = jfile.read()
        enc = chardet.detect(jdata)
        data = jdata.decode(encoding=enc['encoding'])
        jdict = json.loads(data)
        for dicts in jdict:
            desc.append(dicts['name']['common'])
    for country, url in Wiki(desc, 0, len(desc) - 1):
        with open('result.txt', 'a', encoding='utf-8') as res_file:
            res_file.write(str(country) + ': ' + url + '\n')
            print(str(country) + ': ' + url)

