from matplotlib import image as img
from matplotlib import pyplot as plt
from numpy import array
from load_image import ft_load


def main():
    """Call ft_load to get the image, then slice
    it using numpy slice method."""
    try:
        image_array = ft_load("animal.jpeg")
        image_array = 
        print("New shape after slicing:", image_array.shape())
        plt.imshow(image_array)
        plt.show()

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
