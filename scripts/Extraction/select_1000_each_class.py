from sys import argv
from shutil import copy
import os

input_images_directory = argv[1]
output_images_directory = 'scratch/{}'.format(argv[2])

for cluster_folder in os.listdir(input_images_directory):

    img_path = os.path.join(input_images_directory, cluster_folder)

    new_imgs = os.listdir(img_path)
    new_imgs_sliced = new_imgs[:1000]

    for img in new_imgs_sliced:
        src = os.path.join(img_path, img)
        copy(src, os.path.join(output_images_directory, cluster_folder))
