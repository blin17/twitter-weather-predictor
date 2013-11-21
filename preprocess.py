#Problem 2

import string
import numpy as np
import sys
import random
import svmlight
import math

trainName= "trainV2"
trainName= "testV2"

def preprocess(train,test)
  with open(train) as f1: 
    for line in f1:
      if len(line)>1:
        line= line.toLower()
        line= line.split('","')
        for elem in line:
          elem= elem.translate(None, string.punctuation)
        ret= ""
        for i,elem in enumerate(list):

        


        
        label= int(line[:ind])-1
        lst= line[(ind+1):].split(" ")
        lst= [cutColon(elem) for elem in lst]
        if isNormalized:
          lst_sum= sum(zip(*lst)[1])
          lst=[(x,y/float(math.sqrt(lst_sum))) for (x,y) in lst]
        for i in range(4):
          if label==i: labelMats[i].append((1,lst))
          else: labelMats[i].append((-1,lst))
        trueLabels.append(label)
  with open(test) as f2:
    for line in f2:
      if len(line)>1:
        ind= string.find(line, ' ')
        label= int(line[:ind])-1
        lst= line[(ind+1):].split(" ")
        lst= [cutColon(elem) for elem in lst]
        if isNormalized:
          lst_sum=sum(zip(*lst)[1])
          lst=[(x,y/float(math.sqrt(lst_sum))) for (x,y) in lst]
        testData.append((label,lst))

def cutColon(stri):
  ind= string.find(stri, ':')
  return (int(stri[:ind]), bool(stri[(ind+1):]))


def randomKFold(k,numEntries):
  nums= range(numEntries)
  indexSet= [[] for x in xrange(k)]
  foldSize= numEntries/k

  #create list of 5 lists of 400 random numbers partitioning 2000
  for i in range(numEntries):
    n= random.randint(0,len(nums)-1)
    indexSet[(i/foldSize)].append(nums[n])
    nums.remove(nums[n])
  parser.kFoldIndices= indexSet



#fold_num is the number of the fold (0-4) that's used for validation
def getAccuracy(fold_num, C_value):
  kFoldIndices= parser.kFoldIndices
  #one model for each label
  modelSet=  [[] for x in xrange(len(labelMats))]

  #generate model for each label)
  for i in range(len(modelSet)):
    n=(len(kFoldIndices)-1)*len(kFoldIndices[0])
    trains= [[] for x in xrange(n)]
    valids= [[] for x in xrange(len(kFoldIndices[0]))]

    #populate validation set
    for (count,entry) in enumerate(kFoldIndices[fold_num]):
      valids[count]= (entry,labelMats[i][entry])

    #populate trains (used to make model)
    j=0
    for (section,fold) in enumerate(kFoldIndices):
      if section != fold_num:
        for (count,entry) in enumerate(fold):
          trains[(j*len(fold))+count]= (entry,labelMats[i][entry])
        j+=1

    #generate model from training data
    modelSet[i]= svmlight.learn(zip(*trains)[1], C=C_value)

    #endfor
  
  #use svm_classify to predict labels for validation set
  val_predictions= [[] for x in xrange(len(modelSet))]
  for val_ind in range(len(val_predictions)):
    val_predictions[val_ind]= svmlight.classify(modelSet[val_ind],zip(*valids)[1])
  val_labels= [elem.index(max(elem)) for elem in zip(*(val_predictions))]

  #get validation accuracy by comparing actual labels to predicted labels
  valCorrectCount=0
  for (m,index) in enumerate(zip(*valids)[0]):
    if val_labels[m]==trueLabels[index]:
      valCorrectCount += 1
  validation_accuracy= valCorrectCount/float(len(val_labels))

  #use svm_classify to predict labels for training set (4 non-validating folds)
  train_predictions= [[] for x in xrange(len(modelSet))]
  for train_ind in range(len(train_predictions)):
    train_predictions[train_ind]= svmlight.classify(modelSet[train_ind],zip(*trains)[1])
  train_labels= [elem.index(max(elem)) for elem in zip(*(train_predictions))]
  
  #get validation accuracy by comparing actual labels to predicted labels
  trainCorrectCount=0
  for (m,index) in enumerate(zip(*trains)[0]):
    if train_labels[m]==trueLabels[index]:
      trainCorrectCount += 1
  training_accuracy= trainCorrectCount/float(len(train_labels))
  
  return (validation_accuracy, training_accuracy)


def crossValidate(num_folds,C_value):
  val_acc_average=0
  train_acc_average=0
  for i in range(num_folds):
    (val,train)= getAccuracy(i,C_value)
    val_acc_average += val
    train_acc_average += train
  return (val_acc_average/float(num_folds),train_acc_average/float(num_folds))


def getOptimalC(num_folds):
  valid_accs= [0]*len(Cvals)
  train_accs= [0]*len(Cvals)
  for (i,cval) in enumerate(Cvals):
    (v,t)= crossValidate(num_folds,cval)
    valid_accs[i]= v
    train_accs[i]= t
  ind= valid_accs.index(max(valid_accs))
  return (Cvals[ind],valid_accs,train_accs)
    
    
  training_data = __import__('data').train0
  model = svmlight.learn(training_data, C=C_value)
  svmlight.write_model(model, 'my_model.dat')


def trainWithCValue(cval):
  modelSet=  [[] for x in xrange(len(labelMats))]
  for i in range(len(modelSet)):
    modelSet[i]= svmlight.learn(labelMats[i], C=cval)
  
  #use svm_classify to predict labels for validation set
  test_predictions= [[] for x in xrange(len(modelSet))]
  for j in range(len(test_predictions)):
    test_predictions[j]= svmlight.classify(modelSet[j],testData)
  test_labels= [elem.index(max(elem)) for elem in zip(*(test_predictions))]

  #get validation accuracy by comparing actual labels to predicted labels
  testCorrectCount=0
  for m in range(len(testData)):
    if test_labels[m]==testData[m][0]:
      testCorrectCount += 1
  test_accuracy= testCorrectCount/float(len(test_labels))

  #use svm_classify to predict labels for training set (4 non-validating folds)
  train_predictions= [[] for x in xrange(len(modelSet))]
  for p in range(len(train_predictions)):
    train_predictions[p]= svmlight.classify(modelSet[p],labelMats[0])
  train_labels= [elem.index(max(elem)) for elem in zip(*(train_predictions))]
  
  #get validation accuracy by comparing actual labels to predicted labels
  trainCorrectCount=0
  for n in range(len(labelMats[0])):
    if train_labels[n]==trueLabels[n]:
      trainCorrectCount += 1
  training_accuracy= trainCorrectCount/float(len(train_labels))
  
  return (test_accuracy, training_accuracy)

  
if __name__ == '__main__':
  print "Starting preprocess"
  preprocess(sys.argv[1],sys.argv[2])
