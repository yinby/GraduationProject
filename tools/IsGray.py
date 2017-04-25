import cv2 
import os
import shutil
src = "D:/Mywork/data/bad"
tag = "D:/Mywork/data/bad_gray"
total = 0

def IsGray(path):
	img = cv2.imread(path)
	for row in img:
		for col in row:
			if col[0]==col[1] and col[1]==col[2]:
				pass
			else :
				return False
	return True

def Tran(path):
	global total
	path = os.path.normpath(path)
	for file in os.listdir(path):
		nowFile = os.path.join(path,file)
		if IsGray(nowFile):
			shutil.copy(nowFile,os.path.join(tag,str(total)+".jpg"))
			total += 1

if __name__ == '__main__':
	Tran(src)