from PIL import Image
import os

def convert_image(input_path, output_path, output_format):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format=output_format)
        print(f"Image saved to {output_path} in {output_format} format.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_path = input("Enter the path of the image to convert: ")
    output_path = input("Enter the output path for the converted image: ")
    output_format = input("Enter the desired output format (e.g., JPEG, PNG, BMP): ")
    
    convert_image(input_path, output_path, output_format)
