from PIL import Image
import math
import colorsys
import random


#This is the first fractal. I zoom in on the Mandelbrot set to see an interesting design. 
#I changed the range to get an interesting view of the set. 
#I also used a random number generator to affect the colors. 

xmin, xmax = -.958, -.907
ymin, ymax = .238, .287

imgx, imgy = 2048, 2048

maxIt = 256

image = Image.new("RGB",(imgx, imgy))

for y in range(imgy):
	cy = y * (ymax-ymin) / (imgy-1) + ymin
	for x in range(imgx):
		cx = x * (xmax-xmin) / (imgx-1) + xmin
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**2 + c

		r = (i*69)%256
		g = random.randint(1,256)
		b = 256 - i

		image.putpixel((x,y),(r,g,b))

image.show()


#For this image, I use the hsv color scheme to create a different color gradient. I also zoomed in to get an
#intersting view of the Mandelbrot set.

xmin, xmax = .32558, .32561
ymin, ymax = -.03429, -.03426

imgx, imgy = 2048, 2048

maxIt = 256

image = Image.new("RGB",(imgx, imgy))

colorsys.rgb_to_hsv(.73, .91, .45)

for y in range(imgy):
	cy = y * (ymax-ymin) / (imgy-1) + ymin
	for x in range(imgx):
		cx = x * (xmax-xmin) / (imgx-1) + xmin
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**2 + c

		r = random.randint(1,256) 
		g = i
		b = random.randint(1,256)

		image.putpixel((x,y),(r,g,b))

image.show()

#I created this fractal on my own by changing the exponents. This created a five-pronged image. 
#I also added a switching exponent that will amke the colors more interesting.
xmin, xmax = -.1, .1
ymin, ymax = -.1, .1

imgx, imgy = 2048, 2048

maxIt = 256

image = Image.new("RGB",(imgx, imgy))

for y in range(imgy):
	cy = y * (ymax-ymin) / (imgy-1) + ymin
	for x in range(imgx):
		cx = x * (xmax-xmin) / (imgx-1) + xmin
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**6 + c*i

		r = (i*42)%256
		g = 256 - i
		b = 256*(-1)**i

		image.putpixel((x,y),(r,g,b))

image.show()







