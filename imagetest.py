from PIL import Image,ImageFilter

image = Image.open('assert/test/image.jpg')
#image = Image.open('/Users/sh-sharemac01/PycharmProjects/LeetCode/assert/test/image.jpg')

print(image.format,image.size,image.mode)
image.show()

# rect = (80, 20, 310, 360)
# image.crop(rect).show()
# size=(128,128)
# test=image.thumbnail(size)
# image.show()
# print(image.size)
# image.filter(ImageFilter.CONTOUR).show()

