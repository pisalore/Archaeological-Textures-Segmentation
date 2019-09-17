import scipy.io
import os
import glob
import numpy as np

DATA_PROCESSED = 'Dataset_processed'
SHREC_18 = 'SHREK18_Labels'
SEG_DIR = 'all_seg_dir'

print('Converting .mat files to .seg file for pointClouds compatibility in Pointnet and testing...', '\n')

if not os.path.exists(SEG_DIR):
     os.mkdir(SEG_DIR)

for mat_path_file in glob.glob(os.path.join(DATA_PROCESSED, '*.mat')):
    # print(mat_path_file)
    mat_file = os.path.basename(mat_path_file)
    # print(mat_file)
    file_name = str(mat_file.split('.')[0])
    seg_file_path = os.path.join(SEG_DIR, file_name + '.seg')
    # print(seg_file_path)
    label_path_file = os.path.join(SHREC_18, file_name)
    print(label_path_file)
    if not os.path.exists(seg_file_path):
        print('Writing seg file converted from: ', mat_file)
        f = open(seg_file_path, "w+")
        f.seek(0)

        #loading facets current 3D shape
        mat1 = scipy.io.loadmat(mat_path_file)
        facets = mat1['face']
        # loading vertices current 3D shape
        vertices = mat1['vertex']
        #loading labels current 3D shape
        mat2 = scipy.io.loadmat(label_path_file)
        labels = mat2['label']

        vartices_labels = np.zeros((len(vertices) + 1, 1), dtype = np.uint8)
        # print(labels[0])
        # print(facets[0])
        # print(vertices[0])

        for j in range(0, len(facets)):
            vartices_labels[facets[j][0]] = int(labels[j])
            vartices_labels[facets[j][1]] = int(labels[j])
            vartices_labels[facets[j][2]] = int(labels[j])

        for i in range(vartices_labels.shape[0] - 1):
            f.write(' '.join(map(str, vartices_labels[i])) + "\n")

    else:
        print('File: ', mat_file, 'already converted.')
    print('Conversion completed.')


