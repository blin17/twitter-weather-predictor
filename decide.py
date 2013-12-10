import numpy as np
import sys
import math
import tree
import random
import time

decisionTree= tree.Tree("",0,None,None,"")

def entropy(mat_sizes):
    total= sum(mat_sizes)
    if total==0: return 0
    trick= math.log(total,2)
    val= 0
    for i in range(len(mat_sizes)):
        if mat_sizes[i] != 0: val += mat_sizes[i]*(math.log(mat_sizes[i],2)-trick)
    return (-1*val)/total

def classify(lst, DT):
    if DT.getName() != "": (name, val)= DT.getName()
    if DT.getLabel() != "":
        return DT.getLabel()
    elif lst[name]>val:
        return classify(lst,DT.getBranch(1))
    else:
        return classify(lst,DT.getBranch(0))

def maxGainAttr(S,Attr, vals):
    mat_sizes= [elem.shape[0] for elem in S]
    ent= entropy(mat_sizes)
    max=0
    maxIndex= (0,-1) 
    for i in Attr:
        for val in vals:
            noCounts=[0]*len(S)
            yesCounts=[0]*len(S)
            ind=0
            for elem in S:
                for row in elem:
                    if row[i] <= val:
                        noCounts[ind] += 1
                    else:
                        yesCounts[ind] += 1
                ind+= 1
            e1=entropy(noCounts)
            e2=entropy(yesCounts)
            ret= sum(noCounts)*e1 + sum(yesCounts)*e2
            if ent-(float(ret)/float(sum(mat_sizes))) > max:
                max =ent-(float(ret)/float(sum(mat_sizes)))
                maxIndex= (i,val)
    return maxIndex

def maxDepth(self):
    maxDepth= 0
    nodes=[]
    nodes.append(self)
    while nodes != []:
        for elem in nodes:
            if(elem.getDepth() > maxDepth): maxDepth= elem.getDepth()
            if (elem.getBranch(0) is not None):
                nodes.append(elem.getBranch(0))
            if (elem.getBranch(1) is not None):         
                nodes.append(elem.getBranch(1))
            nodes.remove(elem)
    return maxDepth

def printLevels(self):
    lev0=[]
    lev1=[]
    levk_1=[]
    levk=[]
    depth= maxDepth(self)
    nodes=[]
    nodes.append(self)
    while nodes != []:
        for elem in nodes:
            if(elem.getDepth() == 0): lev0.append(elem.getName()[0])
            if(elem.getDepth() == 1): lev1.append(elem.getName()[0])
            if(elem.getDepth() == depth-1): levk_1.append(elem.getName()[0])
            if(elem.getDepth() == depth): levk.append(elem.getName()[0])
            if (elem.getBranch(0) is not None):
                nodes.append(elem.getBranch(0))
            if (elem.getBranch(1) is not None):         
                nodes.append(elem.getBranch(1))
            nodes.remove(elem)
    return (depth,[lev0,lev1,levk_1,levk])
    
                
#attr is a list of the attributes numbered 1 to n (n= # of attributes)
#threshes is the set of allowable threshold values
def ID3(S, Attr, i, isEarlyStop, earlyStopDepth, threshes):
    labelSetSizes= [elem.shape[0] for elem in S]
    print "IN ID3"
    
    #if no training examples took this branch, turn it into a leaf with randomly-selected label
    if sum(labelSetSizes)==0:
        return tree.Tree("",-1,None,None,math.randInt(0,3))

    #if exactly one type of label took this branch, turn it into a leaf with that label
    elif len([x for x in labelSetSizes if x>0])==1:
        ind= (np.nonzero(labelSetSizes))[0][0]
        return tree.Tree("",-1,None,None,ind)

    elif ((len(Attr)==0) or (isEarlyStop and i>=earlyStopDepth)):
        return tree.Tree("",-1,None,None,labelSetSizes.index(max(labelSetSizes)))

    else:
        name= maxGainAttr(S,Attr,threshes)
        node= tree.Tree(name,i,None,None,"")

        noExamples= [np.array([])]*4
        ind1=0
        for elem in S:
            if len(elem)!=0: noExamples[ind1]= elem[elem[:,name[0]] <= 0]
            ind1+=1
        Attr.remove(name[0])
        node.setBranch(0, ID3(noExamples,Attr,i+1,isEarlyStop, earlyStopDepth, threshes))

        yesExamples= [np.array([])]*4
        ind2=0
        for elem in S:
            if len(elem)!=0: yesExamples[ind2]= elem[elem[:,name[0]] > 0]
            ind2+=1
        node.setBranch(1, ID3(yesExamples,Attr,i+1,isEarlyStop,earlyStopDepth, threshes))
        return node
