import json
def processJson(inputFile,outputFile):
	print('start')
	fin = open(inputFile,'r')
	fout = open(outputFile,'w')
	lines = fin.readlines()

	mon1s = "2015-11-16T09:30"
	mon1e = "2015-11-16T16:00"
	tue1s = "2015-11-17T09:30"
	tue1e = "2015-11-17T16:00"
	wed1s = "2015-11-18T09:30"
	wed1e = "2015-11-18T16:00"
	thu1s = "2015-11-19T09:30"
	thu1e = "2015-11-19T16:00"
	fri1s = "2015-11-20T09:30"
	fri1e = "2015-11-20T16:00"

	s1 = e1 = s2 = e2 = s3 = e3 = s4 = e4 = s5 = e5 = 0

	for s1 in range(0, lines.__len__() - 1):
	 	if(lines[s1].find(mon1s) != -1):
			break

	for e1 in range(s1, lines.__len__() - 1):
	 	if(lines[e1].find(mon1e) != -1):
			break

	for s2 in range(e1, lines.__len__() - 1):
	 	if(lines[s2].find(tue1s) != -1):
			break

	for e2 in range(s2, lines.__len__() - 1):
	 	if(lines[e2].find(tue1e) != -1):
			break		

	for s3 in range(e2, lines.__len__() - 1):
	 	if(lines[s3].find(wed1s) != -1):
			break

	for e3 in range(s3, lines.__len__() - 1):
	 	if(lines[e3].find(wed1e) != -1):
			break

	for s4 in range(e3, lines.__len__() - 1):
	 	if(lines[s4].find(thu1s) != -1):
			break

	for e4 in range(s4, lines.__len__() - 1):
	 	if(lines[e4].find(thu1e) != -1):
			break

	for s5 in range(e4, lines.__len__() - 1):
	 	if(lines[s5].find(fri1s) != -1):
			break

	for e5 in range(s5, lines.__len__() - 1):
		if(lines[e5].find(fri1e) != -1):
			break

	
	Mon = lines[s1: e1 - 1]
	Tue = lines[s2: e2 - 1]
	Wed = lines[s3: e3 - 1]
	Thu = lines[s4: e4 - 1]
	Fri = lines[s5: e5 - 1]


	
	
	
	for i in range(0, Mon.__len__() - 1):
		fout.writelines(Mon[i])
		
	for i in range(0, Tue.__len__() - 1):
		fout.writelines(Tue[i])

	for i in range(0, Wed.__len__() - 1):
		fout.writelines(Wed[i])

	for i in range(0, Thu.__len__() - 1):
		fout.writelines(Thu[i])

	for i in range(0, Fri.__len__() - 1):
		fout.writelines(Fri[i])

	fin.close()
	fout.close()

processJson('stocktwits_messages_2015-01-01-2015-12-31.json','Nov-16-20.json')
print('finish')