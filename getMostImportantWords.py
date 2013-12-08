import sys
import time
import math
import random
import heapq

labelCounts= [0]*24
labelWords= [{} for i in xrange(24)]
numWordsPerLabel= [0]*24
vocabulary= set([])
#importantWords= set([])
#mostImportantBreakdown= [[set([]) for i in xrange(24)],[set([]) for i in xrange(24)]]
#sentimentWords= set([])
#whenWords= set([])
#kindWords= set([])
importantWords= []
mostImportantBreakdown= [[] for i in xrange(24)]
sentimentWords= set([])
whenWords= set([])
kindWords= [set([]) for i in xrange(15)]
kindThreshold= 0.7


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
	for index,label in enumerate(labels):
		if label and index not in [0,4,7,15]: 
			labelCounts[index] += 1
			numWordsPerLabel[index] += len(tweet)
			wordsSeen=[]
			for word in words:
				if words not in wordsSeen and word!="":
					wordsSeen += [word]
					if word in labelWords[index]: 
						labelWords[index][word] += 1
					else: 
						labelWords[index][word]= 1
	#if "humidity" in words: print tweet

def binarize(labels):
	return binarizeSentiment(labels[0:5])+binarizeWhen(labels[5:9])+binarizeKind(labels[9:])

def binarizeSentiment(sents):
	newSents= [val for ind,val in enumerate(sents) if ind not in [0,4]] 
	maxes= [ind for ind,val in enumerate(sents) if (val==max(newSents)) and ind not in [0,4]]
	ind= random.choice(maxes)
	return [int(i==ind and ind not in [0,4]) for i in range(len(sents))]

def binarizeWhen(whens):
	newWhens= [val for ind,val in enumerate(whens) if ind!=2] 
	maxes= [ind for ind,val in enumerate(whens) if (val==max(newWhens)) and ind!=2]
	ind= random.choice(maxes)
	return [int(i==ind and ind!=2) for i in range(len(whens))]

def binarizeKind(kinds):
	return [int(float(elem) >= kindThreshold and ind!=6) for ind,elem in enumerate(kinds)]

def mostImportantWords():
	files= [[] for i in xrange(17)]
	global importantWords
	files[0]= open('Important_Word_Output/sentimentWords', 'w+')
	files[1]= open('Important_Word_Output/whenWords', 'w+')
	for i in range(15):
		if i != 6:
			string= 'Important_Word_Output/kindWords'+str(i+1)
			files[i+2]= open(string, 'w+')
	a= labelWords[1]
	b= labelWords[2]
	c= labelWords[3]
	numTweetsWithEachWord= dict((n, a.get(n, 0)+b.get(n, 0)+c.get(n,0)) for n in set(a)|set(b)|set(c))
	#print numTweetsWithEachWord
	indexRanges= [[1,2,3], [5,6,8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23]]
	for j,indRange in enumerate(indexRanges):
		for ind in indRange:
			if ind!=15:
				mapping= labelWords[ind]
				inverse = [(float(value)/float(numTweetsWithEachWord[key]), key) for key, value in mapping.items() if numTweetsWithEachWord[key]>15]
				imp= [word for (count,word) in heapq.nlargest(500, inverse)]
				importantWords += imp
				if j==0: sentimentWords.update(imp)
				elif j==1: whenWords.update(imp)
				else: kindWords[j-2].update(imp)
	
	files[0].write(str(sentimentWords)[5:-2].replace("\'",""))
	files[1].write(str(whenWords)[5:-2].replace("\'",""))
	for i in range(15):
		if i != 6: 
			#print "here", i, str(kindWords[i]), str(kindWords[i])[5:-2].replace("\'","")
			#print files[16]
			files[i+2].write("here")
			files[i+2].write(str(kindWords[i])[5:-2].replace("\'",""))
	for i,file in enumerate(files):
		if i!=8: file.close()

"""			
def mostImportantWordsPerLabel(type):
	global importantWords
	if type=="sentiment": indexRange= range(5)
	elif type=="when": indexRange= range(5,9)
	else: indexRange= range(9,24)
	for result in [0,1]:
		for ind in indexRange:
			mapping= labelWords[result][ind]
			inverse = [(value, key) for key, value in mapping.items()]
			imp= [word for (count,word) in heapq.nlargest(500, inverse)]
			importantWords += imp
			mostImportantBreakdown[result][ind] += imp
"""

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
	mostImportantWords()
	#print "Running time:", time.time()-start
	#c= classify("even if rains and sun wont shine whatever weather youll be mine")
	#for i in range(24):
	#	for j in [0,1]:
	#		print "label:",str(i)+",  yes/no:",str(j)+",  important words:",list(mostImportantBreakdown[j][i])
	#assignWordsForEachLabel()
	#print list(kindWords)

