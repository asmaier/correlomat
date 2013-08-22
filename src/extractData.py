#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 14.09.2011

@author: andi
"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import csv
import re
import codecs
from collections import defaultdict

def readInput():
	input = codecs.open("Bayern2013/module_definition.js","r","iso-8859-1")
	return input


def generateTable(file):
	
	pattern = re.compile("WOMT_aThesen\[(\\d+)\]\[\\d+\]\[\\d+\]='(.*?)';", re.UNICODE)
	pattern2 = re.compile("WOMT_aParteien\[(\\d+)\]\[\\d+\]\[1\]='(.*?)';",re.UNICODE)
	pattern3 = re.compile("WOMT_aThesenParteien\[(\\d+)\]\[(\\d+)\]='(.*?)';",re.UNICODE)
	
	
	thesen={}
	parteien={}
	antworten=defaultdict(defaultdict)
	
	for line in file:
		m = pattern.match(line)
		m2 = pattern2.match(line)
		m3 = pattern3.match(line)
		
		if m:
			thesen[m.group(1)] = m.group(2)
		if m2:
			parteien[m2.group(1)] = m2.group(2)	
		if m3:
			these = m3.group(1)
			partei = m3.group(2)
			antwort = m3.group(3)
			
			antworten[partei][these]=antwort
			
	
	table = defaultdict(defaultdict)
	
	for partei in antworten:
		for these in antworten[partei]:
			table[thesen[these]][parteien[partei]] = antworten[partei][these]
			
	return table

def writeOutput(table):
	
	output = codecs.open("Bayern2013/table.csv","w","utf-8")
	
	writer = csv.writer(output)

	headers=[u"Thesen"]
	for key in table:
		for key2 in table[key]:
			if key2 not in headers:
				headers.append(key2)

	writer.writerow(headers)
	
	for key in table:
		row=[key]
		for key2 in table[key]:
			row.append(table[key][key2])
		writer.writerow(row)	

def analyze(antworten):
	
	correlation = defaultdict(lambda: defaultdict(int))
	
	for these in antworten:
		for partyThis in sorted(antworten[these]):
			answerThis = int(antworten[these][partyThis])	
			for partyOther in sorted(antworten[these]):
				answerOther = int(antworten[these][partyOther])
				if(answerThis == answerOther):
					correlation[partyThis][partyOther]+=1
					
	return correlation				

def writeOutput2(correlation):
	
	output = codecs.open("Bayern2013/correlation.csv","w","utf-8")
	writer = csv.writer(output)
	
	headers =["Partei"]
	
	for party in sorted(correlation):
		headers.append(party)
		
	writer.writerow(headers)
	
	for partyThis in sorted(correlation):
		row=[partyThis]
		for partyOther in sorted(correlation):
			row.append(correlation[partyThis][partyOther])
		writer.writerow(row)	
						
if __name__ == '__main__':
	file = readInput()
	table = generateTable(file)
	writeOutput(table)
	correlation = analyze(table)
	writeOutput2(correlation)