import os
import random
import shutil

def split_data(images_dir, labels_dir, test_dir, validation_dir, test_percentage=10, validation_percentage=5):
    # Create output directories if they don't exist
    os.makedirs(test_dir, exist_ok=True)
    os.makedirs(validation_dir, exist_ok=True)

    # Get the list of images in the images directory
    image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Calculate the number of images for test and validation sets
    num_test_images = int(len(image_files) * (test_percentage / 100.0))
    num_validation_images = int(len(image_files) * (validation_percentage / 100.0))

    # Randomly select images for the test set
    test_images = random.sample(image_files, num_test_images)
    for image in test_images:
        image_path = os.path.join(images_dir, image)
        label_path = os.path.join(labels_dir, os.path.splitext(image)[0] + '.txt')
        shutil.move(image_path, os.path.join(os.path.join(test_dir, 'images'), image))
        shutil.move(label_path, os.path.join(os.path.join(test_dir, 'labels'), os.path.splitext(image)[0] + '.txt'))

    # Randomly select images for the validation set
    validation_images = random.sample([f for f in image_files if f not in test_images], num_validation_images)
    for image in validation_images:
        image_path = os.path.join(images_dir, image)
        label_path = os.path.join(labels_dir, os.path.splitext(image)[0] + '.txt')
        shutil.move(image_path, os.path.join(os.path.join(validation_dir, 'images'), image))
        shutil.move(label_path, os.path.join(os.path.join(validation_dir, 'labels'), os.path.splitext(image)[0] + '.txt'))

if __name__ == "__main__":
    # Replace these paths with your actual paths
    images_directory = '/home/suryansh/Documents/GitHub/Plant-disease-detection/PlantDoc-Object-Detection-Dataset-master/images'
    labels_directory = '/home/suryansh/Documents/GitHub/Plant-disease-detection/PlantDoc-Object-Detection-Dataset-master/labels'
    test_directory = '/home/suryansh/Documents/GitHub/Plant-disease-detection/PlantDoc-Object-Detection-Dataset-master/test'
    validation_directory = '/home/suryansh/Documents/GitHub/Plant-disease-detection/PlantDoc-Object-Detection-Dataset-master/validation'

    split_data(images_directory, labels_directory, test_directory, validation_directory)
