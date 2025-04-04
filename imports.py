# Dependencies for models based on Zernike Moments
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import label_binarize
from sklearn.metrics import (roc_curve, roc_auc_score, auc, log_loss,
                             precision_score, recall_score, f1_score,
                             accuracy_score, classification_report,
                             ConfusionMatrixDisplay, confusion_matrix)


import pandas as pdr
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

#Tensorflow
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense
from tensorflow.keras.layers import (Dense, Dropout,BatchNormalization, Input, Conv1D, Flatten,
                             MaxPooling1D)
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping


import cv2
import os
from skimage.measure import label
from skimage.transform import resize
from skimage.segmentation import slic, mark_boundaries
from skimage.color import label2rgb
from skimage.measure import label, regionprops


#Scikit_learn
from sklearn.model_selection import train_test_split
from sklearn.metrics import (roc_curve, roc_auc_score, auc, log_loss,
                             precision_score, recall_score, f1_score,
                             accuracy_score, classification_report,
                             ConfusionMatrixDisplay, confusion_matrix)
from sklearn import metrics
from sklearn.preprocessing import label_binarize
from sklearn.model_selection import StratifiedKFold


# Dependencies for models based on original images
import random
from PIL import Image
import pickle
import seaborn as sns

#Tensorflow
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras import Sequential
from tensorflow.keras.layers import (Dense, Dropout, Input,Conv2D, Flatten, MaxPooling2D, BatchNormalization)
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.applications import ResNet50, VGG16
from keras.callbacks import EarlyStopping

#Torch
import torch
import torch.nn as nn
from torchvision import transforms