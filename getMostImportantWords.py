import sys
import time
import math
import random
import heapq

labelCounts= [[0]*24, [0]*24]
labelWords= [[{} for i in xrange(24)], [{} for i in xrange(24)]]
numWordsPerLabel= [[0]*24, [0]*24]
vocabulary= set([])
#importantWords= set([])
#mostImportantBreakdown= [[set([]) for i in xrange(24)],[set([]) for i in xrange(24)]]
#sentimentWords= set([])
#whenWords= set([])
#kindWords= set([])
importantWords= []
mostImportantBreakdown= [[[] for i in xrange(24)],[[] for i in xrange(24)]]
sentimentWords= []
whenWords= []
kindWords= []


#Parameters to change:
# -Methods for choosing which labels to increment for each label. 
#  Currently just finds the max confidence score for sentiment and 
#  increments that label's count (if there's a tie it just picks 
#  randomly). May want to increment top 2 or something

def parse(train):
  with open(train) as f: 
    for i,line in enumerate(f):
      if len(line)>1:
      	line= line[:-2]
        lst= line.split(",")
        lst= lst[:4]+binarize(lst[4:])
        updateCounts(lst[1], lst[4:])

def updateCounts(tweet, labels):
	words= tweet.split(" ")
	vocabulary.update(words)
	for i,label in enumerate(labels):
		labelCounts[label][i] += 1
		numWordsPerLabel[label][i] += len(tweet)
	for word in words:
		for index,label in enumerate(labels):
			if word in labelWords[label][index]: labelWords[int(label)][index][word] += 1
			else: labelWords[int(label)][index][word]= 1

def binarize(labels):
	return binarizeSentiment(labels[0:5])+binarizeWhen(labels[5:9])+binarizeKind(labels[9:])

def binarizeSentiment(sents):
	ind= random.choice([ind for ind,val in enumerate(sents) if val==max(sents)])
	return [int(i==ind) for i in range(len(sents))]

def binarizeWhen(whens):
	return binarizeSentiment(whens)

def binarizeKind(kinds):
	return binarizeSentiment(kinds)

def mostImportantWords(type):
	global importantWords
	if type=="sentiment": indexRange= range(5)
	elif type=="when": indexRange= range(5,9)
	else: indexRange= range(9,24)
	for result in [0,1]:
		for ind in indexRange:
			mapping= labelWords[result][ind]
			inverse = [(value, key) for key, value in mapping.items()]
			imp= [word for (count,word) in heapq.nlargest(100, inverse)]
			importantWords += imp
			mostImportantBreakdown[result][ind] += imp

def assignWordsForEachLabel():
	global sentimentWords, whenWords, kindWords
	for i in range(0,5):
		for j in range(2):
			sentimentWords += mostImportantBreakdown[j][i]
	for i in range(5,9):
		for j in range(2):
			whenWords += mostImportantBreakdown[j][i]
	for i in range(9,24):
		for j in range(2):
			kindWords += mostImportantBreakdown[j][i]



if __name__ == '__main__':
	#start= time.time()
	parse(sys.argv[1])
	#print labelWords[1][2]
	#print labelCounts[1][2]
	mostImportantWords("sentiment")
	mostImportantWords("when")
	mostImportantWords("kind")
	#print "Running time:", time.time()-start
	#c= classify("even if rains and sun wont shine whatever weather youll be mine")
	#for i in range(24):
	#	for j in [0,1]:
	#		print "label:",str(i)+",  yes/no:",str(j)+",  important words:",list(mostImportantBreakdown[j][i])
	assignWordsForEachLabel()
	print list(kindWords)

