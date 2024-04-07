#!/opt/homebrew/bin/python3.11
import os
import sys
from PIL import Image


def convert_webp_to_jpg(source_path, target_path):
    """
    Converts a WEBP image to JPG format.

    Parameters:
    - source_path: The file path of the source WEBP image.
    - target_path: The file path where the JPG image will be saved.
    """
    try:
        with Image.open(source_path) as image:
            image.convert("RGB").save(target_path, "jpeg")
        print(f"Conversion successful: {target_path}")
    except Exception as e:
        print(f"Error converting image: {e}")


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: python script.py source.webp target.jpg")
        sys.exit(1)

    source_path, target_path = args[0], args[1]
    convert_webp_to_jpg(source_path, target_path)


if __name__ == "__main__":
    main()
