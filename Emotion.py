# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageFont, ImageDraw
import tkFileDialog
import ExtractFeature
import Train
import FaceDetect
import random

f = open("Text.txt", "r")
path = "D:\Study\Hackx\\"
default_dir = r"C:\Users\Junxue\Desktop"  # 设置默认打开目录
text = f.readlines()
f.close()

for i in range(len(text)):
	text[i] = text[i].decode('utf-8')
	text[i] = text[i].split('.')

def is_img(ext):
	ext = ext.lower()
	if ext in ['jpg', 'png', 'jpeg', 'bmp']:
		return True
	else:
		return False

def main():
	clf = Train.train()
	while(True):
		testset = []
		fname = tkFileDialog.askopenfilename(title = u"选择文件", initialdir = (os.path.expanduser(default_dir)))
		if fname != "":
			if is_img(fname.split('.')[1]):
				width, top, left, height = FaceDetect.cutimg(fname)
				feature = ExtractFeature.geteye_rect(path + fname.split('/')[-1])
				if feature != False:
					testset.append(feature)
				result = clf.predict(testset).tolist()
				if result[0] == 1:
					print "Angry"
				elif result[0] == 2:
					print "Disgust"
				elif result[0] == 3:
					print "Fear"
				elif result[0] == 4:
					print "Delight"
				elif result[0] == 5:
					print "Sadness"
				elif result[0] == 6:
					print "Surprised"
			else:
				print "not image"
				break
			im = Image.open(fname)
			draw = ImageDraw.Draw(im)
			newfont = ImageFont.truetype('simhei.ttf', 30)
			draw.text((left - 50, top + height + 60), text[result[0] - 1][random.randint(0,len(text[result[0] - 1])) - 1], (0, 0, 0), font = newfont)
			im.show()
			im.save(path + "target.jpg")
		else:
			break

main()
