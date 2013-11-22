import string
import sys
import csv
import random
import math
import re
import sets

trainName= "trainV2"
testName= "testV2"
filenames= {"train": trainName, "test":testName}

trainData= []
testData= []
dataSets= {"train": trainData, "test": testData}

smileys= [":)",":(",":-)",":-(", ":D",":P",":-D","=)"]

#Remove trailing leading whitespace and turn excessive whitespace to one whitespace
#Keep smileys in the tweets! (eliminating punctuation gets rid of them!)

def preprocess(train,test):
  inputFile= {"train": train, "test":test}
  global trainData, testData, dataSets
  for k,data in enumerate(["train","test"]):
    csv_file= csv.writer(open(filenames[data], "wb"))
    with open(inputFile[data]) as f1: 
      for j,line in enumerate(f1):
        if len(line)>1 and j<=15:
          line= line.split('","')
          for i,elem in enumerate(line):
            smileSet= sets.Set()
            for smile in smileys:
              inds= [(m.start(), len(smile), smile) for m in re.finditer(re.compile(re.escape(smile)), elem)]
              smileSet= set(smileSet).union(sets.Set(inds))
            smileSet= sorted(list(smileSet))
            currString= ""
            startInd= 0
            for (index, length, smile) in smileSet:
              currString += removePunctuation(elem[startInd:index],len(line),i) + smile
              startInd= index+length
            currString += removePunctuation(elem[startInd:],len(line),i)
            line[i]= currString
          dataSets[data] += [line]  
          csv_file.writerow(line)

def removePunctuation(str, lineLen, i):
  if i==0: str= str.replace("\"", "")
  if i==lineLen-1: str= str.replace("\n", "").translate(None,'\"')
  if i<=4: return str.translate(None, string.punctuation).lower()
  else: return str


## def preprocess2(train, test):
##   global trainData, testData, dataSets
##   inputFile= {"train": train, "test":test}
##   for k,data in enumerate(["train","test"]):
##     with open(inputFile[data]) as f1: 
##       for line in f1:
##           line= line.lower()
##           for elem 
##           line= line.split('","')
##           dataSets[data] += [line]
##   print dataSets
      


## def preprocess2(train, test):
##   inputFile= {"train": train, "test":test}
##   global trainData, testData, dataSets
##   for k,data in enumerate(["train","test"]):
##     csv_file= csv.writer(open(filenames[data], "wb"))
##     with open(inputFile[data]) as f1: 
##       for j,line in enumerate(f1):
##         if len(line)>1:
##           line= line.lower()
##           line= line.split('","')
##           for i,elem in enumerate(line):
##             if i==0: elem= elem.replace("\"", "")
##             if i==len(line)-1: elem= elem.replace("\n", "")
##             line[i]= elem.translate(None, string.punctuation)
##           dataSets[data] += [line]
##   print dataSets
  
if __name__ == '__main__':
  print "Starting preprocess"
  preprocess(sys.argv[1],sys.argv[2])

