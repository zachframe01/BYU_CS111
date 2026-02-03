from byuimage import Image
image = Image("man.png")
image.show()

#identify green pixels if G exceeds a threshold
def detect_green(pixel):
    threshold = 100
    if pixel.green > threshold:
        return True
    else:
        return False

 # change green pixels to red
def change_to_red(image):
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            if detect_green(pixel):
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0

change_to_red(image) 
image.show() 

# now identify green pixels if G exceeds the average color value by a factor 
def detect_green(pixel):
    factor = 1.3
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average:
        return True
    else:
        return False

image = Image("man.png")
change_to_red(image) 
image.show() 

# now identify green pixels if G exceeds the average color value by a factor 
# and exceeds a threshold
def detect_green(pixel):
    factor = 1.3
    threshold = 90
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green > threshold:
        return True
    else:
        return False

image = Image("man.png")
change_to_red(image) 
image.show() 

# now let's use detect_green to copy only the man onto the background 
def green_screen(foreground,background):
    final = Image.blank(background.width,background.height)
    for y in range(background.height):
        for x in range(background.width):
            fp = final.get_pixel(x,y)
            bp = background.get_pixel(x,y)
            fp.red = bp.red
            fp.green = bp.green
            fp.blue = bp.blue

    for y in range(foreground.height):
        for x in range(foreground.width):
            fp = foreground.get_pixel(x, y)
            if not detect_green(fp):
                np = final.get_pixel(x,y)
                np.red = fp.red
                np.green = fp.green
                np.blue =fp.blue
    return final

background_image = Image("explosion.png")
background_image.show()

image = Image("man.png")
final_image = green_screen(image,background_image)
final_image.show()
