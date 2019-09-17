import os
import glob

ALL_PLY_DIR = './data/all_ply_dir'

if not os.path.exists('./data/all_ply_dir/ply_filelist.txt'):
    print('Writing ply file list... \n' )
    f = open('./data/all_ply_dir/ply_filelist.txt', 'a')

    for path_file in glob.glob(os.path.join(ALL_PLY_DIR, '*.ply')):
        ply_file = os.path.basename(path_file)
        print(ply_file)
        f_len = open(path_file, 'r')
        num_lines = str(sum(1 for line in f_len) - 10)
        f.write(ply_file + ' '  + num_lines + '\n')

    print('File list obtained.')
else:
    print('File already exists.')
