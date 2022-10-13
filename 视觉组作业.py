import  cv2
import numpy as np

#识别图中蓝色方块
#导入图片
img = cv2.imdecode(np.fromfile(r"C:\Users\赖文迪\Documents\GitHub\Vision_Group_Guidelines\色块识别\tag.png",dtype = np.uint8),1)

#将原图像进行高斯模糊处理
guassian = cv2.GaussianBlur(img,(3,3),0)

#将BGR彩色转换为HSV彩色图
img_hsv = cv2.cvtColor(guassian,cv2.COLOR_BGR2HSV)

#将HSV彩色图进行腐蚀处理
erosion = cv2.erode(img_hsv,None,iterations=1)

#HSV阈值
hsv_low=np.array([100,43,46])
hsv_high=np.array([124,255,255])

#将图像转化为二值化图像
img_a= cv2.inRange(img_hsv,hsv_low,hsv_high)

#进行平滑处理
img_median = cv2.medianBlur(img_a,7)

#绘制矩形边框
contours,hierarchy = cv2.findContours(img_median,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,255),3)
cv2.imshow("result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#识别图中绿色方块
#导入图片
img = cv2.imdecode(np.fromfile(r"C:\Users\赖文迪\Documents\GitHub\Vision_Group_Guidelines\色块识别\tag.png",dtype = np.uint8),1)

##将原图像进行高斯模糊处理
guassian = cv2.GaussianBlur(img,(3,3),0)

##将BGR彩色转换为HSV彩色图
img_hsv = cv2.cvtColor(guassian,cv2.COLOR_BGR2HSV)

#将HSV彩色图进行腐蚀处理
erosion = cv2.erode(img_hsv,None,iterations=1)

#HSV阈值
hsv_low=np.array([48,43,46])
hsv_high=np.array([77,255,255])

#将图像转化为二值化图像
img_a= cv2.inRange(img_hsv,hsv_low,hsv_high)

#进行平滑处理
img_median = cv2.medianBlur(img_a,7)

#绘制矩形边框
contours,hierarchy = cv2.findContours(img_median,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,255),3)
cv2.imshow("result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
