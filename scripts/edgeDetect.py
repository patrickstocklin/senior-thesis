import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

print ("compile")

img = cv2.imread('/home/vagrant/images/conc_0.004/T2/13_1.jpg',0)
edges = cv2.Canny(img,50,200)

plt.switch_backend('agg')
plt.subplot(121),
plt.imshow(img,cmap = 'gray')
plt.title('Original Image'),
plt.xticks([]), 
plt.yticks([])
plt.subplot(122),
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'),
plt.xticks([]),
plt.yticks([])
#plt.subplot(111),plt.imshow(img,cmap = 'gray')
#plt.title('Second OG'), plt.xticks([]), plt.yticks([])
#plt.subplot(112),plt.imshow(edges,cmap = 'gray')
#plt.title('Second Edge'), plt.xticks([]), plt.yticks([])
#plt.show()

cv2.imwrite("/home/vagrant/images/output.jpg", edges)
print ("Done Bitch")
