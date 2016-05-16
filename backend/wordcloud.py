import json
from collections import Counter
import re
commonList = ["", "the","and","to","poop","i","me","my","myself","we","us","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","whose","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing,will,would","should,can","could","ought","a","co","39","of","at","for","in","at","on","s","t","will","not","up","no","with","but","buy","if","from","1","new","just","today","news","now","by","2","12","15","m","as","so","can","or","all","time","about","see","going","here","0","3","d","already","http","7","4","10","u","00","5","8","an","some","one","day","k","go","think"]
keyword={}
topwords = 40
txt = ""

def openfile(filename):
    fh = open(filename, "r+")
    str = fh.read()
    fh.close()
    return str

def removegarbage(str):
    # Replace one or more non-word (non-alphanumeric) chars with a space
    str = re.sub(r'\W+', ' ', str)
    str = str.lower()
    return str
 
def getwordbins(words):
    cnt = Counter()
    for word in words:
        if word not in commonList:
            cnt[word] += 1
    return cnt

#filename = 'Nov-16-20.json'
filename = 'Dec-30-04.json'
fin = open(filename,'r')
lines =  fin.readlines()

wordSDict = {}      #words counts of Symbols
for i in range(0, lines.__len__() - 1):
    data = json.loads(lines[i])
    txt = removegarbage(data['body'])
    words = txt.split(' ')
    bins = getwordbins(words)
    if "symbols" in data:
        for SYMBOL in data['symbols']:
            if SYMBOL['symbol'] in wordSDict:
                wordSDict[SYMBOL['symbol']] += bins
            else:
                wordSDict[SYMBOL['symbol']] = Counter()
                wordSDict[SYMBOL['symbol']] += bins


truncatedWordSDict = {}
wholeWeekBin = Counter()
for SYMBOL in wordSDict:
    wholeWeekBin += wordSDict[SYMBOL]
    truncatedWordSDict[SYMBOL] = []
    for word, count in wordSDict[SYMBOL].most_common(topwords):
        truncatedWordSDict[SYMBOL].append({'text': word, 'size': count})

#with open('wordCloudData120711.json', 'w') as f:
with open('wordCloudData123004.json', 'w') as f:
    json.dump(truncatedWordSDict, f)

for key, value in wholeWeekBin.most_common(topwords):
    keyword[key]=value

keywordList = []
for TEXT in keyword:
    keywordList.append({'text': TEXT, 'size': keyword[TEXT]})

#with open('wordCloudWeek111620.json', 'w') as f:
with open('wordCloudWeek123004.json', 'w') as f:
    json.dump(keywordList, f)