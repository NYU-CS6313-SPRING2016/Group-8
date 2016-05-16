import json
inputFile = 'Dec-07-11.json'
#inputFile = 'Dec-14-18.json'
fin = open(inputFile,'r')
lines = fin.readlines()

symbolDict = {'MON': {}, 'TUE': {}, 'WED': {}, 'THU': {}, 'FRI': {}}
weekdaysDict = {}
tue1s = "2015-12-08T09:30"
wed1s = "2015-12-09T09:30"
thu1s = "2015-12-10T09:30"
fri1s = "2015-12-11T09:30"
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
firStartIndex = s4

for i in range(0, tueStartIndex - 1):
        data = json.loads(lines[i])
        if "symbols" in data:
                for SYMBOL in data['symbols']:
                        #counting message volume of a symbol                                        
                        if SYMBOL['symbol'] in symbolDict['MON']:
                                symbolDict['MON'][SYMBOL['symbol']]['count'] += 1
                        else:
                                symbolDict['MON'][SYMBOL['symbol']] = SYMBOL
                                symbolDict['MON'][SYMBOL['symbol']]['count'] = 1
                                symbolDict['MON'][SYMBOL['symbol']]['relatedSymbol'] = {}
                                symbolDict['MON'][SYMBOL['symbol']]['sentiment'] = {'bearish': 0, 'bullish': 0, 'unknown': 0}
                        #counting sentiment value
                        if data['entities']['sentiment'] is not None:
                                if data['entities']['sentiment']['basic'] == "Bearish":
                                        symbolDict['MON'][SYMBOL['symbol']]['sentiment']['bearish'] += 1
                                elif data['entities']['sentiment']['basic'] == "Bullish":
                                        symbolDict['MON'][SYMBOL['symbol']]['sentiment']['bullish'] += 1
                        else:
                                symbolDict['MON'][SYMBOL['symbol']]['sentiment']['unknown'] += 1

for i in range(tueStartIndex, wedStartIndex - 1):
        data = json.loads(lines[i])
        if "symbols" in data:
                for SYMBOL in data['symbols']:
                        #counting message volume of a symbol                                        
                        if SYMBOL['symbol'] in symbolDict['TUE']:
                                symbolDict['TUE'][SYMBOL['symbol']]['count'] += 1
                        else:
                                symbolDict['TUE'][SYMBOL['symbol']] = SYMBOL
                                symbolDict['TUE'][SYMBOL['symbol']]['count'] = 1
                                symbolDict['TUE'][SYMBOL['symbol']]['relatedSymbol'] = {}
                                symbolDict['TUE'][SYMBOL['symbol']]['sentiment'] = {'bearish': 0, 'bullish': 0, 'unknown': 0}
                        #counting sentiment value
                        if data['entities']['sentiment'] is not None:
                                if data['entities']['sentiment']['basic'] == "Bearish":
                                        symbolDict['TUE'][SYMBOL['symbol']]['sentiment']['bearish'] += 1
                                elif data['entities']['sentiment']['basic'] == "Bullish":
                                        symbolDict['TUE'][SYMBOL['symbol']]['sentiment']['bullish'] += 1
                        else:
                                symbolDict['TUE'][SYMBOL['symbol']]['sentiment']['unknown'] += 1

for i in range(wedStartIndex, thuStartIndex - 1):
        data = json.loads(lines[i])
        if "symbols" in data:
                for SYMBOL in data['symbols']:
                        #counting message volume of a symbol                                        
                        if SYMBOL['symbol'] in symbolDict['WED']:
                                symbolDict['WED'][SYMBOL['symbol']]['count'] += 1
                        else:
                                symbolDict['WED'][SYMBOL['symbol']] = SYMBOL
                                symbolDict['WED'][SYMBOL['symbol']]['count'] = 1
                                symbolDict['WED'][SYMBOL['symbol']]['relatedSymbol'] = {}
                                symbolDict['WED'][SYMBOL['symbol']]['sentiment'] = {'bearish': 0, 'bullish': 0, 'unknown': 0}
                        #counting sentiment value
                        if data['entities']['sentiment'] is not None:
                                if data['entities']['sentiment']['basic'] == "Bearish":
                                        symbolDict['WED'][SYMBOL['symbol']]['sentiment']['bearish'] += 1
                                elif data['entities']['sentiment']['basic'] == "Bullish":
                                        symbolDict['WED'][SYMBOL['symbol']]['sentiment']['bullish'] += 1
                        else:
                                symbolDict['WED'][SYMBOL['symbol']]['sentiment']['unknown'] += 1

