# -*- coding: utf-8 -*-
import os
import ExtractFeature
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier



dirname = []
testdirname = []
data = []
label = []
testset = []
testlable = []

imgpath = "D:\Study\Hackx\Train"
testpath = "D:\Study\Hackx\Test"
path = "D:\Study\Hackx\\"
def normalize(list):
    for i in range(68):
        list[i] - list[29]
    for i in range(68,len(list)):
        list[i] - list[97]
    return list

def train():
    for file in os.listdir(imgpath):
        file_path = os.path.join(imgpath, file)
        dirname.append(file_path)
    for file in os.listdir(testpath):
        file_path = os.path.join(testpath, file)
        testdirname.append(file_path)
    for i in range(len(dirname)):
        for file in os.listdir(dirname[i]):
            img = os.path.join(dirname[i], file)
            feature = ExtractFeature.geteye_rect(img)
            if feature == False:
                continue
            feature = normalize(feature)
            data.append(feature)
            label.append(int(dirname[i][-1]))


    clf = OneVsRestClassifier(LinearSVC(random_state=0))
    clf.fit(np.array(data),np.array(label))

    for i in range(len(testdirname)):
        testset = []
        for file in os.listdir(testdirname[i]):
            img = os.path.join(testdirname[i], file)
            feature = ExtractFeature.geteye_rect(img)
            if feature == False:
                continue
            testset.append(feature)
        testlable = clf.predict(testset).tolist()
        count = testlable.count(i + 1)
        print "Accuracy of" + str(i + 1) + ":" + str(float(count) / len(testlable))
    return clf
