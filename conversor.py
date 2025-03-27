import cv2

def crop_center(image_path, output_path, crop_width = 0, crop_height = 0):
    """
    Crop the center of an image to the specified width and height.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or unable to read.")
    
    height, width, _ = image.shape

    if crop_width == 0 or crop_height == 0:
        crop_height = min(height, width)
        crop_width = crop_height

    # Calculate the cropping box
    start_x = max((width - crop_width) // 2, 0)
    start_y = max((height - crop_height) // 2, 0)
    end_x = start_x + crop_width
    end_y = start_y + crop_height

    # Perform the crop
    cropped_image = image[start_y:end_y, start_x:end_x]

    # Save the cropped image
    cv2.imwrite(output_path, cropped_image)

def convert_jpeg_to_png(jpeg_path, png_path):
    """
    Convert a JPEG image to PNG format.
    """
    image = cv2.imread(jpeg_path)
    if image is None:
        raise ValueError("Image not found or unable to read.")
    
    # Save the image in PNG format
    cv2.imwrite(png_path, image)

name = "capadocia"

jpeg_path = "images/" + name + ".jpg"
png_path = "images/" + name + ".png"

# crop_center(jpeg_path, "cropped.jpg")

convert_jpeg_to_png("cropped.jpg", png_path)