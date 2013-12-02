import string
import sys
import random
import math
import re
import sets
import time


#Decisions to make:
#  -should non-US locations be ignored? Currently lumped into an "other" dictionary
#  -How to determine which kinds of weather to choose? Probably want to determine a 
#   threshold probability which, if exceeded, means that kind of weather is occuring.
#   Currently just gets all indices with the max probability

states= {"alabama":[], "alaska":[], "arizona":[], "arkansas":[], "california":[], "colorado":[], "connecticut":[], "district of columbia":[], "delaware":[], "florida":[], "georgia":[], "hawaii":[], "idaho":[], "illinois":[], "indiana":[], "iowa":[], "kansas":[], "kentucky":[], "louisiana":[], "maine":[], "maryland":[], "massachusetts":[], "michigan":[], "minnesota":[], "mississippi":[], "missouri":[], "montana":[], "nebraska":[], "nevada":[], "new hampshire":[], "new jersey":[], "new mexico":[], "new york":[], "north carolina":[], "north dakota":[], "ohio":[], "oklahoma":[], "oregon":[], "pennsylvania":[], "rhode island":[], "south carolina":[], "south dakota":[], "tennessee":[], "texas":[], "utah":[], "vermont":[], "virginia":[], "washington":[], "west virginia":[], "wisconsin":[], "wyoming":[]}
histos= {"alabama":[], "alaska":[], "arizona":[], "arkansas":[], "california":[], "colorado":[], "connecticut":[], "district of columbia":[], "delaware":[], "florida":[], "georgia":[], "hawaii":[], "idaho":[], "illinois":[], "indiana":[], "iowa":[], "kansas":[], "kentucky":[], "louisiana":[], "maine":[], "maryland":[], "massachusetts":[], "michigan":[], "minnesota":[], "mississippi":[], "missouri":[], "montana":[], "nebraska":[], "nevada":[], "new hampshire":[], "new jersey":[], "new mexico":[], "new york":[], "north carolina":[], "north dakota":[], "ohio":[], "oklahoma":[], "oregon":[], "pennsylvania":[], "rhode island":[], "south carolina":[], "south dakota":[], "tennessee":[], "texas":[], "utah":[], "vermont":[], "virginia":[], "washington":[], "west virginia":[], "wisconsin":[], "wyoming":[]}

def parse(train):
  global states
  with open(train) as f: 
    for i,line in enumerate(f):
      	if len(line)>1:
         	line= line.split('","')
         	sentiment= [float(elem.replace('\"','')) for elem in line[4:9]]
         	when= [float(elem.replace('\"','')) for elem in line[9:13]]
         	kind= [float(elem.replace('\"','')) for elem in line[13:]]
         	updateStates(line[2], sentiment, when, kind)

def updateStates(name, sentiment, when, kind): 
	print name, (name in states)
	maxSentInd= random.choice([ind for ind,val in enumerate(sentiment) if val==max(sentiment)])
	maxWhenInd= random.choice([ind+5 for ind,val in enumerate(when) if val==max(when)])
	maxKindInds= [ind+9 for ind,val in enumerate(kind) if val==max(kind)]
	states[name] += [(maxSentInd,maxWhenInd,maxKindInds)]

def genHistos():
	for state in states:
		if histos[state]==[]: histos[state]= [0]*24
		for (sent,when,kind) in states[state]:
			histos[state][sent] += 1
			histos[state][when] += 1
			for ind in kind:
				histos[state][ind] += 1



if __name__ == '__main__':
  startTime= time.time()
  print "Start time:", startTime
  parse(sys.argv[1])
  stopTime= time.time()
  print "Stop time:", stopTime, "   Duration:", stopTime-startTime
  print "Start time:", startTime
  genHistos()
  stopTime= time.time()
  print "Stop time:", stopTime, "   Duration:", stopTime-startTime
  for state in states:
  	print state, len(states[state]), histos[state]
