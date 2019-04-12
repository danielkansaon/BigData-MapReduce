#Daniel Pimentel e Diogo Aguilar
from stopwords import allStopWords
import mincemeat  
import codecs
import glob
import csv
import os

path_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
text_files = os.listdir(path_data)

def file_content(file_name):
	f = open(os.path.join(path_data, file_name), encoding="utf8")
	try:
		return f.read()
	finally:
		f.close()
	
datasource = dict((file_name, file_content(file_name)) for file_name in text_files)

def mapfn(k, v):    
    print('map ' + k)
    for line in v.split('\n'):
        if line:            
            fields = line.split(':::')
            authors = fields[1].split('::')
            words = fields[2].split(' ')
            for author in authors:
                for word in words:
                    if word not in allStopWords.keys():                        
                        yield (author, word)


def reducefn(k, v):
    print('reduce ' + k)
    return sum(v)  

s = mincemeat.Server()

s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password='changeme')
w = csv.writer(open(os.path.dirname(os.path.realpath(__file__)) +  "\\result.csv", "w"))

all_author = [all_author for all_author in results.keys()]

for author in all_author:
    if author in results.keys():
        for k, v in results[author].items():
            w.write("\"{}\";\"{}\";\"{}\"\n".format(author, k, v))
    
        amount = [value for value in results[author].values()]
        amount.sort()
        max_values = amount[-2:]

w.close()   