###################################################
# Aparna Pande (ap539)

lines0 = [line.strip() for line in open('out0')]
results0 = [float(i) for i in lines0]
lines1 = [line.strip() for line in open('out1')]
results1 = [float(i) for i in lines1]
lines2 = [line.strip() for line in open('out2')]
results2 = [float(i) for i in lines2]
lines3 = [line.strip() for line in open('out3')]
results3 = [float(i) for i in lines3]
lines4 = [line.strip() for line in open('out4')]
results4 = [float(i) for i in lines4]
lines5 = [line.strip() for line in open('out5')]
results5 = [float(i) for i in lines5]
lines6 = [line.strip() for line in open('out6')]
results6 = [float(i) for i in lines6]
lines7 = [line.strip() for line in open('out7')]
results7 = [float(i) for i in lines7]
lines8 = [line.strip() for line in open('out8')]
results8 = [float(i) for i in lines8]
lines9 = [line.strip() for line in open('out9')]
results9 = [float(i) for i in lines9]
lines10 = [line.strip() for line in open('out10')]
results10 = [float(i) for i in lines10]
lines11 = [line.strip() for line in open('out11')]
results11 = [float(i) for i in lines11]
lines12 = [line.strip() for line in open('out12')]
results12 = [float(i) for i in lines12]
lines13 = [line.strip() for line in open('out13')]
results13 = [float(i) for i in lines13]
lines14 = [line.strip() for line in open('out14')]
results14 = [float(i) for i in lines14]


final = zip(results0,results1,results2,results3,results4,results5,results6,results7,results8,results9,results10,results11,results12,results13,results14)

lines = [line.strip() for line in open('trainsvmkindval')]
total = 0
totalcorrect = 0

######### MODIFY THIS FILE NOW

for i in range(len(final)):
	templist = list(final[i])
	#index = templist.index(max(templist))
	line = lines[i]
	print line
	if (line.find(" ") == -1):
		actualclass = int(line)
	else:
		stringclass = line[:line.find(" ")]
		actualclass = int(stringclass)
	print index, templist
	if index == actualclass:
		totalcorrect += 1
	total += 1


acc = (float(totalcorrect)/total)*100.0
print "Accuracy of training data on final test file is: ",`acc`
