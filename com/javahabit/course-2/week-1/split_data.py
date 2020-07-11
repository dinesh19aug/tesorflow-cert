

import os
import zipfile
import random
import tensorflow as tf
import shutil
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from shutil import copyfile
from os import getcwd

SOURCE_HORSE_DIR='C:/Users/dines/Downloads/horse-or-human/horses'
SOURCE_HUMAN_DIR='C:/Users/dines/Downloads/horse-or-human/humans'
DEST_TRAIN_HORSE_DIR='C:/Users/dines/Downloads/processed/train/horse'
DEST_TEST_HORSE_DIR='C:/Users/dines/Downloads/processed/test/horse'

#copy one file
# os.listdir(DIRECTORY) gives you a listing of the contents of that directory
# os.path.getsize(PATH) gives you the size of the file
# copyfile(source, destination) copies a file from source to destination
# random.sample(list, len(list)) shuffles a list

#shuffle
source_horse_files=random.sample(os.listdir(SOURCE_HORSE_DIR), len(os.listdir(SOURCE_HORSE_DIR)))
counter=0
for i in range(0, int(0.9*500)):
    copyfile(SOURCE_HORSE_DIR+"/"+source_horse_files[i], DEST_TRAIN_HORSE_DIR+"/"+source_horse_files[i])
    counter = counter+1

print('Copied Training horse ')
for i in range(counter, len(source_horse_files)):
    copyfile(SOURCE_HORSE_DIR+"/"+source_horse_files[i], DEST_TEST_HORSE_DIR+"/"+source_horse_files[i])

print('Copied Testing horse ')




