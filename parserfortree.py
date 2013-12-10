###################################################
# File brennanparser.py
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

svmfile = open('trainsvm', 'w')

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
    when = [float(i) for i in trainvaluelist[13:28]] ######################
    index = when.index(max(when))
    tweet = trainvaluelist[1]
    vec = np.array(buildFeatureVector(tweet))
    s.append((vec,index))
    zeroDict()

pickle.dump(s, open("Brennan/kind.p", "wb")) ######################
pickle.dump(when_dict.keys(), open("Brennan/kind_dict_words.p", "wb")) ######################

#print whenwords
#print trainvaluelist
#print tweet
#print when_dict['gt']
#print tweet.split(" ")
#print vec
#print df
#print np.array(vec)
print s[(len(alltraindata)-4):]

print when_dict.keys()
print len(when_dict)

infile1.close()
infile2.close()
svmfile.close()
