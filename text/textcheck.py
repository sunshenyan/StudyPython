#!/usr/bin/env python
# _*_ coding:utf8 _*_

import sys,json,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

fr = open('红楼梦.txt','r',encoding='utf8')

characers=[]
stat={}

for line in fr:
	line=line.strip()
	if len(line)==0:
		continue

	for x in range(0,len(line)):
		#print(line[x])
		if line[x] in [' ','，','。','','．','：','“','”','"','？','！','\'','`','　','《','》','—','_']:
			continue

		if line[x] not in characers:
			characers.append(line[x])
		
		if not line[x] in stat:
			stat[line[x]]=0
		stat[line[x]]+=1

	
fr.close()

fw=open('result.json','w')
fw.write(json.dumps(stat))
fw.close()

stat=sorted(stat.items(),key=lambda d:d[1],reverse=True)
#for key,value in enumerate(stat):
#	print (key,value)
fw=open('result.csv','w')
for item in stat:
	fw.write(item[0]+','+str(item[1])+'\n')
fw.close()

