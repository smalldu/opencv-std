
import numpy as np
import cv2
from matplotlib import  pyplot as plt

# cv2.IMREAD_COLOR: 读入一副彩色图像，透明度会被忽略 ， 这个是默认参数
# cv2.IMREAD_GRAYSCALE 以灰度模式读入图像
# cv2.IMREAD_UNCHANGED 读入一副图像，并且包括图像的alpha通道
# img = cv2.imread('kt.jpg',cv2.IMREAD_GRAYSCALE)
# 就算路径是错的 只是返回None ,opencv并不会报错

# 保存图片
# cv2.imwrite('kt_copy.jpg',img)
# cv2.imshow('image',img)
#
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 使用 matplotlib 显示图片

img = cv2.imread('kt.jpg',cv2.IMREAD_COLOR)
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.imshow(img2,interpolation='bicubic')
plt.xticks([]) , plt.yticks([])
plt.show()

