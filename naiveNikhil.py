
import sys
import time
import math

labelCounts= [[0]*240, [0]*240]
labelWords= [[{} for i in xrange(240)], [{} for i in xrange(240)]]
numWordsPerLabel= [[0]*240, [0]*240]
vocabulary= set([])

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

def binarize(lst):
	ret= []
	for elem in lst:
		ret += convert_to_binary(float(elem.replace('\"','')))
	return ret

def unbinarize(lst): 
	ret= [0]*24
	for i in range(24):
		binary= lst[i*10:(i+1)*10]
		binary= ''.join(map(str, binary))
		ret[i]= int(binary,2)/float(1000)
	return ret

def convert_to_binary(num):
	num= num*1000
	binary= [int(i) for i in str(bin(int(num)))[2:]]
	binary= [0]*(10-len(binary))+binary
	return binary

def classify(tweet):
	ret= [0]*240
	probs= [0,0]
	for word in tweet: 
		for entry in range(240):
			for label in [0,1]:
				if word in labelWords[label][entry]: count= labelWords[label][entry][word]
				else: count= 0
				print len(vocabulary), numWordsPerLabel[label][entry]
				probs[label] += math.log(float(1+count)/float(len(vocabulary)+numWordsPerLabel[label][entry]))
			print "probs", probs[0],probs[1]
			ret[entry]= probs.index(max(probs))	
			probs= [0,0]
	return ret




if __name__ == '__main__':
	start= time.time()
	parse(sys.argv[1])
	#print labelWords
	#print labelCounts
	print "Running time:", time.time()-start
	c= classify("even if rains and sun wont shine whatever weather youll be mine")
	print unbinarize(c)
	print len(vocabulary)
