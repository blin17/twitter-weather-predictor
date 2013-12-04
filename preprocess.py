import string
import sys
import csv
import random
import math
import re
import sets
import time

trainName= "trainV2"
testName= "testV2"
filenames= {"train": trainName, "test":testName}

trainData= []
testData= []
dataSets= {"train": trainData, "test": testData}

stopWords= []
smileys= []


#Features:
#  -Processed files saved to "trainV2" and "testV2" files
#  -Strings switch to lowercase and punctuation removed
#  -Smileys are preserved (list of smileys read in from file)
#  -Leading and trailing whitespace is removed, internal whitespace compressed into single spaces
#  -Stopwords are filtered out of all strings (list of stopwords read in from file)

#Issues: 
#  -links turn into garbage after removing punctuation, e.g. "http://bit.ly/g6ZQzw"
#  -we're and were will be treated identically when punctuation is removed!!
#  -Deal with RT, @mention, #hashtags

#Potential optimizations:
#  -Don't put label numbers through preprocessing steps when not necessary (e.g. "0" doesn't need to be filtered for stopwords)

#Used to parse smileys.txt and stopwords.txt files into "smileys" and "stopwords" lists
def parseWordList(wordsFile):
    ret= []
    with open(wordsFile) as f: 
      for line in f:
        if len(line)>1:
          ret += [line.strip().lower()]
    return ret


def preprocess(train,test):
  inputFile= {"train": train, "test":test}
  global trainData, testData, dataSets
  for k,data in enumerate(["train","test"]):
    csv_file= csv.writer(open(filenames[data], "wb"))
    with open(inputFile[data]) as f: 
      for j,line in enumerate(f):
        if len(line)>1:
          st= time.time()
          line= line.split('","')
          for i,elem in enumerate(line):
            #Recursively remove punctuation and make things lowercase between smileys
            smileSet= sets.Set()
            for smile in smileys:
              inds= [(m.start(), len(smile), smile) for m in re.finditer(re.compile(re.escape(smile)), elem)]
              smileSet= set(smileSet).union(sets.Set(inds))
            smileSet= sorted(list(smileSet))
            currString= ""
            startInd= 0
            for (index, length, smile) in smileSet:
              currString += removePunctuation(elem[startInd:index],len(line),i) + " " + smile + " "
              startInd= index+length
            currString += removePunctuation(elem[startInd:],len(line),i)
            #Remove stopwords in string
            stillStripping= True
            first= False
            last=False
            while stillStripping:
              firstWord= currString[:currString.find(" ")]
              lastWord= currString[currString.rfind(" ")+1:]
              if firstWord in stopwords: 
                currString= currString[currString.find(" "):]
                first= True
              if lastWord in stopwords: 
                currString= currString[:currString.rfind(" ")]
                last= True
              stillStripping= first or last
              first= False
              last= False
            for stop in stopwords:
              currString= currString.replace(" "+stop+" ", " ")
            line[i]= currString.strip()
          dataSets[data] += [line]  
          csv_file.writerow(line)
          #print "Done with one line", time.time()-st

def removePunctuation(str, lineLen, i):
  if i==0: str= str.replace("\"", "").lower()
  if i==lineLen-1: str= str.translate(None,'\"').lower()
  if i<=3: str= str.translate(None, string.punctuation).lower() 
  return re.sub("\s+"," ",str.lower().strip())


  
if __name__ == '__main__':
  global stopwords, smileys
  startTime= time.time()
  print "Start time:", startTime
  print "Parsing stopwords.txt and smileys.txt..."
  stopwords= parseWordList("stopwords_unigram.txt")
  smileys= parseWordList("smileys.txt")
  print stopwords
  print smileys
  print "Preprocessing..."
  preprocess(sys.argv[1],sys.argv[2])
  stopTime= time.time()
  print "Stop time:", stopTime, "   Duration:", stopTime-startTime
  #print trainData[3]
  #print testData[3]

