import os
from PIL import Image
import pandas as pd
import shutil
# Class mapping
class_mapping = {'Apple Scab Leaf': 0, 'Apple leaf': 1, 'Apple rust leaf': 2, 'Bell_pepper leaf': 3, 'Bell_pepper leaf spot': 4, 'Blueberry leaf': 5, 'Cherry leaf': 6, 'Corn Gray leaf spot': 7, 'Corn leaf blight': 8, 'Corn rust leaf': 9, 'Peach leaf': 10, 'Potato leaf': 11, 'Potato leaf early blight': 12, 'Potato leaf late blight': 13, 'Raspberry leaf': 14, 'Soyabean leaf': 15, 'Squash Powdery mildew leaf': 16, 'Strawberry leaf': 17, 'Tomato Early blight leaf': 18, 'Tomato Septoria leaf spot': 19, 'Tomato leaf': 20, 'Tomato leaf bacterial spot': 21, 'Tomato leaf late blight': 22, 'Tomato leaf mosaic virus': 23, 'Tomato leaf yellow virus': 24, 'Tomato mold leaf': 25, 'Tomato two spotted spider mites leaf': 26, 'grape leaf': 27, 'grape leaf black rot': 28}
def convert_to_yolo_format(xmin, ymin, xmax, ymax, img_width, img_height):
    # YOLO format: centerX, centerY, width, height (all normalized)
    x_center = (xmin + xmax) / (2 * img_width)
    y_center = (ymin + ymax) / (2 * img_height)
    width = (xmax - xmin) / img_width
    height = (ymax - ymin) / img_height

    return x_center, y_center, width, height

def process_images(csv_path, images_dir, output_images_dir, output_labels_dir):
    df = pd.read_csv(csv_path)
    # Iterate through each image in the TRAIN directory
    k=236
    new_df = pd.read_csv('./new_labels2.csv')
    data_list = []
    flag=1
    for filename in os.listdir(images_dir):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Construct image and annotation paths
            image_path = os.path.join(images_dir, filename)
            label_path = os.path.join(output_labels_dir, 'img'+str(k) + '.txt')

            # Load image to get width and height
            img = Image.open(image_path)
            img_width, img_height = img.size
            df_filtered=df[df['filename']==filename]
            flag=0
            for index, row in df_filtered.iterrows():
                flag=1
                # For simplicity, assuming some dummy box coordinates here
                filename,width,height,cls,xmin,ymin,xmax,ymax = row
                # Convert box coordinates to YOLO format
                x_center, y_center, width, height = convert_to_yolo_format(
                    float(xmin), float(ymin), float(xmax), float(ymax), img_width, img_height)

                # Save YOLO format annotation to label file
                with open(label_path, 'a') as label_file:
                    label_file.write(f"{class_mapping[cls]} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
                data_list.append({'filename': 'img'+str(k)+'.jpg','width': row['width'],'height': row['height'],'class': row['class'],'xmin': row['xmin'],'ymin': row['ymin'],'xmax': row['xmax'],'ymax': row['ymax']})

            # Copy image to output images directory
            if flag==1:
                output_image_path = os.path.join(output_images_dir, 'img'+str(k)+'.jpg')
                shutil.copyfile(image_path, output_image_path)
                k+=1
    new_df1 = pd.DataFrame(data_list)
    new_df = pd.concat([new_df, new_df1], ignore_index=True)
    # new_df= pd.DataFrame(data_list)
    new_df.to_csv('/home/suryansh/Documents/GitHub/Plant-disease-detection/PlantDoc-Object-Detection-Dataset-master/new_labels2.csv', index=False)

if __name__ == "__main__":
    # Replace these paths with your actual paths
    csv_path='/home/suryansh/Documents/GitHub/Plant-disease-detection/PlantDoc-Object-Detection-Dataset-master/train_labels.csv'
    images_directory = '/home/suryansh/Documents/GitHub/Plant-disease-detection/PlantDoc-Object-Detection-Dataset-master/TRAIN'
    output_images_directory = '/home/suryansh/Documents/GitHub/Plant-disease-detection/PlantDoc-Object-Detection-Dataset-master/images'
    output_labels_directory = '/home/suryansh/Documents/GitHub/Plant-disease-detection/PlantDoc-Object-Detection-Dataset-master/labels'

    # Create output directories if they don't exist
    os.makedirs(output_images_directory, exist_ok=True)
    os.makedirs(output_labels_directory, exist_ok=True)

    process_images(csv_path, images_directory, output_images_directory, output_labels_directory)
