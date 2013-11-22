import numpy as np
from sklearn.datasets import load_svmlight_file 
import math
import preprocess as parser


def load_probabilities(data):
    sentiment = [0]*5
    time = [0]*4
    weather = [0]*15
    words= {}
    word_count = 0
    
    for datum in data:
        sentence = datum[1].split(" ")
        for word in sentence:
            if word in words:
                for i in range(24):
                    words[word][i] = float(words[word][i])+ float(datum[i+4])
            else:
                words[word] = datum[4:]
            word_count += 1
            for i in range(4,9):
                sentiment[i-4] +=1
            for i in range(9,13):
                time[i-9] += 1
            for i in range(13,28):
                weather[i-13] += 1
    
    return (words, word_count, len(data), sentiment, time, weather)
    

def determine_weather(tweet,data):
    (words, word_count, num_data_points, sentiment, time, weather)= load_probabilities(data)
    submission = [0]*24
    for word in tweet.split(" "):
        if word in words:
            for i in range(0,24):
                if (float(words[word][i])/num_data_points) > 0:
                    if math.log10(float(words[word][i])/num_data_points) == 0:
                        submission[i] -= 1
                    else:
                        submission[i]+= math.log10(float(words[word][i])/num_data_points)
    max_sentiment = 0
    max_time = 0
    max_weather = 0

    for i in range(0,5):
        if submission[i] != 0:
            if max_sentiment == 0:
                max_sentiment = submission[i]
            else:
                if submission[i] > max_sentiment:
                    max_sentiment = submission[i]
    for i in range(5,9):
        if submission[i] != 0:
            if max_time == 0:
                max_time = submission[i]
            else:
                if submission[i] > max_time:
                    max_time = submission[i]
        
    for i in range(9,24):
        if submission[i] != 0:
            if max_weather == 0:
                max_weather = submission[i]
            else:
                if submission[i] > max_time:
                    max_weather = submission[i]
    
    for i in range(0,5):
        if submission[i] == max_sentiment:
            submission[i]= 1
        else:
            submission[i] =0
    for i in range(5,9):
        if submission[i] == max_time:
            submission[i]= 1
        else:
            submission[i]= 0
    
    
    
    for i in range(9,24):
        if submission[i] == max_weather:
            submission[i]= 1
        else:
            submission[i]= 0
        
    return submission
    
parser.preprocess("train.txt", "test.txt")
print determine_weather("Jazz for a Rainy Afternoon:  {link}", parser.trainData)
