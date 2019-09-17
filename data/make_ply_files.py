import scipy.io
import os
import glob

DATA_PROCESSED = 'Dataset_processed'
PLY_DIR = 'all_ply_dir'
# VERTEX_NUM = 6144
print('Converting .mat files to .ply file for pointClouds compatibility in Pointnet...', '\n')

if not os.path.exists(PLY_DIR):
     os.mkdir(PLY_DIR)

for mat_path_file in glob.glob(os.path.join(DATA_PROCESSED, '*.mat')):
    mat_file = os.path.basename(mat_path_file)
    file_name = str(mat_file.split('.')[0])
    ply_file_path = os.path.join(PLY_DIR, file_name + '.ply')
    if not os.path.exists(ply_file_path):
        print('Writing ply file converted from: ', mat_file)
        f = open(ply_file_path, "w+")
        f.seek(0)
        mat = scipy.io.loadmat(mat_path_file)
        vertex = mat['vertex']
        header = "ply\nformat ascii 1.0\ncomment VCGLIB generated\nelement vertex " + str(len(vertex)) + \
               "\nproperty float x\nproperty float y\nproperty float z\nelement " \
               "face 0\nproperty list uchar int vertex_indices\nend_header\n"
        f.write(header)
        for i in range(0, len(vertex)):
            f.write(' '.join(map(str, vertex[i])) + "\n")
    else:
        print('File: ', mat_file, 'already converted.')
    print('Conversion completed.')








