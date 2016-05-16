import json
inputFile = 'Dec-07-11.json'
#inputFile = 'Dec-14-18.json'
fin = open(inputFile,'r')
lines = fin.readlines()

monday = '2015-12-07'
tuesday = '2015-12-08'
wednesday = '2015-12-09'
thursday = '2015-12-10'
friday = '2015-12-11'



symbolDict = {monday: {}, tuesday: {}, wednesday: {}, thursday: {}, friday: {}}
weekdaysDict = {}
startTime = 'T09:30'
tue1s = tuesday + startTime
wed1s = wednesday + startTime
thu1s = thursday + startTime
fri1s = friday + startTime
tueStartIndex = 0
wedStartIndex = 0
thuStartIndex = 0
friStartIndex = 0
s1 = 0
for s1 in range(0, lines.__len__() - 1):
	if(lines[s1].find(tue1s) != -1):
		break
tueStartIndex = s1

s2 = 0
for s2 in range(tueStartIndex, lines.__len__() - 1):
	if(lines[s2].find(wed1s) != -1):
		break
wedStartIndex = s2

s3 = 0
for s3 in range(wedStartIndex, lines.__len__() - 1):
	if(lines[s3].find(thu1s) != -1):
		break
thuStartIndex = s3

s4 = 0
for s4 in range(thuStartIndex, lines.__len__() - 1):
	if(lines[s4].find(fri1s) != -1):
		break
friStartIndex = s4

for i in range(0, tueStartIndex - 1):
        data = json.loads(lines[i])
        if "symbols" in data:
                for SYMBOL in data['symbols']:
                        #counting message volume of a symbol                                        
                        if SYMBOL['symbol'] in symbolDict[monday]:
                                symbolDict[monday][SYMBOL['symbol']]['count'] += 1
                        else:
                                symbolDict[monday][SYMBOL['symbol']] = SYMBOL
                                symbolDict[monday][SYMBOL['symbol']]['count'] = 1
                                symbolDict[monday][SYMBOL['symbol']]['relatedSymbol'] = {}
                                symbolDict[monday][SYMBOL['symbol']]['sentiment'] = {'bearish': 0, 'bullish': 0, 'unknown': 0}
                        #counting sentiment value
                        if data['entities']['sentiment'] is not None:
                                if data['entities']['sentiment']['basic'] == "Bearish":
                                        symbolDict[monday][SYMBOL['symbol']]['sentiment']['bearish'] += 1
                                elif data['entities']['sentiment']['basic'] == "Bullish":
                                        symbolDict[monday][SYMBOL['symbol']]['sentiment']['bullish'] += 1
                        else:
                                symbolDict[monday][SYMBOL['symbol']]['sentiment']['unknown'] += 1

for i in range(tueStartIndex, wedStartIndex - 1):
        data = json.loads(lines[i])
        if "symbols" in data:
                for SYMBOL in data['symbols']:
                        #counting message volume of a symbol                                        
                        if SYMBOL['symbol'] in symbolDict[tuesday]:
                                symbolDict[tuesday][SYMBOL['symbol']]['count'] += 1
                        else:
                                symbolDict[tuesday][SYMBOL['symbol']] = SYMBOL
                                symbolDict[tuesday][SYMBOL['symbol']]['count'] = 1
                                symbolDict[tuesday][SYMBOL['symbol']]['relatedSymbol'] = {}
                                symbolDict[tuesday][SYMBOL['symbol']]['sentiment'] = {'bearish': 0, 'bullish': 0, 'unknown': 0}
                        #counting sentiment value
                        if data['entities']['sentiment'] is not None:
                                if data['entities']['sentiment']['basic'] == "Bearish":
                                        symbolDict[tuesday][SYMBOL['symbol']]['sentiment']['bearish'] += 1
                                elif data['entities']['sentiment']['basic'] == "Bullish":
                                        symbolDict[tuesday][SYMBOL['symbol']]['sentiment']['bullish'] += 1
                        else:
                                symbolDict[tuesday][SYMBOL['symbol']]['sentiment']['unknown'] += 1

for i in range(wedStartIndex, thuStartIndex - 1):
        data = json.loads(lines[i])
        if "symbols" in data:
                for SYMBOL in data['symbols']:
                        #counting message volume of a symbol                                        
                        if SYMBOL['symbol'] in symbolDict[wednesday]:
                                symbolDict[wednesday][SYMBOL['symbol']]['count'] += 1
                        else:
                                symbolDict[wednesday][SYMBOL['symbol']] = SYMBOL
                                symbolDict[wednesday][SYMBOL['symbol']]['count'] = 1
                                symbolDict[wednesday][SYMBOL['symbol']]['relatedSymbol'] = {}
                                symbolDict[wednesday][SYMBOL['symbol']]['sentiment'] = {'bearish': 0, 'bullish': 0, 'unknown': 0}
                        #counting sentiment value
                        if data['entities']['sentiment'] is not None:
                                if data['entities']['sentiment']['basic'] == "Bearish":
                                        symbolDict[wednesday][SYMBOL['symbol']]['sentiment']['bearish'] += 1
                                elif data['entities']['sentiment']['basic'] == "Bullish":
                                        symbolDict[wednesday][SYMBOL['symbol']]['sentiment']['bullish'] += 1
                        else:
                                symbolDict[wednesday][SYMBOL['symbol']]['sentiment']['unknown'] += 1

