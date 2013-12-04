import sys
import time
import math
import random
import heapq

labelCounts= [[0]*24, [0]*24]
labelWords= [[{} for i in xrange(24)], [{} for i in xrange(24)]]
numWordsPerLabel= [[0]*24, [0]*24]
vocabulary= set([])
importantWords= set([])
mostImportantBreakdown= [[set([]) for i in xrange(24)],[set([]) for i in xrange(24)]]

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
	if type=="sentiment": indexRange= range(5)
	elif type=="when": indexRange= range(5,9)
	else: indexRange= range(9,24)
	for result in [0,1]:
		for ind in indexRange:
			mapping= labelWords[result][ind]
			inverse = [(value, key) for key, value in mapping.items()]
			print heapq.nlargest(10, inverse)
			importantWords.update([word for (count,word) in heapq.nlargest(200, inverse)])
			mostImportantBreakdown[result][ind].update([word for (count,word) in heapq.nlargest(20, inverse)])


if __name__ == '__main__':
	#start= time.time()
	parse(sys.argv[1])
	#print labelWords[1][2]
	#print labelCounts[1][2]
	print mostImportantWords("sentiment")
	print mostImportantWords("when")
	print mostImportantWords("kind")
	#print "Running time:", time.time()-start
	#c= classify("even if rains and sun wont shine whatever weather youll be mine")
	print len(vocabulary)
	print importantWords
	print "WOOOOOOO\n\n"
	for i in range(24):
		for j in [0,1]:
			print "label:",str(i)+",  yes/no:",str(j)+",  important words:",mostImportantBreakdown[j][i]
