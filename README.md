# Archeological Textures Segmentation
The segmentation of different **geoemetric textures** in a 3D image could be useful to classify different styles and/or peculiar characteristics that should be in common in different objects: a sculture, a building, an archeological fragment, for example. However, if part segmentation is a challenging 3D recognition task, **3D pattern recognition** it's more challenging. 

In this work, given a dataset of archeological 3D images defined by a different number of *point cloud*, an import type of geometric data structure, the aim is to use [Pointnet](https://github.com/charlesq34/pointnet), a neural network that makes deep learning on point sets for 3D classification and segmentation, to locate and segment geometric textures and analyze the results of this computation.

In the code it's presented a part to make compatibile the dataset (originally in Matlab) to the input required by the network used for training and testing, **pointnet**. 

Created by [Lorenzo Pisaneschi](https://www.linkedin.com/in/lorenzo-pisaneschi-aaa4b3123).


