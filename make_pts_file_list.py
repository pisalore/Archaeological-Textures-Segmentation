import os
import glob

ALL_PTS_DIR = './data/all_pts_dir'

if not os.path.exists('./data/all_pts_dir/pts_filelist.txt'):
    print('Writing pts file list... \n' )
    f = open('./data/all_pts_dir/pts_filelist.txt', 'a')

    for path_file in glob.glob(os.path.join(ALL_PTS_DIR, '*.pts')):
        pts_file = os.path.basename(path_file)
        print(pts_file)
        f_len = open(path_file, 'r')
        num_lines = str(sum(1 for line in f_len))
        f.write(pts_file + ' '  + num_lines + '\n')

    print('File list obtained.')
else:
    print('File already exists.')
