###################################################
# File svmparser.py
###################################################

import numpy as np
#import pandas as pd
import cPickle as pickle

infile1 = open('kindWords.txt', 'r') ######################
line = infile1.readline().strip()
line = line[1:-1]
whenwords = line.split("\', \'")
infile2 = open('trainV2')
alltraindata = [line.strip() for line in infile2]
svmfile = open('svmfiles/trainsvmkind14', 'w') #####################
svmvalfile = open('svmfiles/trainsvmkind14val', 'w') #####################

when_dict = {}
index_dict = {}

def buildIndexDict():
	i = 0
	for word in whenwords:
		index_dict[word] = i
		i += 1

def buildWhenDict():
	for word in whenwords:
		when_dict[word] = 0

def zeroDict():
	for key in when_dict:
		when_dict[key] = 0

def buildFeatureVector(tweet):
	tweetwords = tweet.split(" ")
	for word in tweetwords:
		if (word in when_dict):
			when_dict[word] += 1
	return (when_dict.values())

def buildsvmline(tweet, classification):
	tweetwords = tweet.split(" ")
	if classification == 14: ###############################
		s = "1"
	else: s = "-1"
	#s = `classification`
	for word in tweetwords:
		if word in when_dict:
			when_dict[word] += 1
	for i in range(len(whenwords)):
		count = when_dict[whenwords[i]]
		if count > 0:
			if i != index_dict[whenwords[i]]:
				print " WHATS THE"
			s = s + " " + `(i+1)` + ":" + `count`
	return s

###########################################################################
# CODE SEQUENCE

buildIndexDict()
buildWhenDict()


g = 1
for k in range(len(alltraindata)):
    trainvaluelist = [i for i in alltraindata[k].split(",")]
    when = [float(i) for i in trainvaluelist[13:28]] ######################
    index = when.index(max(when))
    tweet = trainvaluelist[1]
    #print tweet, when
    #vec = buildFeatureVector(tweet)
    svmstr = buildsvmline(tweet, index)
    if g < 60000:
    	svmfile.write(svmstr + "\n")
    else:
    	svmvalfile.write(svmstr + "\n")
    zeroDict()

#print vec
#print whenwords[885]

infile1.close()
infile2.close()
svmfile.close()
svmvalfile.close()
