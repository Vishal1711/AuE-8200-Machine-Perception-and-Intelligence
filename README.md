# AuE-8200-Machine-Perception-and-Intelligence
 CU-ICAR Spring 2022
 ### Note - Detail work of each homework is in the Readme of the respective homework folder

## Homework 1

1. Continuous-time signal and its FFT
2. Discrete signal and its FFT
3. Convolution operation on 1D signal




## Homework 2
The [nuScenes] (https://www.nuscenes.org/nuscenes) dataset is a public large-scale dataset for autonomous driving developed by the team at Motional (formerly nuTonomy). Motional is making driverless vehicles a safe, reliable, and accessible reality. This data aims to support public research into computer vision and autonomous driving.
1. Visualize Lidar point cloud data
2. Visualize Radar data
3. Visualize Radar data projection on image
4. Visualize LiDAR data projection on image

Tools that I used for this Assignment-
- NuScene develop kit
- OpenCV
- Open3D

## Homework 3

Write code rather than using any direct build-in implementation from 3rd party (like Matlab, Python, or others) libraries.
1. RGB to gray, using a standard RGB-intensity conversion approach like NTSC and implement the convolution (using basic arithmetic operations only, rather than build-in conv()) of Sobel kernel.
2. Implement a function to perform histogram equalization for image, visualize histogram-equalized image and its histogram distribution.
3. Apply Hough transformation or other line detection approach to detect multiple lines in the image. Visualize the lines in the image space and in the transformed space.

## Homework 4



1. Select a frame (or a few frames) of LiDAR data file, parse the file and visualize the 3D point cloud of that frame.
2. Perform voxel filter (or box grid filter) to down-sample all the 3D point cloud points to the 3D voxel space points, and visualize the result points.
3. Apply RANSAC algorithm (or any others you prefer) to the 3D voxel space points to find a ground plane model.
4. Perform a x-y projection to the off-ground points, and get a 2D matrix (you decide what is the element value), and visualize the 2D matrix as an image.
5. Based on the raw point cloud data (Questions 1), which is in Cartesian Coordinate, represent and visualize all the point cloud in 3D of horizontal and vertical angels (converted using Polar Coordinate).


## Homework 5

### TorchVision Instance Segmentation Finetuning Tutorial

For this tutorial, we will be finetuning a pre-trained Mask R-CNN model in the Penn-Fudan Database for Pedestrian Detection and Segmentation. It contains 170 images with 345 instances of pedestrians, and we will use it to illustrate how to use the new features in torchvision in order to train an instance segmentation model on a custom dataset.

First, need to install pycocotools. This library will be used for computing the evaluation metrics following the COCO metric for intersection over union.





