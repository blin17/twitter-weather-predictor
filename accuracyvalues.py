###################################################
# File accuracyvalues.py
###################################################

infile1 = open('train_submission.txt', 'r')
submissionline1 = infile1.readline().strip()
allsubdata = [line.strip() for line in infile1]

infile2 = open('trainV2')
alltraindata = [line.strip() for line in infile2]
when_dict = {}
sent_dict = {}
kind_dict = {}
total_when_correct = 0
total_sent_correct = 0
total_kind_correct = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
total_kind_tp = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
total_kind_fp = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
total_kind_tn = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
total_kind_fn = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

total = 0


def compareLists(trainlst, sublst):
	maxindex = sublst.index(max(sublst))
	topvalue = max(trainlst)
	bestindex = trainlst.index(topvalue)
	if (maxindex == bestindex):
		return 1.0
	else: return 0.0

def compareKinds(trainlst, sublst):
	for i in range(len(trainlst)):
		if (sublst[i] == 1.0) and (trainlst[i] > 0.7):
			total_kind_correct[i] += 1
			#print `total_kind_correct`
		elif (sublst[i] == 0.0) and (trainlst[i] <= 0.2):
			total_kind_correct[i] += 1


for k in range(len(alltraindata)):
    trainvaluelist = [i for i in alltraindata[k].split(",")]
    sent_dict[str(trainvaluelist[0])] = [float(i) for i in trainvaluelist[4:9]]
    when_dict[str(trainvaluelist[0])] = [float(i) for i in trainvaluelist[9:13]]
    kind_dict[str(trainvaluelist[0])] = [float(i) for i in trainvaluelist[13:28]]


for k in range(len(allsubdata)):
	subvaluelist = [float(i) for i in allsubdata[k].split(",")]
	key = str(int(subvaluelist[0]))
	sent = subvaluelist[1:6]
	when = subvaluelist[6:10]
	kind = subvaluelist[10:]
	if (key in when_dict):
		total_when_correct += compareLists(when_dict[key], when)
		total_sent_correct += compareLists(sent_dict[key], sent)
		compareKinds(kind_dict[key], kind)
		#print kind_dict[key], kind
	else: 
		print "key not in training dictionaries"
	total += 1


when_acc = (float(total_when_correct)/total)*100.0
print "Total when correct is ",`total_when_correct`, "Accuracy of \"when\" label is: ",`when_acc`

sent_acc = (float(total_sent_correct)/total)*100.0
print "Total sentiment correct is ",`total_sent_correct`, "Accuracy of \"sentiment\" label is: ",`sent_acc`

kind_acc = [(x*100.0)/total for x in total_kind_correct]
print "Kind accuracies", `kind_acc`

total_kind_acc = sum(kind_acc)/len(kind_acc)
print "Average kind accuracy is ", `total_kind_acc`

print kind_dict['11']



