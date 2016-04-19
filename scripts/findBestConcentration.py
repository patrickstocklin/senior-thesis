import numpy as np
import math
from PIL import Image
import os
import sys
import shutil
import cv2
import matplotlib

'''
To Do:
Search through directory of original images
Grab the concentration and the similar images (20_1 and such)
Find the agar by taking the mode (or 2nd mode if mode = total black)
For each concentration, take the slices of each image (absolute difference between T1 and T2)
Return the highest ABS Val for Concentration
'''
class concentration(object):
	def __init__(self, cVal, T1, T2, t1fname, t2fname):
		self.concentrationVal = cVal
		if 'T1' in t1fname:
			self.T1image = T1
			self.T1imagefname = t1fname
			self.T2image = T2
			self.T2imagefname = t2fname
		elif 'T2' in t1fname:
			self.T1image = T2
			self.T1imagefname = t2fname
			self.T2image = T1
			self.T2imagefname = t1fname
		self.score = 0.0

	def calculateScore(self):
		SLICE_SIZE = 150

		print ("Calculating Score for Concentration %s" %self.concentrationVal)
		print ("T1")
		print self.T1imagefname	
		pixels = list(self.T1image.getdata())
		width, height = self.T1image.size
		pixels1 = [pixels[i * width:(i+1) * width] for i in xrange(height)]
		print pixels1[height/2]
		print ("T2")
		print self.T2imagefname
		pixels = list(self.T2image.getdata())
		width, height = self.T2image.size
		pixels2 = [pixels[i * width:(i+1) * width] for i in xrange(height)]
		print pixels2[height/2]

		
		midpnt = height/2 - SLICE_SIZE / 2

		slices = []
		res = []
		j = 0
		while j < SLICE_SIZE:
			res = []
			for i in xrange(height):
				res.append(abs(pixels1[midpnt + j][i] - pixels2[midpnt + j][i]))
			j += 1
			slices.append(res)
		print ('results')
		print slices

		finalres = []
		for i in xrange(height):
			total = 0
			for piece in slices:
				total += piece[i]
			total = total / SLICE_SIZE
			finalres.append(total)
		print ('final, averaged')
		print finalres		

def grabImages(image1, image2):
	for dirName, subdirList, fileList in os.walk(IMAGE_DIRECTORY + IMAGE_SET_DATE + '/original'):
		for fname in fileList:
			if image1 in fname:
				T1image = Image.open(dirName + '/' + fname)
			elif image2 in fname:
				T2image = Image.open(dirName + '/' + fname)
	return T1image, T2image

if __name__ == '__main__':
	IMAGE_DIRECTORY = '/home/vagrant/images/'
	IMAGE_SET_DATE = '04.19.16'

	CONCENTRATIONS = set()
	concentrations = []

	for dirName, subdirList, fileList in os.walk(IMAGE_DIRECTORY + IMAGE_SET_DATE + '/original'):
		print '-------------'
		print dirName
		if 'T1' in dirName or 'T2' in dirName:
			fields = dirName.split('/')
			print fields
			print fileList[-1]
			print fileList
			CONCENTRATIONS.add((fields[6], fileList[-1], dirName+'/'+fileList[-1]))
	print ("Finding Best Concentration based on Brightness")
	for conc in CONCENTRATIONS:
		for auxil in CONCENTRATIONS:
			if conc[0] == auxil[0] and (conc[1] != auxil[1]):
				T1, T2 = grabImages(str(conc[1]),str(auxil[1]))
				c = concentration(conc[0], T1, T2, conc[2], auxil[2])	
				concentrations.append(c)
	#concentrations[1].calculateScore()
	for conc in concentrations:
		conc.calculateScore()
