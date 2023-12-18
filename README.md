# Plant disease detection
Plant disease detection is important for large scale farming. This project aims to detect plant disease using deep learning.
We have used the plantdoc dataset for this project.
We have used the following models for this project:
- YOLOv8
- Visual Transformer(ViT)
- ResNet50

## Tasks involved
## 1. Segmentation:
- The first task involved for detecting diseases in plants is to segment the images of plant leaves from the images available.
- For performing segmentation we've used YOLOv8 model which was trained on the plantdoc dataset to detect the leaves of the plants.
- Results:
    - We obtained a **mAP50 of 89.3%**
    - We obtained a **mAP50-95 of 65.5%**
## 2. Classification:
- The second task involved is to predict the disease class of the leaves.
- For performing classification we've trianed and tested two models: Visual Transformer(ViT) and ResNet50 models.
- ResNet50:
    - It was
- Visual Transformer:
    - 


