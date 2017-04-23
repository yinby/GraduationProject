import cv2  
import numpy as np    
    
def medianBlur(img,n=5,t=5): #中值滤波
    for i in range(t):
        img = cv2.medianBlur(img,n)
    return img

def GaussianBlur(img,x=5,y=5,t=1):#高斯模糊
    for i in range(t):
        img=cv2.GaussianBlur(img,(x,y),0)
    return img

def bilateralFilter(img,d=9,p1=75,p2=75):#双边滤波
    return cv2.bilateralFilter(img,d,p1,p2)

def cut(img,up=165,down=700,left=190,right=850):#裁剪图片
    return img[up:down,left:right]

if __name__ == '__main__':
    img = cv2.imread("pic/72.jpg", 0)
    print (img.shape)
    new = cut(img)
    median=medianBlur(new,15,1)
    cv2.imshow("new", bilateralFilter(new))
    cv2.imshow("Median", median)
    cv2.waitKey(0)
