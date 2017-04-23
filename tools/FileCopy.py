import os
import shutil

src = "D:/Mywork/20170411/lry/liuruyu20160619/TY-20150609-刘敏--甲状腺乳头状癌经典型"
tag = "D:/Mywork/data/bad"
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
			if(dir==src):
				continue
			shutil.copy(nowFile, os.path.join(tag,str(total)+".jpg"))
			total+=1
		elif (os.path.isdir(nowFile)):
			print("DIR!")
			copyFile(nowFile)
		else:
			print("DK!")

copyFile(src)