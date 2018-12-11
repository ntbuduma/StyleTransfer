from __future__ import print_function

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from PIL import Image
import matplotlib.pyplot as plt

import torchvision.transforms as transforms
import torchvision.models as models
import torchvision

import copy

import os
import cv2

from multiprocessing.dummy import Pool as ThreadPool
import time

image_folder = "./generated_frames 2/"
images = [img for img in os.listdir("generated_frames 2")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

img_list = []
for filename in os.listdir("generated_frames 2"):
    img_list.append((filename, int(filename[5:-4])))
img_list = sorted(img_list, key = lambda x : x[1])

print(img_list)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
video_name = 'video_test_finally.mp4'
video = cv2.VideoWriter(video_name, fourcc, frameSize=(width,height), fps=25)
image_folder = "./generated_frames 2/"
for img_tup in img_list:
    video.write(cv2.imread(os.path.join(image_folder, img_tup[0])))  
print("Here")
cv2.destroyAllWindows()
video.release()