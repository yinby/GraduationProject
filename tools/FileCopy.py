#-*- coding: utf-8 -*-

import os
import shutil

src = "D:/Mywork/20170411/lry"
tag = "D:/Mywork/data/bad"
val = []
total = len(os.listdir(tag))

def copyFile(dir):
	global total
	thisDir = os.path.normpath(dir)
	print("Here in: "+thisDir)
	for filename in os.listdir(thisDir):
		nowFile = os.path.join(thisDir,filename)
		print("-- "+nowFile)
		if (os.path.isfile(nowFile)):
			print("FILE!")
			if(dir in val):
				continue
			shutil.copy(nowFile, os.path.join(tag,str(total)+".jpg"))
			total+=1

		elif (os.path.isdir(nowFile)):
			print("DIR!")
			copyFile(nowFile)
		else:
			print("DK!")
if __name__ == '__main__':
	for filename in os.listdir(src):
		nowFile = os.path.join(src,filename)
		if os.path.isdir(nowFile) and (filename[0]!='g'):
			for subFile in os.listdir(nowFile):
				if "癌" in subFile:
					truePath = os.path.join(nowFile,subFile)
					val.append(truePath)
					copyFile(truePath)
	# for x in src:
	# 	copyFile(x)
	# 	print(total)