for i in range(thuStartIndex, friStartIndex):
        data = json.loads(lines[i])
        if "symbols" in data:
                for SYMBOL in data['symbols']:
                        #counting message volume of a symbol                                        
                        if SYMBOL['symbol'] in symbolDict[thursday]:
                                symbolDict[thursday][SYMBOL['symbol']]['count'] += 1
                        else:
                                symbolDict[thursday][SYMBOL['symbol']] = SYMBOL
                                symbolDict[thursday][SYMBOL['symbol']]['count'] = 1
                                symbolDict[thursday][SYMBOL['symbol']]['relatedSymbol'] = {}
                                symbolDict[thursday][SYMBOL['symbol']]['sentiment'] = {'bearish': 0, 'bullish': 0, 'unknown': 0}
                        #counting sentiment value
                        if data['entities']['sentiment'] is not None:
                                if data['entities']['sentiment']['basic'] == "Bearish":
                                        symbolDict[thursday][SYMBOL['symbol']]['sentiment']['bearish'] += 1
                                elif data['entities']['sentiment']['basic'] == "Bullish":
                                        symbolDict[thursday][SYMBOL['symbol']]['sentiment']['bullish'] += 1
                        else:
                                symbolDict[thursday][SYMBOL['symbol']]['sentiment']['unknown'] += 1

for i in range(friStartIndex, lines.__len__() - 1):
        data = json.loads(lines[i])
        if "symbols" in data:
                for SYMBOL in data['symbols']:
                        #counting message volume of a symbol                                        
                        if SYMBOL['symbol'] in symbolDict[friday]:
                                symbolDict[friday][SYMBOL['symbol']]['count'] += 1
                        else:
                                symbolDict[friday][SYMBOL['symbol']] = SYMBOL
                                symbolDict[friday][SYMBOL['symbol']]['count'] = 1
                                symbolDict[friday][SYMBOL['symbol']]['relatedSymbol'] = {}
                                symbolDict[friday][SYMBOL['symbol']]['sentiment'] = {'bearish': 0, 'bullish': 0, 'unknown': 0}
                        #counting sentiment value
                        if data['entities']['sentiment'] is not None:
                                if data['entities']['sentiment']['basic'] == "Bearish":
                                        symbolDict[friday][SYMBOL['symbol']]['sentiment']['bearish'] += 1
                                elif data['entities']['sentiment']['basic'] == "Bullish":
                                        symbolDict[friday][SYMBOL['symbol']]['sentiment']['bullish'] += 1
                        else:
                                symbolDict[friday][SYMBOL['symbol']]['sentiment']['unknown'] += 1

#convert symbolDict to the dict we need
weeklySDict = {}
for WEEKDAY in symbolDict:
        for SYMBOL in symbolDict[WEEKDAY]:
                if SYMBOL in weeklySDict:
                    weeklySDict[SYMBOL].append({'date': WEEKDAY,
                                                            'count': symbolDict[WEEKDAY][SYMBOL]['count'],
                                                            'sentiment_value': (symbolDict[WEEKDAY][SYMBOL]['sentiment']['bullish'] - symbolDict[WEEKDAY][SYMBOL]['sentiment']['bearish']) / (symbolDict[WEEKDAY][SYMBOL]['sentiment']['bullish'] + symbolDict[WEEKDAY][SYMBOL]['sentiment']['bearish'] + symbolDict[WEEKDAY][SYMBOL]['sentiment']['unknown'])})
                else:
                    weeklySDict[SYMBOL] = []
                    weeklySDict[SYMBOL].append({'date': WEEKDAY,
                                                            'count': symbolDict[WEEKDAY][SYMBOL]['count'],
                                                            'sentiment_value': (symbolDict[WEEKDAY][SYMBOL]['sentiment']['bullish'] - symbolDict[WEEKDAY][SYMBOL]['sentiment']['bearish']) / (symbolDict[WEEKDAY][SYMBOL]['sentiment']['bullish'] + symbolDict[WEEKDAY][SYMBOL]['sentiment']['bearish'] + symbolDict[WEEKDAY][SYMBOL]['sentiment']['unknown'])})
#weeklySList = []
#for SYMBOL in weeklySDict:
#    weeklySList.append({SYMBOL: weeklySDict[SYMBOL]})

with open('linechart.json', 'w') as f:
        json.dump(weeklySDict,f)
