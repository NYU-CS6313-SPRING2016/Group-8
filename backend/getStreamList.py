import json
rst = {}
def search(name):
    for p in rst:
        if name in p:
            return p


fin = open('Nov-16-20.json','r')

lines = fin.readlines()


for i in range (0, lines.__len__()):
	data = json.loads(lines[i])
	if data['entities']['sentiment'] is not None:
		if "symbols" in data:
			for SYMBOL in data['symbols']:
				
				if rst.get(SYMBOL['symbol']) is not None:
					#e = rst[SYMBOL['symbol']]
					if rst[SYMBOL['symbol']].__len__() < 40:
						tmp = {}
						tmp['crated_at'] = data['created_at']
						tmp['body'] = data['body']
						tmp['sentiment'] = data['entities']['sentiment']['basic']
						lst = data['symbols']
						if lst.__len__() == 1:
							tmp['symbol'] = lst[0]['symbol']
						else:
							ttmp = ""
							for j in range (0, lst.__len__() - 1):
								ttmp = ttmp + str(lst[j]['symbol']) + ', '
							ttmp = ttmp + str(lst[lst.__len__() - 1]['symbol'])
							tmp['symbol'] = ttmp
						'''if SYMBOL.__len__() == 1:
							tmp['symbol'] = SYMBOL['symbol']
						else:
							ttmp = []
							for j in range (0, SYMBOL.__len__()):
								ttmp.append(SYMBOL['symbol'])
							tmp['symbols'] = ttmp'''

						rst[SYMBOL['symbol']].append(tmp)
					else:
						break
				else:
					
					rst[SYMBOL['symbol']] = []
					




with open('stream111620.json', 'w') as f:
        json.dump(rst,f)