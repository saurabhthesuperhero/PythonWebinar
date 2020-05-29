from PIL import Image,ImageEnhance
import os
#make grayscale/-b/w for all files at one click

# print(os.listdir()) 
for i in os.listdir('.'):# print(i)
	try:
		im2=Image.open(i).convert('RGB')
		im3=im2.convert('L')
		im3.save('gray/'+i)
		print(i)
	except:
		pass