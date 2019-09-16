# Archeological Textures Segmentation
The segmentation of different **geoemetric textures** in a 3D image could be useful to classify different styles and/or peculiar characteristics that should be in common in different objects: a sculture, a building, an archeological fragment, for example. However, if part segmentation is a challenging 3D recognition task, **3D pattern recognition** it's more challenging. 

In this work, given a dataset of archeological 3D images defined by a different number of *point cloud*, an import type of geometric data structure, the aim is to use [Pointnet](https://github.com/charlesq34/pointnet), a neural network that makes deep learning on 3D point sets, to locate and segment geometric textures and analyze the efficacy of this task

In the code it's presented a part to make compatibile the dataset (originally in Matlab) to the input required by the network used for training and testing, **pointnet**. 

Created by [Lorenzo Pisaneschi](https://www.linkedin.com/in/lorenzo-pisaneschi-aaa4b3123).

# Getting started

For use the software, firstly clone this repository:

**Linux**
```
git clone https://github.com/pisalore/Archeological-Textures-Segmentation
```

**Windows**

If you are a Windows User, you can clone the repository using GitHub Desktop (download it [here](https://desktop.github.com/)).

## Prerequisites

The code it's all implemented in **Python**. So, you have to install [Python 3](https://www.python.org/downloads/) firstly.
Once Python it's installed, you need:
-[Tensorflow](https://www.tensorflow.org/).
-[h5py](https://github.com/h5py/h5py) (for handling h5 files that are the effective inputs of the network).
-[Scipy] (https://www.scipy.org/index.html) (for manipulating and converting matlab files).
-Numpy
-Matplotlib (optional).
You can install all these packages via **pip**.
