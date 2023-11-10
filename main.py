# Import necessary libraries
from ultralytics import YOLO
from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf
from PIL import Image as PILImage
import io
from IPython.display import Image, display
from PIL import Image as PILImage
import numpy as np
import tensorflow as tf
import io

# Load the YOLO model
yolo_model = YOLO('/kaggle/working/best.pt')

# Load the ResNet50 model
model2 = load_model('/kaggle/input/plantcroppedresnet/model_resnet50.h5')

# Class mapping
class_mapping = {'Apple Scab Leaf': 0, 'Apple leaf': 1, 'Apple rust leaf': 2, 'Bell_pepper leaf': 3, 'Bell_pepper leaf spot': 4, 'Blueberry leaf': 5, 'Cherry leaf': 6, 'Corn Gray leaf spot': 7, 'Corn leaf blight': 8, 'Corn rust leaf': 9, 'Peach leaf': 10, 'Potato leaf': 11, 'Potato leaf early blight': 12, 'Potato leaf late blight': 13, 'Raspberry leaf': 14, 'Soyabean leaf': 15, 'Squash Powdery mildew leaf': 16, 'Strawberry leaf': 17, 'Tomato Early blight leaf': 18, 'Tomato Septoria leaf spot': 19, 'Tomato leaf': 20, 'Tomato leaf bacterial spot': 21, 'Tomato leaf late blight': 22, 'Tomato leaf mosaic virus': 23, 'Tomato leaf yellow virus': 24, 'Tomato mold leaf': 25, 'Tomato two spotted spider mites leaf': 26, 'grape leaf': 27, 'grape leaf black rot': 28}

# Directory containing images to predict
image_directory = '/kaggle/input/plant-doc-dataset/PlantDoc-Dataset/test/Peach leaf'
# Predict objects using YOLO
results = yolo_model.predict(image_directory)

# Create empty lists to store results
resized_cropped_images = []
predicted_classes = []

# Define the target size for ResNet50
target_size = (256, 256)

# Process YOLO results
for x in results:
    for r in x:
        # Get the image and bounding box
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = PILImage.fromarray(im_array[..., ::-1])  # Convert BGR to RGB PIL image
        bbox = r.boxes.data[0, :4].cpu().numpy()  # Get the bounding box

        # Crop the detected object from the image
        cropped_im = im.crop((bbox[0], bbox[1], bbox[2], bbox[3]))

        # Resize the cropped image to the target size
        resized_cropped_im = cropped_im.resize(target_size)

        # Save the resized and cropped image to a BytesIO object
        img_io = io.BytesIO()
        resized_cropped_im.save(img_io, 'PNG')

        # Append the resized and cropped image to the list
        resized_cropped_images.append(img_io.getvalue())

        # Predict the class of the cropped object using the loaded ResNet50 model
        img_array = np.array(resized_cropped_im)
        img_array = tf.image.resize(img_array, (256, 256))
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model2.predict(img_array)
        predicted_class_index = np.argmax(predictions, axis=1)
        predicted_class_label = list(class_mapping.keys())[predicted_class_index[0]]
        predicted_classes.append(predicted_class_label)

# Display the resized and cropped images with predicted classes
for img_data, predicted_class in zip(resized_cropped_images, predicted_classes):
    display(Image(data=img_data), f"Predicted Class: {predicted_class}")