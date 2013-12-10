###################################################
# File brennanparser.py
###################################################

import numpy as np
#import pandas as pd
import cPickle as pickle

filenum = '15'
elemkind = 27

infile1 = open('Important_Word_Output/kindWords'+filenum, 'r') ######################
line = infile1.readline().strip()
whenwords = line.split(", ")

infile2 = open('trainV2')
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
    #when = [float(i) for i in trainvaluelist[13:28]]
    #index = when.index(max(when))
    whenkind = float(trainvaluelist[elemkind]) ######################
    if whenkind >= 0.7:
    	classkind = 1
    else: classkind = 0
    tweet = trainvaluelist[1]
    vec = np.array(buildFeatureVector(tweet))
    s.append((vec,classkind))
    zeroDict()

print trainvaluelist
#print when
#print index
print whenkind
print classkind
print tweet
print vec


pickle.dump(s, open("Brennan/kind"+filenum+".p", "wb")) ######################
pickle.dump(when_dict.keys(), open("Brennan/kind_dict_words"+filenum+".p", "wb")) ######################

#print trainvaluelist
#print tweet
#print when_dict['gt']
#print tweet.split(" ")
#print vec
#print df
#print np.array(vec)


#print s[(len(alltraindata)-4):]
print when_dict.keys()
#print len(when_dict)

infile1.close()
infile2.close()
