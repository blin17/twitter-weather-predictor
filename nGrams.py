
import sys
import time
import math
import random

labelCounts= [0]*39
labelWords= [{} for i in xrange(39)]
numWordsPerLabel= [0]*39
vocabulary= set([])
gramsWeights= {}
kindThresh= 0.7
numExamples= 0

#need to give different weight to different grams in classify method
#may need to change the way "binarizeKind" is implemented

def parse(train, grams):
  global numExamples
  with open(grams) as f1: 
    for i,line in enumerate(f1):
      if len(line)>1:
      	lst= line.split(" ")
      	gramsWeights[int(lst[0])]= int(lst[1])

  with open(train) as f2: 
    for i,line in enumerate(f2):
      if len(line)>1:
      	numExamples += 1
      	line= line[:-2]
        lst= line.split(",")
        lst= lst[:4]+binarize(lst[4:])
        #print i, lst
        updateCounts(lst[1], lst[4:])

def updateCounts(tweet, labels):
	for gram in gramsWeights:
		words= tweet.split(" ")
		newWords= []
		if len(words) >= gram:
			string= ""
			for grouping in range(len(words)-gram+1):
				for i,elem in enumerate(range(gram)):
					if i==gram-1: string += words[elem+grouping]
					else:  string += words[elem+grouping]+" "
				newWords += [string]
				string= ""
			vocabulary.update(newWords)
			for i,label in enumerate(labels):
				if i<9:	
					if label==1: 
						labelCounts[i] += 1
						numWordsPerLabel[i] += len(tweet)
						for word in newWords:
							if word in labelWords[i]: labelWords[i][word] += 1
							else: labelWords[i][word]= 1
				else:
					index= ((i-9)*2)+9+label
					#print index
					labelCounts[index] += 1
					numWordsPerLabel[index] += len(tweet)
					for word in newWords:
						if word in labelWords[index]: labelWords[index][word] += 1
						else: labelWords[index][word]= 1


def binarize(labels):
	return binarizeSentiment(labels[0:5])+binarizeWhen(labels[5:9])+binarizeKind(labels[9:])

def binarizeSentiment(sents):
	ind= random.choice([ind for ind,val in enumerate(sents) if val==max(sents)])
	return [int(i==ind) for i in range(len(sents))]

def binarizeWhen(whens):
	return binarizeSentiment(whens)

def binarizeKind(kinds):
	return [int(float(val.replace('\"','')) >= kindThresh) for val in kinds]
	
def classify(tweet, state, time):
	global numExamples
	ret= [0]*24
	probs= [0]*39
	gramSets= {}
	for gram in gramsWeights:
		words= tweet.split(" ")
		if len(words) >= gram:
			gramSets[gram]= []
			string= ""
			for grouping in range(len(words)-gram+1):
				for i,elem in enumerate(range(gram)):
					if i==gram-1: string += words[elem+grouping]
					else:  string += words[elem+grouping]+" "
				gramSets[gram] += [string]
				string= ""
	#print gramSets

	for gram in gramSets: 
		for word in gramSets[gram]:
			for label in range(39):
				if word in labelWords[label]: count= labelWords[label][word]
				else: count= 0
				#print "Count for",word,"is",count,"out of",labelCounts[label]
				#print len(vocabulary), numWordsPerLabel[label]
				prior= 0.001
				if float(labelCounts[label])/float(numExamples) > 0: prior=float(labelCounts[label])/float(numExamples)
				probs[label] += prior
				probs[label] += math.log(float(1+count)/float(len(vocabulary)+numWordsPerLabel[label]))
	#print probs

	sentInd= random.choice([ind for ind,val in enumerate(probs[0:5]) if val==max(probs[0:5])])
	whenInd= 5+random.choice([ind for ind,val in enumerate(probs[5:9]) if val==max(probs[5:9])])
	kindInds= []
	#print sentInd,whenInd,kindInds
	for i in range(9,39,2):
		if probs[i]<probs[i+1]: kindInds += [int(i-((i-9)/2))]
	print probs
	ret= [int(elem==sentInd or elem==whenInd or elem in kindInds) for elem in range(24)]

	#string= id+"," #<- for accuracy.py
	string= state+","+time+","
	for k,num in enumerate(ret):
		if k==len(ret)-1: string += str(num) + '\n'
		else: string += str(num) + ","
	return string


def classifyAll(test,outFile):
  out=open(outFile,'w')
  with open(test) as f: 
    for i,line in enumerate(f):
      if len(line)>1:
    	lst= line.split(',')
    	out.write(classify(lst[2],lst[0],lst[1]))


if __name__ == '__main__':
	parse(sys.argv[1], sys.argv[2]) #arg1 is trainV2, arg2 is file containing grams and weights
	#print labelWords
	#print labelCounts
	start= time.time()
	classify("90 degrees 100 humidity feel crowded bus brooklyn 50 sweaty crewguys", "CA", "2009-06-19 03:49:06")
	#classifyAll("/Users/nikhilnathwani/Desktop/MRF_Train", "nikhilOutput2.txt")
	#classify("love rainy days")
	#print c
	print "Running time:", time.time()-start
	#print unbinarize(c)
	#print len(vocabulary)
