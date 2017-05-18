import numpy as np
import math
import sys
import datetime
from sklearn import preprocessing
sys.path.append('..')
from tools import SaveAndLoad as load

POSITION = "D:/Mywork/data/"
INF_DISTANCE = 10000000000

def calculateEuclideanDistanceDouble(instance1,instance2):
	tempSum = 0
	#print (instance1)
	#print (instance2)
	featureNumber = len(instance2)
	for i in range(featureNumber):
		tempSum += (int(instance1[i]) - int(instance2[i])) * (int(instance1[i]) - int(instance2[i]))
	return tempSum

def calculateHausdoffDistance_maxHD(bag1,bag2):
	nowAnswer = 0
	for instance1 in bag1:
		tempDistance = INF_DISTANCE
		for instance2 in bag2:
			tempDistance = min(tempDistance,calculateEuclideanDistanceDouble(instance1,instance2))
		nowAnswer = max(nowAnswer,tempDistance)
	return nowAnswer

def calculateHausdoffDistance_minHD(bag1,bag2):
	nowAnswer = INF_DISTANCE
	for instance1 in bag1:
		tempDistance = INF_DISTANCE
		for instance2 in bag2:
			tempDistance = min(tempDistance,calculateEuclideanDistanceDouble(instance1,instance2))
		nowAnswer = min(nowAnswer,tempDistance)
	return nowAnswer

def kNN(now,trainingSample,r=0,c=2):
	reference = []
	sampleSize = len(trainingSample)
	R = [0] * 2
	C = [0] * 2
	for i in range(sampleSize):
		bag = trainingSample[i]
		bagType = bag["type"]
		bagData = bag["data"]
		if(len(bagData)==0):
			continue
		reference.append((calculateHausdoffDistance_minHD(now["data"],bagData),bagType))
		citer = []
		citer.append((calculateHausdoffDistance_minHD(bagData,now["data"]),0))
		for other in range(sampleSize):
			if(i==other):
				continue
			thisTrainingSample = trainingSample[other]
			citer.append((calculateHausdoffDistance_minHD(bagData,thisTrainingSample["data"]),1))
		citer.sort()
		for j in range(c):
			if(citer[j][1]==1):
				C[int(bagType)]+=1
	for i in range(r):
		R[int(reference[i][1])]+=1
	print (C[0],C[1],R[0],R[1])
	P = C[1]+R[1]
	N = C[0]+R[0]
	return (P,N)

if __name__ == '__main__':
	[allData] = load.load(POSITION+"in.txt",1) 
	Right = 0
	Wrong = 0
	trueNum = 0
	wrongNum = 0
	num=0
	bagSize = len(allData)
	Alldata = []
	for i in range(bagSize):
		bag = allData[i]
		if(len(bag["data"])!=0):
			Alldata.append(bag)
			if(bag["type"]==1):
				trueNum += 1
			else :
				wrongNum += 1
	print (trueNum,wrongNum)
	allData = Alldata
	for i in range(bagSize):
		print (num)
		num += 1
		bag = allData[i]
		bagType = bag["type"]
		bagData = bag["data"]
		if (len(bagData)==0):
			continue
		trainingSample = allData[:i]+allData[i+1:]
		(P,N) = kNN(bag,trainingSample)
		print (P,N)
		if(P>N):
			if(1==int(bagType)):
				Right += 1
			else :
				Wrong += 1
		else :
			if(0==int(bagType)):
				Right += 1
			else :
				Wrong += 1
		print (Right,Wrong)
