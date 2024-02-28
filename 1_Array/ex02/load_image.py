from matplotlib import image as img
from matplotlib import pyplot as plt
from numpy import array

# To print image, paste
# plt.imshow(image_array)
# plt.show()
# after its loaded into image_array


def ft_load(path: str) -> array:
    """Loading an image using matplotlib library.
    imread() automatically returns a numpy array"""
    try:
        image_array = img.imread(path)
        print('The shape of image is:', image_array.shape)
        print(image_array)
        return (image_array)

    except Exception as e:
        print("Error:", str(e))
        return (None)
