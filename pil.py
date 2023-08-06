import PIL.Image

def resize_image(image_path, output_path, width, height):
    """
    Resizes an image to the specified width and height.

    Args:
        image_path (str): The path to the input image.
        output_path (str): The path to the output image.
        width (int): The desired width of the output image.
        height (int): The desired height of the output image.
    """

    image = PIL.Image.open(image_path)
    image = image.resize((width, height))
    image.save(output_path)

if __name__ == "__main__":
    resize_image("nature.jpg", "output.jpg", 100, 100)