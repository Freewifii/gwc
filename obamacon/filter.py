from PIL import Image

img = Image.open("image5.jpg")
img.show()
print(img.size)
print(img.mode)
print(img.getpixel(xy))
