from matplotlib import image as img
from numpy import array
from numpy import squeeze

# from matplotlib import pyplot as plt
#
# To print image, paste
# plt.imshow(image_array)
# plt.show()
# after its loaded into image_array


def ft_load(path: str) -> array:
    """Loading an image using matplotlib library.
    imread() automatically returns a numpy array"""
    image_array = img.imread(path)
    image_array = image_array[100:500, 450:850, 0:1]
    print('The shape of image is:', image_array.shape, "or",
          squeeze(image_array).shape)
    print(image_array)
    return (image_array)
