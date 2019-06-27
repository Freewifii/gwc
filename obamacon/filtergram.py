import filters
from PIL import Image
img = Image.open("bp.jpg")
img.show()
print(img.size)

 

def load_img(file_name):
    im = Image.open(file_name)
    return im


#Holds the image object

def show_img(img_object):
    img_object.show()
  
            #Object type, string type
def save_img(img_object, save_name):
        img_object.save(save_name)

img = load_img("bp.jpg") 
save_img(img,"jisoos.jpg")
                        #Placeholder
    #Should return a nwe Image object with filter applied

def obamicon(img_object):
    #create new empty list which you will put new pixel values in (HINT: USE APPEND)
    orginal_pixels = img.object.getdata() 
    pixels = im.getdata()
  # Create a list to hold the new image pixel data.
    new_pixels = []
  
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

def avg_pixel(pixel):
  # Use the average of p's RGB values to set a new pixel value.
  avg = (pixel[0] + pixel[1] + pixel[2]) // 3 # Use // for int division.
  return (avg, avg, avg) # R = G = B will be a gray pixel!
  
r = p[0]
g = p[1]
b = p[2]

for p in pixels:
    new_p = avg_pixel(p)
    new_pixels.append(new_p)

    # Pixel intensity = R value + G value + B value
    intensity = p[0] + p[1] + p[2]

    if intensity < 182:
      new_pixels.append(darkBlue)

    elif intensity >= 182 and intensity < 364:
      new_pixels.append(red)

    elif intensity >= 364 and intensity < 546:
      new_pixels.append(lightBlue)

    elif intensity >=546:
      new_pixels.append(yellow)
        #use for loop to iterate through every single pixel
        #use conditionals and boolean cheecks to determine new color to change to

        #image.getdata(band=None)



def main():
    img = load_img("bp.jpg") 
    filters.obamicon(img)
    save_img(img,"jisoos.jpg")
    print(saved_img.title)
import filters

def main():
  # Ask what image the user wants to edit
  filename = input("Enter the name of the image file to edit: ")
  
  # Load the image from the specified file
  img = filters.load_img(filename)

  # Apply filters!
  newimg = filters.bq.jpg(img)
  newimg = filters.grayscale(newimg)

  blue = (30,85,115)
  anotherimg = filters.emphasize(img, blue, 50)

  blueimg = filters.add_color(img, blue)

  lastimg = filters.invert(blueimg)

  # Save the final images
  filters.save_img(newimg, "recolored1.jpg")
  filters.save_img(anotherimg, "recolored2.jpg")
  filters.save_img(blueimg, "recolored3.jpg")
  filters.save_img(lastimg, "recolored4.jpg")

#if __name__ == '__main__':
  #main(filtergram.py)
