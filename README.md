# Machine Learning for Morphological Galaxy Classification

The code in this repository is largely based on the paper ["Galaxy Morphological Classification with Zernike Moments and Machine Learning Approaches"](https://doi.org/10.3847/1538-4365/ada8ab) by Ghaderi et al. (2025) and [their code](https://github.com/hmddev1/machine_learning_for_morphological_galaxy_classification?tab=readme-ov-file). It was modified and extended by [Florine H. J. Koch](https://github.com/florine680), [Isa Chousein Basia](https://github.com/IssaHB), and [Madalena Lima](https://github.com/mlima3) as part of a group project for the "Deep Learning in Physics" graduate-level course offered by the University of Groningen, The Netherlands. 

## Overview

We re-produced the results for five different classification models used by the original authors of the paper, including:

1. Support Vector Machine (SVM) with Zernike Moments (ZMs)
2. 1D-Convolutional Neural Network (1D-CNN) with ZMs
3. 2D-CNN with Vision Transformer (ViT) and original images
4. ResNet50 with ViT and original images
5. VGG16 with ViT and original images

The SVM and 1D-CNN models utilized Zernike moments (ZMs) extracted from the images, while the 2D-CNN, ResNet5, and VGG16 with Vision Transformer (ViT) models were designed based on the original images.

We also extended these results to include:

1. Improvements on the models used by Ghaderi et al.
2. Performance of the models on a modified dataset
3. Classification of "odd" galaxies (e.g., mergers, irregulars, lenses, etc.)

## Data
The data files are accessible from [here](https://drive.google.com/drive/folders/1pwNk-8VJ-a_jUn84DyPYRYmhYSmki1dh) and include two categories:

- galaxy-nongalaxy
- galaxy
  
Each category contains two folders:

- images: This folder includes the original images for galaxy-nongalaxy and cropped images for galaxy classifiers.
- ZMs: This folder contains Zernike Moments (ZMs) data sets in CSV file format.

## Task Allocation
### Florine
- A
- B
  
### Isa
- Prepared a dataset for odd galaxies (e.g., mergers, irregulars, etc.) and trained Model III of Ghaderi et al. (2025) on this dataset.
- Computed the Zernike Moments (ZMs) from the original image dataset used by Ghaderi et al. (2025) for 45 different Zernike Polynomial orders and trained their Model I on these ZMs to illustrate the relationship between accuracy and ZP order.

### Madalena
- Created a modified dataset by adjusting the voting threshold and trained all five models on this dataset.
- Reproduced paper results.
