#argument forms (python image_processing.py <operation flag> [<argument 1> <argument 2> ...])
from byuimage import Image
import sys


def display(filename):
    return Image(filename)

def darken(filename, percent):
    #Takes as inputs a filename and percent.
    # Returns an image where each pixel’s RGB values is reduced by the given percent
    new_percent = (1 - percent)
    picture = Image(filename)
    for y in range (0,picture.height):
        for x in range (0,picture.width):
            pixel = picture.get_pixel(x,y)
            pixel.red = pixel.red*new_percent
            pixel.green = pixel.green*new_percent
            pixel.blue = pixel.blue*new_percent
            pass
    return picture


def grayscale(filename):
    # Takes as input a filename.
    # Returns an image where each pixel’s RGB values are all averaged
    picture = Image(filename)
    for y in range (0,picture.height):
        for x in range (0,picture.width):
            pixel = picture.get_pixel(x,y)
            average = (pixel.red + pixel.green + pixel.blue) / 3
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    return picture

def sepia(filename):
    # Takes as input a filename.
    # Returns an image where each pixel’s RGB values are computed using the sepia filter
    picture = Image(filename)
    for y in range (0,picture.height):
        for x in range (0,picture.width):
            pixel = picture.get_pixel(x,y)
            true_red = 0.393*pixel.red + 0.769*pixel.green + 0.189*pixel.blue
            true_green = 0.349*pixel.red + 0.686*pixel.green + 0.168*pixel.blue
            true_blue = 0.272*pixel.red + 0.534*pixel.green + 0.131*pixel.blue
            if pixel.red > 255:
                pixel.red = 255
            else:
                pixel.red = true_red
            if pixel.green > 255:
                pixel.green = 255
            else:
                pixel.green = true_green
            if pixel.blue > 255:
                pixel.blue = 255
            else:
                pixel.blue = true_blue
    return picture



def flipped(filename):
    # Takes as inputs a filename.
    # Returns an image where each pixel's position is flipped vertically
    image = Image(filename)
    new_image = Image.blank(image.width, image.height)
    target_y = image.height - 1 
    for y in range(0, image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x,y)
            new_pixel = new_image.get_pixel(x,target_y)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
        target_y -= 1 
    return new_image

def mirrored(filename):
    # Takes as inputs a filename.
    # Returns an image where each pixel's position is flipped vertically
    image = Image(filename)
    new_image = Image.blank(image.width, image.height)
    target_x = image.width - 1 
    for y in range(0, image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x,y)
            new_pixel = new_image.get_pixel(target_x,y)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
            target_x -= 1 
        target_x = image.width - 1
    return new_image


def make_borders(filename, thickness, red, green, blue):
    # Takes as inputs a filename, thickness of the borders, and the RGB values of the borders.
    # Returns the given image surrounded by a border of the thickness and color given.
    image = Image(filename)
    new_image = Image.blank(image.width+(thickness*2),image.height+(thickness*2)) 
    for y in range(image.height):                          
        for x in range(image.width):                       
            pixel = image.get_pixel(x, y)                  
            pixel_new = new_image.get_pixel(x+thickness, y+thickness)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue
    for y in range(0, thickness): 
        for x in range(image.width + (2 * thickness)):                       
            pixel_new = new_image.get_pixel(x, y)          
            pixel_new.red = red
            pixel_new.green = green
            pixel_new.blue = blue
    for y in range(thickness + image.height, image.height + (2*thickness)):          
        for x in range(image.width + (2 * thickness)):                       
            pixel_new = new_image.get_pixel(x, y)          
            pixel_new.red = red
            pixel_new.green = green
            pixel_new.blue = blue
    for x in range(thickness + image.width, image.width + (2*thickness)):          
        for y in range(image.height + (2 * thickness)):                       
            pixel_new = new_image.get_pixel(x, y)          
            pixel_new.red = red
            pixel_new.green = green
            pixel_new.blue = blue
    for x in range(0, thickness):          
        for y in range(image.height + (2 * thickness)):                       
            pixel_new = new_image.get_pixel(x, y)          
            pixel_new.red = red
            pixel_new.green = green
            pixel_new.blue = blue
    return new_image


