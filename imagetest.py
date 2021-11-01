from PIL import Image

image = Image.open('image.jpg')
print(image.format,image.size,image.mode)
image.show()

rect = (80, 20, 310, 360)
image.crop(rect).show()
size=(128,128)
test=image.thumbnail(size)
image.show()
print(image.size)


