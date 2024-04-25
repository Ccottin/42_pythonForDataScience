from matplotlib import image as img
from numpy import array

# To print image, paste
# plt.imshow(image_array)
# plt.show()
# after its loaded into image_array
# also import this library
# import matplotlib.pyplot as plt


def ft_load(path: str) -> array:
    """Loading an image using matplotlib library.
    imread() automatically returns a numpy array"""
    try:
        image_array = img.imread(path)
        print(image_array)
        return (image_array)

    except Exception as e:
        print("Error:", str(e))
        return (None)
