from matplotlib import pyplot as plt
from load_image import ft_load
import numpy as np
from numpy import array


def ft_rotate(image: array) -> array:
    """Performs a rotation of the picture the way numpy.transpose
    will do."""
    new_image = np.zeros(shape=image.shape)
    size = len(image)
    print(size)
    i = 0
    while i < size:
        x = 0
        while x < size:
            new_image[x][i] = image[i][x]
            x = x + 1
        i = i + 1
    return (new_image)


def main():
    """Call ft_load to get the image, then rotate it by
    reversing axis.
    We are not allowed to use signal() in this exercice ;
    it is normal to get alot of text when doing SIGINT :)"""

    try:
        image_array = ft_load("animal.jpeg")
        image_array = image_array[100:500, 450:850, 0:1]
        print('The shape of image is:', image_array.shape, "or",
              np.squeeze(image_array).shape)
        print(image_array)
        image_array = np.squeeze(image_array)
        image_array = ft_rotate(image_array)
        print("new shape after transpose:", image_array.shape)
        print(image_array)
        plt.imshow(image_array, cmap=plt.get_cmap('gray'))
        plt.show()

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
