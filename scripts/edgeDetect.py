import cv2
import sys
import os
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import shutil

'''
To Do:
Allow for user input for folder date!
Copy Image Folder Directory
Search through all image files
Store in array of images to be processed
	Vary Thresholds
Edge images are then written to each respective folder
Exit!
'''
def initialize():
	plt.switch_backend('agg')


if __name__ == "__main__":
	IMAGE_DIRECTORY = '/home/vagrant/images/'
	IMAGE_SET_DATE = '02.28.15'
	THRESHOLDS = []
	a = 60
	b = 80
	while(a < 100):
		b = 80
		while(b < 120):
			THRESHOLDS.append((a,b))
			b += 10
		a += 10
	#THRESHOLDS = [(50,80),(50,90),(50,100),(50,110),(50,120),(75,80),(100,150),(100,200)]
	initialize()

	src = IMAGE_DIRECTORY + IMAGE_SET_DATE + '/original/'
	dst = IMAGE_DIRECTORY + IMAGE_SET_DATE + '/edges/'
	shutil.copytree(src, dst, symlinks=False, ignore=None)

	for dirName, subdirList, fileList in os.walk(IMAGE_DIRECTORY + IMAGE_SET_DATE):
		print('Found directory: %s' % dirName)
		for fname in fileList:
			print('\t%s' % fname)
			print fname[-3:]
			if fname[-3:] == 'jpg':
				image = cv2.imread((dirName + '/' + fname),0)
				dest = dirName.replace('original', 'edges')
				cv2.imwrite(dest + '/' + fname, image)	
				for parameter in THRESHOLDS:
					edge = cv2.Canny(image, parameter[0], parameter[1])
					cv2.imwrite(dest + '/' + 'edge' + str(parameter[0]) + \
						',' + str(parameter[1]) + fname, edge)
							
	
	print ("Canny Edge Detection completed!")

