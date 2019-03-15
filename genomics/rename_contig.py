print('strart')

import os

files = os.listdir()
directory = os.getcwd()

os.mkdir(directory +'/rename/')

for file in files:
    if file.endswith('.fna'):

        with open(file) as file_opened:
            with open(directory +'/rename/'+ file[0:-4] + '_rename.fna','a') as file_rename:
                for file_line in file_opened:
                    if '>' in file_line:
                        file_rename.write('>' + 'stv_' + file[0:-4] +' '+ file_line[1:])
                    else:
                        file_rename.write(file_line)

print('end')
