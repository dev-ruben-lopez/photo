from PIL import Image
import os

def create_thumbnail(source_file_path, dest_file_path):
    # Open the image file
    img = Image.open(source_file_path)

    # Set the maximum size of the thumbnail
    max_size = (128, 128)

    # Resize the image while maintaining the aspect ratio
    img.thumbnail(max_size)

    # Set the maximum file size of the thumbnail
    max_file_size = 50 * 1024  # 50 KB

    # Loop until the file size of the thumbnail is below the maximum
    while True:
        # Save the thumbnail with a high quality setting
        img.save(dest_file_path, optimize=True, quality=90)

        # Check the file size of the thumbnail
        if os.path.getsize(dest_file_path) <= max_file_size:
            break

        # If the file size is too large, reduce the quality
        img.save(dest_file_path, optimize=True, quality=50)
