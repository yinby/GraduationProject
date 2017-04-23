import cv2
import blur
import Image
    
def Sharp(image,flag1=0,flag2=0):
    shape = image.shape
    w = shape[1]
    h = shape[0]
    #print (w,h)
    iSharp = image.copy()
    for i in range(h-1):
        for j in range(w-1):
            if flag2 == 0:
                x = abs(int(image[i,j+1])-int(image[i,j]))
                y = abs(int(image[i+1,j])-int(image[i,j]))
            else:
                x = abs(int(image[i+1,j+1])-int(image[i,j]))
                y = abs(int(image[i+1,j])-int(image[i,j+1]))
            if flag1 == 0:
                iSharp[i,j] = max(x,y)
            else:
                iSharp[i,j] = x+y
    return iSharp 

if __name__ == '__main__':
    img = cv2.imread("pic/6.bmp", 0)
    new = blur.cut(img)
    #image = blur.medianBlur(new,5,3)
    image = new
    #cv2.imshow('image',image)
    cv2.imshow("tr",image)
    iMaxSharp = Sharp(image)
    iAddSharp = Sharp(image,1)
    iRMaxSharp = Sharp(image,0,1)
    iRAddSharp = Sharp(image,1,1)
    cv2.imshow('iMaxSharp',iMaxSharp)
    cv2.imshow('iAddSharp',iAddSharp)
    cv2.imshow('iRAddSharp',iRAddSharp)
    cv2.imshow('iRMaxSharp',iRMaxSharp)
    cv2.waitKey(0)