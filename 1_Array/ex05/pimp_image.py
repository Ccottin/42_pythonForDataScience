import matplotlib.pyplot as plt
from numpy import array
import numpy as np

# To extract a channel and isolate it ; we can use array[:,:,x] where
# x is the index of the channel, then patch it back 
def ft_invert(array) -> array:
    """Inverts the colors of the image received."""
    try:
        assert array is not None, "No file provided."
        image = 255 - array
        plt.imshow(image)
        plt.show()
    except Exception as e:
        print("Error:", str(e))


def ft_red(array) -> array:
    """Remove all but red from the image received."""
    try:
        assert array is not None, "No file provided."
        image = array * [1, 0, 0]
        plt.imshow(image)
        plt.show()
    except Exception as e:
        print("Error:", str(e))


def ft_green(array) -> array:
    """Remove all but green from the image received."""
    try:
        assert array is not None, "No file provided."
        image = array - [255, 0, 255]
        image = np.clip(image, 0, 255)
        plt.imshow(image)
        plt.show()
    except Exception as e:
        print("Error:", str(e))


def ft_blue(array) -> array:
    """Remove all but blue from the image received."""
    try:
        assert array is not None, "No file provided."
        blue_channel = array[:, :, 2]
        image = np.zeros(shape=array.shape, dtype=int)
        image[:, :, 2] = blue_channel
        plt.imshow(image)
        plt.show()
    except Exception as e:
        print("Error:", str(e))


def ft_grey(array) -> array:
    """Outputs the image received in grey shades. Mean = moyenne"""
    try:
        assert array is not None, "No file provided."
        gray = np.zeros(shape=array.shape, dtype=int)
        gray = np.mean(array, -1, dtype=int)
        gray = np.repeat(gray[:, :, np.newaxis], 3, axis=2)
        plt.imshow(gray,  cmap=plt.get_cmap('gray'))
        plt.show()
    except Exception as e:
        print("Error:", str(e))
