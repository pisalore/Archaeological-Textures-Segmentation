import scipy.io
import os
import glob

DATA_PROCESSED = 'Dataset_processed'
PTS_DIR = 'all_pts_dir'
# VERTEX_NUM = 6144
print('Converting .mat files to .pts file for pointClouds compatibility in Pointnet and testing...', '\n')

if not os.path.exists(PTS_DIR):
     os.mkdir(PTS_DIR)

for mat_path_file in glob.glob(os.path.join(DATA_PROCESSED, '*.mat')):
    mat_file = os.path.basename(mat_path_file)
    file_name = str(mat_file.split('.')[0])
    pts_file_path = os.path.join(PTS_DIR, file_name + '.pts')
    if not os.path.exists(pts_file_path):
        print('Writing pts file converted from: ', mat_file)
        f = open(pts_file_path, "w+")
        f.seek(0)
        mat = scipy.io.loadmat(mat_path_file)
        vertex = mat['vertex']
        for i in range(0, len(vertex)):
            f.write(' '.join(map(str, vertex[i])) + "\n")
    else:
        print('File: ', mat_file, 'already converted.')
    print('Conversion completed.')

