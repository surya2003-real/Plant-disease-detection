# Plant disease detection
Plant disease detection is important for large scale farming. This project aims to detect plant disease using deep learning.
We have used the plantdoc dataset for this project.
We have used the following models for this project:
- YOLOv8
- ViT-base-patch-16
- VGG16
- VGG19
- ViT-B16

## Tasks involved
## 1. Segmentation:
- The first task involved for detecting diseases in plants is to segment the images of plant leaves from the images available.
- For performing segmentation we've used YOLOv8 model which was trained on the plantdoc dataset to detect the leaves of the plants.
- Results:
    - We obtained a **mAP50 of 52.00%** on the test set.
    - We obtained a **mAP of 34.09%** on the test set.
## 2. Classification:
- The second task involved is to predict the disease class of the leaves of the plants.
- For performing classification we've trianed and tested the following models:
- ### **Visual Transformer:**
    - We have used two models of visual transformers for this project:
        - ViT-base-patch-16
        - ViT-B16
    - Results:
        - ViT-base-patch-16:
            - We obtained a **test accuracy of 75.05%**
        - ViT-B16:
            - We obtained a **test accuracy of 73.08%**
- ###  **Visual Geometry Group(VGG):**
    - We have used two models of visual geometry group for this project:
        - VGG16
        - VGG19
    - Results:
        - VGG16:
            - We obtained a **test accuracy of 59.47%**
        - VGG19:
            - We obtained a **test accuracy of 57.59%**
## 3. Plant Disease Detection Pipeline:
- The third task involved is to create a pipeline for detecting plant diseases.
- These are the results of the following pipelines:
    - YOLOv8 + ViT-base-patch-16:
        - We obtained a **mAP50 of 37.78%** on the test set.
        - We obtained a **mAP of 26.52%** on the test set.
    - YOLOv8 + ViT-B16:
        - We obtained a **mAP50 of 35.46%** on the test set.
        - We obtained a **mAP of 25.17%** on the test set.
    - YOLOv8 + VGG16:
        - We obtained a **mAP50 of 18.80%** on the test set.
        - We obtained a **mAP of 25.74%** on the test set.
    - YOLOv8 + VGG19:
        - We obtained a **mAP50 of 20.59%** on the test set.
        - We obtained a **mAP of 28.58%** on the test set.

## Dataset:
- We have used the plantdoc dataset for this project.
- The dataset can be downloaded from [here](https://github.com/pratikkayal/PlantDoc-Object-Detection-Dataset).

## Complete Results:
- The complete results of can be found [here](https://docs.google.com/spreadsheets/d/1Agrq7cZtefHFdXKagkL3ytCqYO0rXbqO6TLNiWNCzPU/edit#gid=43507475).

## Special Thanks:
- We would like to thank [Prof. Tushar Sandhan](https://home.iitk.ac.in/~sandhan/) for guiding us throughout the project.
- We would like to thank [Mr. Debojyoti Misra](https://in.linkedin.com/in/debojyoti-misra-442511143) for guiding us throughout the project.
- We would like to thank [Pratik Kayal](https://github.com/pratikkayal) for providing us with the plantdoc dataset.