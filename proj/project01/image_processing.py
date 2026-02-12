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
            image_to_show = make_borders(commands[1], commands[3], commands[4], commands[5])
            image_to_show.save(commands[2])
            image_to_show.show()
    else:
        print("that was not a good command")

    pass