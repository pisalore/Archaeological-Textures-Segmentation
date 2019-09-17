# Archeological Textures Segmentation

![banner](https://github.com/pisalore/Archeological-Textures-Segmentation/blob/master/doc/ATS.png)
![patterns](https://github.com/pisalore/Archeological-Textures-Segmentation/blob/master/doc/patterns1.png)

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

- [Tensorflow](https://www.tensorflow.org/).
- [h5py](https://github.com/h5py/h5py) (for handling h5 files that are the effective inputs of the network).
- [Scipy](https://www.scipy.org/index.html) (for manipulating and converting matlab files).
- [Plyfile](https://pypi.org/project/plyfile/) very important for ply files manipulation.
- Numpy
- Matplotlib (optional).

You can install all these packages via **pip**.

Once installed, you can use the code and then train and test.

## Generate the dataset

Once you have succesfully cloned the repository and installed all the required parts, you have to generate the compatible pointnet dataset from the **.mat** files you have. In fact, you have two folders containing .mat files:

- Dataset_processed folder, which contain the point cloud coordinates.
- SHREK18_Labels, consisting in the Ground Truth of our 3D models.

For obtaining the right dataset, you have to do the following steps:

1. Generate the **.seg files** for labelling vertices (infact, the original dataset provides labelled factes, not vertices that are required in pointnet) running the *make_seg_files*; then, generate the **seg filelist** running *make_seg_file_list*.
```
python3 make_seg_files.py
```
```
python3 make_seg_file_list.py
```

2. Generate the **.ply files** for obtain Polygon File Format files for visualization (for example in [MeshLab](http://www.meshlab.net/#download)) and obtaining .h5 files in a subsequent step, running *make_ply_files; then, generate also the 
**ply filelist** running *make_py_file_list*.
```
python3 make_ply_files.py
```
```
python3 make_ply_file_list.py
```

3. Genarate the **.pts files** which contains the point cloud coordinates and are needful for testing, running *make_pts_files*; than, like for .ply and .seg files, generate the **pts fileslist** runing *make_pts_file_list*.
```
python3 make_pts_files.py
```
```
python3 make_pts_file_list.py
```

Now you have all the necessary to use pointnet, but ther is a fundamental step.
So, pointnet has been projected to work with input made of 256, 512, 1024 or 2048 points; our dataset it's formed by images of different number of points (like 60243, 55480, 10495...). The idea it's to train and test the network using one image at time, splitting out its points in sub-dataset consisting in sub-images of 256, 512, 1024 or 2048 points. 
The code presented split out an image in sub-images of 512 points, because experiments find out which splitting in sub samples of 512 points improves accuracy (but you can obviously using differents splitting criteria).
So, all you have to do it's to run *obtain_dataset* script.
```
python3 obtain_dataset.py
```
Once done this step, you have to create the *training_filelist.txt* and the *testing_filellst.txt* in the data folder, and then fill them with the name of the files you want to use for training and testing in the **train** procedure using pointnet. Remember: you have to choose a number of files for training and testing list divisible for the batch size selected (the default batch size is 4, so for example, if you have obtained from an image of 
10495 points 20 sub images each made of 512 points, it's advisible to select 16 files for training and 4 for testing).

Now, the most important step it's to generate the **.h5 files for training and testing**, the real pointnet input. You have simply to run the *make_hdf5_files*, which will be saved in the data/hdf5_data folder.

```
python3 make_hdf5_files.py
```
The last step, it's to generate the testing list running the *make_testing_file_list* script.
```
python3 make_testing_file_list.py
```
That's all. Now you can train and test the network with the created dataset.
Firstly, you have to run the script **train.py**:

```
python3 train.py
```
This script will generate a *train_results* folder with a diagram describing the train process, logs and trained model.
Then, you have to run the **test.py** script:
```
python3 test.py
```
This procedure will generate a *test_results* folder, with logs and three kind of **.obj** files:
1. GT files, which describes the Ground Truth.
2. PRED files, which are the results of training and testing; these files define what the network has learnt.
3. DIFF files, which highlight the difference between GT and PRED files.
You can open these files in Meshlab to visualize how the network has worked.

### Important

Generating your dataset it's really important that the sub-images have a similar structure to allow pointnet to do a good learning.

## Results
In this section, some results are shown. The mesaures for evaluate the process are **accuracy** and **IoU** ([intersection over union](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)).
These are the parameters selected:
- Epochs: 100
- Batch size: 4
- Points number: 512

For the image "EgyptFaceDense": 
- Accuracy: 74%
- IoU: 80%

![example](https://github.com/pisalore/Archeological-Textures-Segmentation/blob/master/doc/eyb%20(1).png)

In this image are shown the GT, PRED, and DIFF files.

### Papers, Documents and Links
Here there is a list of intersting materials used developing this project:
- [GitHub Pointnet page](https://github.com/charlesq34/pointnet)
- [Pointnet Introduction](http://stanford.edu/~rqi/pointnet/). See also [this page](https://arxiv.org/abs/1612.00593) for downloading related paper .
- [Shrec'18 Geometric Patterns Recognition](https://www.researchgate.net/publication/325166002_SHREC'18_track_Recognition_of_geometric_patterns_over_3D_models)
- [Representing 3D Texture on Mesh Manifolds for Retrieval and Recognition Applications](https://www.researchgate.net/publication/291522152_Representing_3D_Texture_on_Mesh_Manifolds_for_Retrieval_and_Recognition_Applications), a related work.
