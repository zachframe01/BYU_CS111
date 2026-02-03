from byuimage import Image

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
    # for y in range(0, <image height>):
    #     for x in range(0, <image width>):
      ## code to manipulate the pixel
    # Takes as inputs a filename.
    # Returns an image where each pixel's position is flipped vertically
    return

def make_borders(filename, thickness, red, green, blue):
    # Takes as inputs a filename, thickness of the borders, and the RGB values of the borders.
    # Returns the given image surrounded by a border of the thickness and color given.
    image = Image(filename)
    new_image = Image.blank(image.width+(thickness*2),
                            image.height+(thickness*2)) 
    new_image.color = (red,green,blue)  # Create the larger image.
    for y in range(image.height):                          # Copy the original image
        for x in range(image.width):                       #  into the top of the new
            pixel = image.get_pixel(x, y)                  #  one.
            pixel_new = new_image.get_pixel(x+thickness, y+thickness)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue


    return new_image


if __name__ == "__main__":
    # solution = darken("deer.jpg", 0.9)
    # solution.show()

    # gray = grayscale("deer.jpg")
    # gray.show()

    # sepia = sepia("deer.jpg")
    # sepia.show()
    border = make_borders("deer.jpg", 50, 220, 100, 100)
    border.show()

    pass