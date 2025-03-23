# Machine Learning for Morphological Galaxy Classification

The code in this repository is largely based on the paper ["Galaxy Morphological Classification with Zernike Moments and Machine Learning Approaches"](https://doi.org/10.3847/1538-4365/ada8ab) by Ghaderi et al. (2025). It was modified and extended by [Florine H. J. Koch](https://github.com/florine680), [Isa Chousein Basia](https://github.com/IssaHB), and [Madalena Nunes De Lima](https://github.com/mlima3) as part of a group project for the "Deep Learning in Physics" graduate-level course offered by the University of Groningen, The Netherlands. 

## Overview

We re-produced the results for five different classification models used by the original authors of the paper, including:

1. Support Vector Machine (SVM) with Zernike moments (ZMs)
2. 1D-Convolutional Neural Network (1D-CNN) with ZMs
3. 2D-CNN with Vision Transformer (ViT) and original images
4. ResNet50 with ViT and original images
5. VGG16 with ViT and original images

The SVM and 1D-CNN models utilized Zernike moments (ZMs) extracted from the images, while the 2D-CNN, ResNet5, and VGG16 with Vision Transformer (ViT) models were designed based on the original images.

We also extended these results for three more classifficaiton models designed based on the original images, including:

1. AlexNet
2. ZFNet
3. Dense Convolutional Networks (DenseNet)

## Data
The data files are accessible from [here](https://drive.google.com/drive/folders/1pwNk-8VJ-a_jUn84DyPYRYmhYSmki1dh) and include two categories:

- galaxy-nongalaxy
- galaxy
  
Each category contains two folders:

- images: This folder includes the original images for galaxy-nongalaxy and cropped images for galaxy classifiers.
- ZMs: This folder contains Zernike Moments (ZMs) data sets in CSV file format.
