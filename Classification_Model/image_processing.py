import numpy as np
from PIL import Image

def rotate_image(image, angle_of_rotation):
	out = image.rotate(angle_of_rotation)
	return np.asarray(out)
