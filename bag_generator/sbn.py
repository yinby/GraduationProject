import cv2
import os
import shutil

SRC="D:/Mywork/data/bad_nosymbol"
TAG="D:/Mywork/data/bad_new"
INSTANCE_UPPER_BOUND = 200
ROW_LIMIT = 20
COL_LIMIT = 20
DIRECTION = ((0,0),(-2,0),(2,0),(0,2),(0,-2))
FOUR = ((0,0),(0,1),(1,1),(1,0))

def averengeOfFour(img,x,y):
	return int((img[x][y] + img[x+1][y] + img[x][y+1] + img[x+1][y+1])/4)

#Maybe resize many times
# def resize(img):
# 	row = len(img)
# 	col = len(img[0])
# 	size = row * col
# 	while(size>INSTANCE_UPPER_BOUND):
# 		print (size)
# 		img = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
# 		row = len(img)
# 		col = len(img[0])
# 		size = row *col
# 	return img

def resize(img):
	row = len(img)
	col = len(img[0])
	size = min(ROW_LIMIT/row,COL_LIMIT/col)
	img = cv2.resize(img,None,fx=size,fy=size,interpolation=cv2.INTER_AREA)
	return img

def SBN(img):
	row = len(img)
	col = len(img[0])
	realRowNumber = int(row/2)
	realColNumber = int(col/2)
	result = []
	for x in range(2,(realRowNumber-1)*2,2):
		for y in range(2,(realColNumber-1)*2,2):
			result.append([])
			for z in DIRECTION:
				nowx = x + z[0]
				nowy = y + z[1]
				nowValue = 0;
				for i in FOUR:
					newx = nowx + i[0]
					newy = nowy + i[1]
					nowValue += img[newx][newy][0]
				nowValue /= 4
				result[len(result)-1].append(nowValue)
	return result

if __name__ == '__main__':
	for filename in os.listdir(SRC):
		img = cv2.imread(os.path.join(SRC,filename))
		cv2.imshow("0",img)
		img = resize(img)
		result = SBN(img)
		print(result)
		cv2.imshow("1",img)
		cv2.waitKey(0)
		break