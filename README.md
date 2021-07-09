# Image Converter #

This script is designed to convert a standard bitmap image to binary format for use in our
innovate development board running Micropython. This saves CPU cycles as it unloads the processing overhead from the ESP32 core.

### Requirements ###

* Resolution of the image must match the screen, for our example we used a 160x128 RGB screen.
* Only tested with bitmap format

### Usage ###

* Create a VENV and install Requirements.txt
* Change FILENAME to match the file you are converting, default: 'splash_screen.bmp'
* Run python image_converter.py
* Output generated as 'splash_.txt'

### Who do I talk to? ###

* Support@trumakers.com