def collage(image1, image2, image3, image4, thickness):
    # Takes as inputs a filename, thickness of the borders, and the RGB values of the borders.
    # Returns the given image surrounded by a border of the thickness and color given.
    image1 = Image(image1)
    image2 = Image(image2)
    image3 = Image(image3)
    image4 = Image(image4)
    new_image = Image.blank((image1.width * 2) +(thickness*3),(image1.height * 2) +(thickness*3)) 
    for y in range(new_image.height):                          
        for x in range(new_image.width):
            pixel_new = new_image.get_pixel(x, y)          
            pixel_new.red = 0
            pixel_new.green = 0
            pixel_new.blue = 0
    for y in range(image1.height):                          
        for x in range(image1.width):                       
            pixel = image1.get_pixel(x, y)                  
            pixel_new = new_image.get_pixel(x+thickness, y+thickness)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue
    for y in range(image2.height):                          
        for x in range(image2.width):                       
            pixel = image2.get_pixel(x, y)                  
            pixel_new = new_image.get_pixel(x+thickness*2 + image1.width , y+thickness)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue
    for y in range(image3.height):                          
        for x in range(image3.width):                       
            pixel = image3.get_pixel(x, y)                  
            pixel_new = new_image.get_pixel(x+thickness, y+thickness + thickness + image3.height)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue
    for y in range(image4.height):                          
        for x in range(image4.width):                       
            pixel = image4.get_pixel(x, y)                  
            pixel_new = new_image.get_pixel(x+thickness + thickness + image4.width, y+thickness + thickness + image3.height)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue
    return new_image

def detect_green(pixel, threshold_set, factor_set):
    factor = factor_set
    threshold = threshold_set
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green >  threshold:
        return True
    else:
        return False
    

def greenscreen_filter(front_image, back_image, threshold, factor):
    front_image = Image(front_image)
    back_image = Image(back_image)
    new_image = Image.blank(front_image.width, front_image.height)
    for y in range(new_image.height):                          
        for x in range(new_image.width):
            pixel = front_image.get_pixel(x, y) 
            pixel_new = new_image.get_pixel(x, y)
            if detect_green(pixel, threshold, factor):
                pixel = back_image.get_pixel(x, y)
                pixel_new.red = pixel.red
                pixel_new.green = pixel.green
                pixel_new.blue = pixel.blue
            else:
                pixel = front_image.get_pixel(x, y)
                pixel_new.red = pixel.red
                pixel_new.green = pixel.green
                pixel_new.blue = pixel.blue
    return new_image



def validate_commands(commands):
   ### this will validate the things inputted. 
    if commands[0] == "-d" and len(commands) == 2:
        return True
    elif commands[0] == "-k" and len(commands) == 4:
        return True
    elif commands[0] == "-s" and len(commands) == 3:
        return True
    elif commands[0] == "-g" and len(commands) == 3:
        return True
    elif commands[0] == "-f" and len(commands) == 3:
        return True
    elif commands[0] == "-m" and len(commands) == 3:
        return True
    elif commands[0] == "-b" and len(commands) == 7:
        return True
    elif commands[0] == "-c" and len(commands) == 7:
        return True
    elif commands[0] == "-y" and len(commands) == 6:
        return True
    else:
        return False




if __name__ == "__main__":
    commands = sys.argv [1:]
    print(commands)
    if validate_commands(commands):
        if commands[0] == "-d":
            image_to_show = display(commands[1])
            image_to_show.show()
        elif commands[0] == "-k":
            image_to_show = darken(commands[1], float(commands[3]))
            image_to_show.save(commands[2])
            image_to_show.show()
        elif commands[0] == "-s":
            image_to_show = sepia(commands[1])
            image_to_show.save(commands[2])
            image_to_show.show()
        elif commands[0] == "-g":
            image_to_show = grayscale(commands[1])
            image_to_show.save(commands[2])
            image_to_show.show()
        elif commands[0] == "-f":
            image_to_show = flipped(commands[1])
            image_to_show.save(commands[2])
            image_to_show.show()
        elif commands[0] == "-m":
            image_to_show = mirrored(commands[1])
            image_to_show.save(commands[2])
            image_to_show.show()
        elif commands[0] == "-b":
            image_to_show = make_borders(commands[1], int(commands[3]), commands[4], commands[5], commands[6])
            image_to_show.save(commands[2])
            image_to_show.show()
        elif commands[0] == "-c":
            image_to_show = collage(commands[1], commands[2], commands[3], commands[4], int(commands[6]))
            image_to_show.save(commands[5])
            image_to_show.show()
        elif commands[0] == "-y":
            image_to_show = greenscreen_filter(commands[1], commands[2], float(commands[4]), float(commands[5]))
            image_to_show.save(commands[3])
            image_to_show.show()
    else:
        print("that was not a good command")



