import json
inputFile = 'Dec-07-11.json'
fin = open(inputFile,'r')
lines = fin.readlines()

MON = {}
mon1e = "2015-12-07T16:00"
s1 = 0
for s1 in range(0, lines.__len__() - 1):
		if(lines[s1].find(mon1e) != -1):
			break

DayLines1 = lines[0: s1 - 1]

for i in range(0, DayLines1.__len__() - 1):
	data = json.loads(DayLines1[i])
	if "symbols" in data:
		for SYMBOL in data['symbols']:
			MON[SYMBOL] = {}
			if MON.get('count'):
				MON[SYMBOL['count']] += 1
			else:
				
				MON[SYMBOL['count']] = 1

			if data['entities']['sentiment'] is not None:
				if data['entities']['sentiment']['basic'] == "Bearish":
					MON[SYMBOL['sentiment']] -= 1
		        	
		        elif data['entities']['sentiment']['basic'] == "Bullish":
		            MON[SYMBOL['sentiment']] += 1
			else:
				MON[SYMBOL['sentiment']] = 0
    
    	

with open('tttt.json', 'w') as f:
	json.dump(MON, f)