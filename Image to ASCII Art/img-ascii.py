#Code by Abhinav 

from PIL import Image   #Using Python Imaging Library

def mono(imagename, extension):
	photo = Image.open('courage.jpg')
	photo = photo.convert('1') #Converting full colour image to monochrome
	return photo

def pixels(img, x, y):   #now we read the RGB colours and also read the x-y coordinates of a pixel
	pixel = img.load()  #stores image pixel coordinates
	return pixel[x,y]   #displays RGB values

def ascii_convert(img, imagename):
	width, height = img.size    #returns the size of the image as two values
	#setting these values to zero, so as to start the conversion from the beginning
	x = 0
	y = 0
	
	chars = {0: '$', 255: " "}  #setting reference for our black and white colour
	textfile = open(imagename + '.txt', 'w')
	
	while y<= height - 1:
		rgb = pixels(img, x, y)
		textfile.write(chars[rgb])
		x += 1

		if x == width - 1:
			textfile.write('\n')
			x = 0
			y += 1
	textfile.close()
	
print("Welcome to the ASCII Art Generator!")
print("All files must be located in this folder")
imagename = input("Enter Image Name (without its file extension): ")  # Get User Chosen Image
extension = input("Enter its file extension (EX: .jpg}")

ascii_convert(mono(imagename, extension), imagename)

print("Done!")
