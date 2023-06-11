"""
File: stanCodoshop.py
Name: chaowei hsieh
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_distance = math.sqrt((red-pixel.red)**2+(green-pixel.green)**2+(blue-pixel.blue)**2)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    return[
        sum(map(lambda pixel: pixel.red, pixels))//len(pixels),
        sum(map(lambda pixel: pixel.green, pixels))//len(pixels),
        sum(map(lambda pixel: pixel.blue, pixels))//len(pixels)
    ]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the
    average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """

    best = min(list((get_pixel_dist(pixel, get_average(pixels[0]), get_average(pixels[1]), get_average(pixels[2])),
                     pixel) for pixel in pixels), key=lambda t: t[0])

    return best[1]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    for i in range(result.height):                      # SimpleImage.height
        for j in range(result.width):                   # SimpleImage.width
            pixel_xy = []
            for k in range(len(images)):                # pixel of (x, y) from list of images; in:list, out:list
                img = images[k].get_pixel(j, i)
                pixel_xy.append(img)

            pixel_xy_best = get_best_pixel(pixel_xy)    # best pixel from list of pixel ; in: list, out:pixel

            new_pixel = result.get_pixel(j, i)          # making result from best pixel ; in: pixel, out:SimpleImage
            new_pixel.red = pixel_xy_best.red
            new_pixel.green = pixel_xy_best.green
            new_pixel.blue = pixel_xy_best.blue

    print("Displaying image!")
    result.show()

    
def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
