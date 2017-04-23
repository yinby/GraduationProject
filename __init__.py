import cv2 
import matplotlib.pyplot as plt
import numpy as np
import blur 

if __name__ == '__main__':
    img = cv2.imread("pic/6.bmp", 0)
    new = blur.cut(img)
    cv2.imshow("tr",new)
    zz=np.bincount(new.ravel(),minlength=256)
    plt.subplot(221)
    plt.plot(zz)
    #plt.show("ttt")
    new = blur.medianBlur(new,13,1)
    cv2.imshow("old",new)
    # for a in new:
    #     for b in a:
    #         b = min(255,b*2)
    #median=medianBlur(new,15,1)
    print (new.shape)
    # for a in new:
    #     for b in a:
    #         print (b)
    zz=np.bincount(new.ravel(),minlength=256)
    # for a in zz:
    #     print (a)
    plt.subplot(222)
    plt.plot(zz)
    cv2.imshow("new", new)
    plt.show("zzz")
    #print("zzz")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
