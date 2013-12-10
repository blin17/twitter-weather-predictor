#This file parses the pictures of in the test/train files into Pic objects
import string
import sys
import tree
import math
import decide
import time
import random
import numpy as np

#label->index: 0->0, 1->1, 2->2, 4->3
typeMats= [[0,0,0,0,0],[0,0,0,0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
labelMats= typeMats[0]
testSet= []
featureHash= {}


def loadWordFeatures(filename):   
  with open(filename) as f: 
    for line in f:
      if len(line)>1:
        lst=[elem.strip().replace('\'','') for elem in line.split(',')]
        count= 0
        for elem in lst:
          featureHash[elem]= count
          count += 1

        print featureHash


def parser(filename, type):
  fv= open("featureVectors.txt", 'a')
  with open(filename) as f: 
    for i,line in enumerate(f):
      if len(line)>1:
        print "Parsing line", i
        lst= line.split(',')
        tweet= lst[0]
        sentiment= [float(elem.replace('\"','')) for elem in lst[4:9]]
        label= random.choice([ind for ind,val in enumerate(sentiment) if val==max(sentiment)])
        vals= [0]*len(featureHash)
        tweet= tweet.split(' ')
        for word in tweet:
          if word in featureHash:
            vals[featureHash[word]] += 1
        string=lst[0]+","
        for j,elem in enumerate(vals):
          if j==len(vals): string+=str(elem)
          else: string+= str(elem)+','
        fv.write(string)
        if isinstance(labelMats[label],int):
          labelMats[label]= np.array(vals)
        else: labelMats[label]= np.vstack((labelMats[label],np.array(vals)))

def partition(filename1, filename2, k):
  partitions=[]
  for ind in range(k):
    partitions.append([])
  i=0
  for file in [filename1, filename2]:
    with open(file) as f: 
      for line in f:
        if len(line)>1:
          ind= string.find(line, ' ')
          label= int(line[:ind])
          if label==4:
            label= 3
          lst= line[(ind+1):].split(" ")
          vals= [0]*2000
          for elem in lst:
            ind= string.find(elem, ':')
            vals[int(elem[:ind])]= int(elem[(ind+1):])
          partitions[i%k].append((label,vals))
          i+=1
  return partitions

def getError(filename, DT):
  num_correct=0
  num_incorrect=0
  correct_vector= [] #1 if correct, 0 otherwise
  
  with open(filename) as f: 
    for line in f:
      if len(line)>1:
        ind= string.find(line, ' ')
        label= int(line[:ind])
        if label==4:
          label= 3
        lst= line[(ind+1):].split(" ")
        vals= [0]*2000
        for elem in lst:
          ind= string.find(elem, ':')
          vals[int(elem[:ind])]= int(elem[(ind+1):])
        DTlabel= decide.classify(vals,DT)
        if DTlabel == label:
          num_correct += 1
          correct_vector.append(1)
        else:
          num_incorrect += 1
          correct_vector.append(0)
  return (float(num_incorrect)/float(num_correct+num_incorrect), correct_vector)

def getErrorOfPartitions(parts, DT):
  partErrors=[0]*5
  num_correct=0
  num_incorrect=0
  i=0
  for part in parts:
    for (lbl,lst) in part:
      DTlabel= decide.classify(lst,DT)
      if DTlabel == lbl:
        num_correct += 1
      else:
        num_incorrect += 1
    partErrors[i]= float(num_incorrect)/float(num_correct+num_incorrect)
    num_correct=0
    num_incorrect=0
    i+=1
  return partErrors

def mcnemar(vec1, vec2):
  pospos=[]
  posneg=[]
  negpos=[]
  negneg=[]
  for i in range(len(vec1)):
    if vec1[i]==1 and vec2[i]==1: pospos.append(0)
    if vec1[i]==1 and vec2[i]==0: posneg.append(0)
    if vec1[i]==0 and vec2[i]==1: negpos.append(0)
    if vec1[i]==0 and vec2[i]==0: negneg.append(0)
  return (len(pospos),len(posneg),len(negpos),len(negneg))

if __name__ == '__main__':
  loadWordFeatures("sentimentWords.txt")
  parser("trainV2", 0)
  start= time.time()
  print "about to go into ID3 method"
  #dt2Level= decide.ID3(labelMats,range(len(featureHash)),0,1,2,[0])
  #print dt2Level
  print time.time()-start