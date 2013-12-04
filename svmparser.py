###################################################
# File svmparser.py
###################################################

#import numpy as np
#import pandas as pd

infile1 = open('whenWords.txt', 'r')
line = infile1.readline().strip()
line = line[1:-1]
whenwords = line.split("\', \'")
#allsubdata = [line.strip() for line in infile1]

when_dict = {}

for word in whenwords:
	when_dict[word] = 0

infile2 = open('trainV2')
alltraindata = [line.strip() for line in infile2]

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
    tweet = trainvaluelist[1]
    print tweet
    vec = buildFeatureVector(tweet)
    print vec
    zeroDict()


#print whenwords
print trainvaluelist
print tweet
print when_dict['gt']
print tweet.split(" ")
#print vec
#print df