from byuimage import Image
image = Image("pebbles.jpg")
# image.show()

# for pixel in image:
#     pixel.green = 0
#     pixel.blue = 0
# image.show()

# how would we darken all the colors in an image?
# def darken(image):
#     for pixel in image:
#         pixel.red = pixel.red/2
#         pixel.green = pixel.green/2
#         pixel.blue = pixel.blue/2
        

# image = Image("pebbles.jpg")
# darken(image)
# image.show()

# # how would we darken only half of an image using .height, .width, and .get_pixel()?
# def darken_half(image):

#     for y in range (0,image.height//2):
#         for x in range (0,image.width):
#             pixel = image.get_pixel(x,y)
#             pixel.red = pixel.red/2
#             pixel.green = pixel.green/2
#             pixel.blue = pixel.blue/2
#             pass
        
# image = Image("pebbles.jpg")
# darken_half(image)
# image.show()

# how would we create an image that was a copy of an image? 
# use Image.blank(x,y) to create a new blank image with x width and y height
# def copy(image):
#     new_image = Image.blank(image.width, image.height)
#     for y in new_image.height:
#         for x in new_image.width:
#             pixel = 
#             pixel_new = 
#             pixel_new.red = 
#             pixel_new.green = 
#             pixel_new.blue = 
#     return new_image
#     pass
# 
# image = Image("pebbles.jpg")
# copy(image).show()

 # create a copy of an Image with the top half of the pixels muted
def mute_top(image):
    new_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            pixel_new = new_image.get_pixel(x, y)
            factor = 1.0
            if (pixel.red + pixel.blue + pixel.green)/3 > 120 and y < image.height//2:
                factor = 0.5
            pixel_new.red = pixel.red * factor
            pixel_new.green = pixel.green * factor
            pixel_new.blue = pixel.blue * factor
    return new_image

image = Image("pebbles.jpg")
mute_top(image).show()

# create a copy of an Image that is 50 pixels larger with a black boarder at the bottom 
def bottom_black_border(image):
    new_image = Image.blank(image.width,image.height+50)   # Create the larger image.
    for y in range(image.height):                          # Copy the original image
        for x in range(image.width):                       #  into the top of the new
            pixel = image.get_pixel(x, y)                  #  one.
            pixel_new = new_image.get_pixel(x, y)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue
    for y in range(image.height,image.height+50):          # Make the pixels in the
        for x in range(image.width):                       #  bottom black. RGB for
            pixel_new = new_image.get_pixel(x, y)          #  black is (0,0,0).
            pixel_new.red = 255
            pixel_new.green = 0
            pixel_new.blue = 0

    return new_image

image = Image("pebbles.jpg")
bottom_black_border(image).show()