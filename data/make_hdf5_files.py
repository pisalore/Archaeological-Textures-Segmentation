import h5py
import numpy as np
import os
from plyfile import PlyData, PlyElement

HDF5_DATA = 'hdf5_data'

print('Generating .h5 files...', '\n')
if not os.path.exists(HDF5_DATA):
     os.mkdir(HDF5_DATA)

filenames_training = [line.rstrip() for line in open("filelist_training.txt", 'r')]
filenames_testing = [line.rstrip() for line in open("filelist_testing.txt", 'r')]
print((len(filenames_training)))
print((len(filenames_testing)))


f_training = h5py.File("./hdf5_data/data_training.h5", 'w')
f_testing = h5py.File("./hdf5_data/data_testing.h5", 'w')

a_data_training = np.zeros((len(filenames_training), 512, 3))
a_pid_training = np.zeros((len(filenames_training), 512), dtype = np.uint8)

a_data_testing = np.zeros((len(filenames_testing), 512, 3))
a_pid_testing = np.zeros((len(filenames_testing), 512), dtype = np.uint8)

for i in range(0, len(filenames_training)):
    print(filenames_training[i])
    plydata = PlyData.read("./ply_dir/" + filenames_training[i] + ".ply")
    piddata = [line.rstrip() for line in open("./seg_dir/" + filenames_training[i] + ".seg", 'r')]
    for j in range(0, 512):
        a_data_training[i, j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
        a_pid_training[i, j] = piddata[j]
data = f_training.create_dataset("data", data = a_data_training)
pid = f_training.create_dataset("pid", data = a_pid_training)


for i in range(0, len(filenames_testing)):
    plydata = PlyData.read("./ply_dir/" + filenames_testing[i] + ".ply")
    piddata = [line.rstrip() for line in open("./seg_dir/" + filenames_testing[i]  + ".seg", 'r')]
    for j in range(0, 512):
        a_data_testing[i, j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
        a_pid_testing[i, j] = piddata[j]
data = f_testing.create_dataset("data", data = a_data_testing)
pid = f_testing.create_dataset("pid", data = a_pid_testing)

print('HDF5 files generated.')