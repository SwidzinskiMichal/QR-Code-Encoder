import PIL
from PIL import Image
from QRgenerator import logo_resize

def test_image_size():
    test_image = logo_resize()
    width, height = test_image.size
    if width != 50 or height != 50:
        raise Exception("Image width and/or height too big!")
