#!/bin/bash
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind0" "svmfiles/model0"
svm_classify -v 3 "svmfiles/trainsvmkind0val" "svmfiles/model0" "svmfiles/out0"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind1" "svmfiles/model1"
svm_classify -v 3 "svmfiles/trainsvmkind1val" "svmfiles/model1" "svmfiles/out1"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind2" "svmfiles/model2"
svm_classify -v 3 "svmfiles/trainsvmkind2val" "svmfiles/model2" "svmfiles/out2"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind3" "svmfiles/model3"
svm_classify -v 3 "svmfiles/trainsvmkind3val" "svmfiles/model3" "svmfiles/out3"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind4" "svmfiles/model4"
svm_classify -v 3 "svmfiles/trainsvmkind4val" "svmfiles/model4" "svmfiles/out4"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind5" "svmfiles/model5"
svm_classify -v 3 "svmfiles/trainsvmkind5val" "svmfiles/model5" "svmfiles/out5"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind6" "svmfiles/model6"
svm_classify -v 3 "svmfiles/trainsvmkind6val" "svmfiles/model6" "svmfiles/out6"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind7" "svmfiles/model7"
svm_classify -v 3 "svmfiles/trainsvmkind7val" "svmfiles/model7" "svmfiles/out7"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind8" "svmfiles/model8"
svm_classify -v 3 "svmfiles/trainsvmkind8val" "svmfiles/model8" "svmfiles/out8"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind9" "svmfiles/model9"
svm_classify -v 3 "svmfiles/trainsvmkind9val" "svmfiles/model9" "svmfiles/out9"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind10" "svmfiles/model10"
svm_classify -v 3 "svmfiles/trainsvmkind10val" "svmfiles/model10" "svmfiles/out10"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind11" "svmfiles/model11"
svm_classify -v 3 "svmfiles/trainsvmkind11val" "svmfiles/model11" "svmfiles/out11"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind12" "svmfiles/model12"
svm_classify -v 3 "svmfiles/trainsvmkind12val" "svmfiles/model12" "svmfiles/out12"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind13" "svmfiles/model13"
svm_classify -v 3 "svmfiles/trainsvmkind13val" "svmfiles/model13" "svmfiles/out13"
svm_learn -v 0 -t 0 "svmfiles/trainsvmkind14" "svmfiles/model14"
svm_classify -v 3 "svmfiles/trainsvmkind14val" "svmfiles/model14" "svmfiles/out14"