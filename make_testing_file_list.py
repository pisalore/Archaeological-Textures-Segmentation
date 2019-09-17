import os
import glob

PTS_DIR = './data/pts_dir'
SEG_DIR = './data/seg_dir'

if not os.path.exists('./testing_ply_filelist.txt'):
    print('Writing test file list... \n' )
    f = open('testing_ply_filelist.txt', 'a')

    for path_file in glob.glob(os.path.join(PTS_DIR, '*.pts')):
        pts_file = os.path.basename(path_file)
        print(pts_file)
        seg_file = str(pts_file.split('.')[0]) + '.seg'
        print(seg_file)
        f.write('pts_dir/' + pts_file + ' ' + 'seg_dir/' + seg_file + '\n')

else:
    print('File already exists.')