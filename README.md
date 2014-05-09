Twitter_Weather_Predictor
=========================

Using over 100,000 weather related tweets as learning data, we created a classifier to generate the sentiment, time frame, and weather for tweets. To build this classifier, we tested Naive Bayes, Support Vector Machine, and Decision Tree algorithms to discover which one most accurately predicts labels for tweets.


Related Information:
Partly Sunny with a Chance of Hashtags
http://www.kaggle.com/c/crowdflower-weather-twitter

id, tweet, state, location, s1, s2, ...., k15

Sample data: "1","Jazz for a Rainy Afternoon:  {link}","oklahoma","Oklahoma","0","0","1","0","0","0.8","0","0.2","0","0","0","0","0","0","0","0","0","0","1","0","0","0","0","0"

s1,"I can't tell"
s2,"Negative"
s3,"Neutral / author is just sharing information"
s4,"Positive"
s5,"Tweet not related to weather condition"

w1,"current (same day) weather"
w2,"future (forecast)"
w3,"I can't tell"
w4,"past weather"

k1,"clouds"
k2,"cold"
k3,"dry"
k4,"hot"
k5,"humid"
k6,"hurricane"
k7,"I can't tell"
k8,"ice"
k9,"other"
k10,"rain"
k11,"snow"
k12,"storms"
k13,"sun"
k14,"tornado"
k15,"wind"