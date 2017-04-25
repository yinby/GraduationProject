import cv2 
import os
import shutil
src = "D:/Mywork/data/good_gray"
tag = "D:/Mywork/data/good_nosymbol"
total = 0

# def IsSymboled(path):
# 	img = cv2.imread(path)
# 	for row in img:
# 		rowlen = len(row)
# 		for x in range(rowlen-10):
# 			ok = True
# 			for y in range(5):
# 				if row[x+y][0]<240:
# 					ok = False
# 			if ok:
# 				return True
# 	return False

def IsSymboled(path):
	img = cv2.imread(path)
	for row in img:
		for col in row:
			if col[0]>252:
				return True
	return False

def Tran(path):
	global total
	path = os.path.normpath(path)
	for file in os.listdir(path):
		nowFile = os.path.join(path,file)
		if not IsSymboled(nowFile):
			shutil.copy(nowFile,os.path.join(tag,str(total)+".jpg"))
			total += 1

if __name__ == '__main__':
	Tran(src)