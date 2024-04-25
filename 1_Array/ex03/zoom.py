from matplotlib import pyplot as plt
from load_image import ft_load
import numpy as np


def main():
    """Call ft_load to get the image, then slice
    it using numpy slice method.
    We are not allowed to use signal() in this exercice ;
    it is normal to get alot of text when doing SIGINT :)"""
    try:
        image_array = ft_load("animal.jpeg")
        assert image_array is not None, "No image provided"
        image_array = image_array[100:500, 450:850, 0:1]
        print("New shape after slicing:", image_array.shape, "or",
              np.squeeze(image_array).shape)
        print(image_array)
        plt.imshow(image_array, cmap=plt.get_cmap('gray'))
        plt.show()

    except Exception as e:
        print("Error:", str(e))
        return (None)


if __name__ == "__main__":
    main()
