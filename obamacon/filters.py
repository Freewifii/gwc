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

#def obamicon(img_object):
    #create new empty list which you will put new pixel values in (HINT: USE APPEND)
    #orginal_pixels = img.object.getdata()
        #use for loop to iterate through every single pixel
        #use conditionals and boolean cheecks to determine new color to change to

        #image.getdata(band=None)