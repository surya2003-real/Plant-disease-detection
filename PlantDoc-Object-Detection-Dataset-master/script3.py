import os
import pandas as pd
from PIL import Image

def crop_and_save_images(images_dir, csv_path, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read CSV file
    df = pd.read_csv(csv_path)

    # List all image files in the directory
    image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        image_path = os.path.join(images_dir, image_file)

        # Filter rows in the DataFrame for the current image file
        image_data = df[df['filename'] == image_file]

        # Iterate through bounding boxes for the current image
        for index, row in image_data.iterrows():
            xmin, ymin, xmax, ymax = row['xmin'], row['ymin'], row['xmax'], row['ymax']

            # Open the image
            image = Image.open(image_path)

            # Crop the image based on xmin, ymin, xmax, ymax
            cropped_image = image.crop((xmin, ymin, xmax, ymax))

            if cropped_image.mode != 'RGB':
                cropped_image = cropped_image.convert('RGB')

            os.makedirs(os.path.join(output_dir, row['class']), exist_ok=True)
            
            # Save the cropped image in the original format
            output_path = os.path.join(output_dir, row['class'], f"{os.path.splitext(image_file)[0]}_{index + 1}.jpg")
            cropped_image.save(output_path, format='JPEG')

if __name__ == "__main__":
    # Replace these paths with your actual paths
    images_directory = '../datasets/test/images'
    csv_file_path = '../YOLOv8_training/new_labels.csv'
    output_directory = '../plantdoc_ViT_training/cropped_images_dataset/test'

    crop_and_save_images(images_directory, csv_file_path, output_directory)
