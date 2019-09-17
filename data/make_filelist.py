import os
import glob

FILES = './data/pts_dir'

if not os.path.exists('filelist.txt'):
    print('Writing filelist...\n')
    f = open('filelist.txt', 'a')

    for path_file in glob.glob(os.path.join(FILES, '*.pts')):
        file = os.path.basename(path_file)
        file_name = str(file.split('.')[0])
        f.write(file_name + '\n')
    print('Filelist created.')
else:
    print('filelist.txt already exists.')


