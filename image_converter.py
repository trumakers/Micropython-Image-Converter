
# TruMakers
#
# Bitmap converter: This script converts a standard bitmap file to an array of RGB values that can be directly displayed
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# Important note: This software is distributed WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR 
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# version         : 0.1
# python_version  : 3.7
# Author          : Aaron Brown


from PIL import Image
import numpy as np

#Change the filename to your input filename
FILENAME = 'splash_screen.bmp'
OUTPUT = 'splash_.txt'


def image_to_data(image):
    """Generator function to convert a PIL image to 16-bit 565 RGB bytes."""
    data = np.array(image.convert("RGB")).astype("uint16")
    color = (
        ((data[:, :, 0] & 0xF8) << 8)
        | ((data[:, :, 1] & 0xFC) << 3)
        | (data[:, :, 2] >> 3)
    )
    return bytes(np.dstack(((color >> 8) & 0xFF, color & 0xFF)).flatten().tolist())


#ingest the file and generate the output.
pixels = image_to_data(Image.open(FILENAME))
f = open(OUTPUT, "wb")
f.write(pixels)
f.close()

print("Generated output to file: {}".format(OUTPUT))