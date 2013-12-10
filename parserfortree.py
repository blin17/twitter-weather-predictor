###################################################
# File brennanparser.py
###################################################

import numpy as np
#import pandas as pd
import cPickle as pickle

filenum = '1'
#elemkind = 27

infile1 = open('Important_Word_Output/kindWords'+filenum, 'r') 
line = infile1.readline().strip()
whenwords = line.split(", ")

infile2 = open('trainingSetTweetsV2')
alltraindata = [line.strip() for line in infile2]

when_dict = {}
s = []

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

for k in range(len(alltraindata)):
    trainvaluelist = [i for i in alltraindata[k].split(",")]
    print trainvaluelist
    #when = [float(i) for i in trainvaluelist[13:28]]
    #index = when.index(max(when))
    #whenkind = float(trainvaluelist[elemkind]) 
    #if whenkind >= 0.7:
    #	classkind = 1
    #else: classkind = 0
    tweet = trainvaluelist[1]
    vec = np.array(buildFeatureVector(tweet))
    #s.append((vec,classkind))
    s.append(vec)
    zeroDict()

#pickle.dump(s, open("Brennan/kind"+filenum+".p", "wb")) ######################
##pickle.dump(when_dict.keys(), open("Brennan/kind_dict_words"+filenum+".p", "wb")) ######################


infile1.close()
infile2.close()
