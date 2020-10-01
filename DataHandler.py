import glob, shutil, os, random
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

food_classes = ['bread', 'dairy_product', 'dessert', 'egg', 'fried_food', 'meat',
                'noodles_pasta', 'rice', 'seafood', 'soup',
                'vegetable']  # According to data set at 0 index food type at 1st index food type viceversa


def split_data_into_class_folders(path_to_data, class_id):
    imgs_path = glob.glob(path_to_data + '*.jpg')

    for path in imgs_path:
        basename = os.path.basename(path)

        if basename.startswith(str(class_id) + '_'):
            path_to_save = os.path.join(path_to_data, food_classes[class_id])

            if not os.path.isdir(path_to_save):
                os.makedirs(path_to_save)

            shutil.move(path, path_to_save)


if __name__ == '__main__':

    split_data_switch = True

    path_to_train_data = '/home/psp/Desktop/food/archive/food-11/training/'
    path_to_val_data = '/home/psp/Desktop/food/archive/food-11/validation/'
    path_to_eval_data = '/home/psp/Desktop/food/archive/food-11/evaluation/'

    if split_data_switch:
        for i in range(11):
            split_data_into_class_folders(path_to_val_data, i)