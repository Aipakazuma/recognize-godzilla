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
    results = []
    results_2 = np.zeros((1, 19200))
    for i in series:
        images = glob.glob(i + '/*')
        data_sets = {
            'data': [],
            'label': []
        }
        for image in images:
            r, g, b = read_image(image)
            rgb = np.concatenate((r, g, b), axis=0).reshape(1, 19200)
            data_sets['data'].append(rgb)
            # data_sets['label'].append(label)
            results_2 = np.vstack([results_2, rgb])

        label += 1
        results.append(data_sets)
    numpy_array = np.concatenate([np.array(results[0]['data']), np.array(results[1]['data'])], axis=0)
    # numpy_array_reshape = numpy_array.reshape(numpy_array.shape[0], 3, 80, 80)
    print(results_2.shape)
    return results


def main():
    read()


if __name__ == '__main__':
    main()
