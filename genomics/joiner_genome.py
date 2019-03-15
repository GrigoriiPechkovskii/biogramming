print('strart')

import os

files = os.listdir()

for file in files:
    if file.endswith('.fna'):
        with open('join_genome.fna','a') as join_files:
            with open(file,'r') as file_opened:
                join_files.write(file_opened.read())


print('end')
