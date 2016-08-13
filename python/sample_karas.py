# -*- coding: utf8 -*-

from keras.models import Sequential
from keras.datasets import cifar10
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adadelta
from keras.utils import np_utils
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils.visualize_util import model_to_dot, plot
from keras import backend as K
import numpy as np
from IPython.display import SVG

from matplotlib import pyplot as plt
import matplotlib.image as mpimg
plt.style.use("ggplot")
np.random.seed(13)

batch_size = 32
nb_classes = 10
nb_epoch = 4
nb_filter = 10

# input image dimensions
img_rows, img_cols = 32, 32
# the CIFAR10 images are RGB
img_channels = 3

# the data, shuffled and split between train and test sets
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

np_utils.to_categorical(y_train, nb_classes)


import read_image

datasets, labels = read_image.read()
np.random.shuffle(datasets)
np.random.shuffle(labels)
X_train = datasets[:16].reshape(16, 3, 80, 80)
X_test = datasets[17:].reshape(15, 3, 80, 80)
y_train = labels[:16]
y_test = labels[17:]

X_train = X_train.astype('float32') # floatに変換
X_test = X_test.astype('float32')
X_train /= 255 # 0 ~ 1の範囲で学習させるため
X_test /= 255

nb_classes = 3

Y_train = np_utils.to_categorical(y_train, nb_classes) # データのラベルをone-hot表現に変換
Y_test = np_utils.to_categorical(y_test, nb_classes)

