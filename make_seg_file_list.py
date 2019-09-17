import os
import glob

ALL_SEG_DIR = './data/all_seg_dir'

if not os.path.exists('./data/all_seg_dir/seg_filelist.txt'):
    print('Writing seg file list... \n' )
    f = open('./data/all_seg_dir/seg_filelist.txt', 'a')
    print('Writing seg file list... \n')

    for path_file in glob.glob(os.path.join(ALL_SEG_DIR, '*.seg')):
        seg_file = os.path.basename(path_file)
        print(seg_file)
        f_len = open(path_file, 'r')
        num_lines = str(sum(1 for line in f_len))
        f.write(seg_file + ' ' + num_lines + '\n')

    print('File list obtained.')
else:
    print('File already exists.')