for i in range(thuStartIndex, friStartIndex):
        data = json.loads(lines[i])
        if "symbols" in data:
                for SYMBOL in data['symbols']:
                        #counting message volume of a symbol                                        
                        if SYMBOL['symbol'] in symbolDict['THU']:
                                symbolDict['THU'][SYMBOL['symbol']]['count'] += 1
                        else:
                                symbolDict['THU'][SYMBOL['symbol']] = SYMBOL
                                symbolDict['THU'][SYMBOL['symbol']]['count'] = 1
                                symbolDict['THU'][SYMBOL['symbol']]['relatedSymbol'] = {}
                                symbolDict['THU'][SYMBOL['symbol']]['sentiment'] = {'bearish': 0, 'bullish': 0, 'unknown': 0}
                        #counting sentiment value
                        if data['entities']['sentiment'] is not None:
                                if data['entities']['sentiment']['basic'] == "Bearish":
                                        symbolDict['THU'][SYMBOL['symbol']]['sentiment']['bearish'] += 1
                                elif data['entities']['sentiment']['basic'] == "Bullish":
                                        symbolDict['THU'][SYMBOL['symbol']]['sentiment']['bullish'] += 1
                        else:
                                symbolDict['THU'][SYMBOL['symbol']]['sentiment']['unknown'] += 1

for i in range(firStartIndex, lines.__len__() - 1):
        data = json.loads(lines[i])
        if "symbols" in data:
                for SYMBOL in data['symbols']:
                        #counting message volume of a symbol                                        
                        if SYMBOL['symbol'] in symbolDict['FRI']:
                                symbolDict['FRI'][SYMBOL['symbol']]['count'] += 1
                        else:
                                symbolDict['FRI'][SYMBOL['symbol']] = SYMBOL
                                symbolDict['FRI'][SYMBOL['symbol']]['count'] = 1
                                symbolDict['FRI'][SYMBOL['symbol']]['relatedSymbol'] = {}
                                symbolDict['FRI'][SYMBOL['symbol']]['sentiment'] = {'bearish': 0, 'bullish': 0, 'unknown': 0}
                        #counting sentiment value
                        if data['entities']['sentiment'] is not None:
                                if data['entities']['sentiment']['basic'] == "Bearish":
                                        symbolDict['FRI'][SYMBOL['symbol']]['sentiment']['bearish'] += 1
                                elif data['entities']['sentiment']['basic'] == "Bullish":
                                        symbolDict['FRI'][SYMBOL['symbol']]['sentiment']['bullish'] += 1
                        else:
                                symbolDict['FRI'][SYMBOL['symbol']]['sentiment']['unknown'] += 1

#convert symbolDict to the dict we need
weeklySDict = {}
for WEEKDAY in symbolDict:
        for SYMBOL in symbolDict[WEEKDAY]:
                if SYMBOL in weeklySDict:
                    weeklySDict[SYMBOL][WEEKDAY] = {'count': symbolDict[WEEKDAY][SYMBOL]['count'],
                                                                    'sentiment_value': (symbolDict[WEEKDAY][SYMBOL]['sentiment']['bullish'] - symbolDict[WEEKDAY][SYMBOL]['sentiment']['bearish']) / (symbolDict[WEEKDAY][SYMBOL]['sentiment']['bullish'] + symbolDict[WEEKDAY][SYMBOL]['sentiment']['bearish'] + symbolDict[WEEKDAY][SYMBOL]['sentiment']['unknown'])}
                else:
                    weeklySDict[SYMBOL] = {}
                    weeklySDict[SYMBOL][WEEKDAY] = {'count': symbolDict[WEEKDAY][SYMBOL]['count'],
                                                                    'sentiment_value': (symbolDict[WEEKDAY][SYMBOL]['sentiment']['bullish'] - symbolDict[WEEKDAY][SYMBOL]['sentiment']['bearish']) / (symbolDict[WEEKDAY][SYMBOL]['sentiment']['bullish'] + symbolDict[WEEKDAY][SYMBOL]['sentiment']['bearish'] + symbolDict[WEEKDAY][SYMBOL]['sentiment']['unknown'])}

weeklySList = []
for SYMBOL in weeklySDict:
    weeklySList.append({SYMBOL: weeklySDict[SYMBOL]})

with open('linechart.json', 'w') as f:
        json.dump(weeklySList,f)
