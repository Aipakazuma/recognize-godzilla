# -*- coding: utf8 -*-

import cv2
import numpy as np
import glob


def read_image(image):
    image_object = cv2.imread(image)
    image_object_rgb = cv2.cvtColor(image_object, cv2.COLOR_BGR2RGB)
    image_object_rgb_array = np.array(image_object_rgb)
    r = image_object_rgb_array[:, :, 0]
    g = image_object_rgb_array[:, :, 1]
    b = image_object_rgb_array[:, :, 2]
    return r, g, b


def read():
    series = glob.glob('../data/img/*')
    label = 0
    labels = np.zeros([1], dtype='uint8')
    results = np.zeros((1, 19200))
    for i in series:
        label += 1
        images = glob.glob(i + '/*')
        for image in images:
            r, g, b = read_image(image)
            rgb = np.concatenate((r, g, b), axis=0).reshape(1, 19200)
            results = np.vstack([results, rgb])
            labels = np.vstack([labels, np.array([label])])
    return results, labels


def main():
    print(read())


if __name__ == '__main__':
    main()
