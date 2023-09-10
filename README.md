# basic-image-editor
# Python Image Editor

![Python Image Editor](Images/Canvas.png)

This is a Python-based image editor application with a graphical user interface (GUI). It allows you to open, edit, and save images with various features.

## Features

- **Open Images**: You can open image files in formats such as JPEG, PNG, GIF, BMP, and more.

- **Image Editing**: The editor provides various image editing functionalities, including:
  - Flipping (Horizontal)
  - Rotating (Left and Right)
  - Applying Filters (Black and White, Blur, Sharpen, and more)
  - Erasing Lines
  - Cropping(Working on this)
  - Enhancing Images (Adjusting Brightness and Contrast) (still Qorking on this)

- **Drawing**: You can draw lines on the image canvas.

## Usage

1. Open an image using the "Add" button.
2. Use the buttons in the left frame to perform actions like flipping, rotating, saving, and more.
3. Apply filters using the "Select Filter" dropdown.
4. Draw lines on the image by clicking and dragging the mouse.
5. Crop the image by selecting an area on the canvas.
6. Enhance the image using the "Enhance" button.

## Installation

You can install the required libraries using pip:

```bash
pip install ttkbootstrap opencv-python-headless pillow
