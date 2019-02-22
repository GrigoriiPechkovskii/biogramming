#by Grigorii Pechkovskii
'''
The script to select the genome on the basis of their properties
'''
import os 
import os.path
import subprocess  
import shutil

import pandas as pd

#input data
genome_table = '/home/grigoriipechkovskii/Desktop/biogramming/genomics/test/genomes_proks.csv'
dir_in = '/home/grigoriipechkovskii/Desktop/biogramming/genomics/test/genome_in'
dir_out = '/home/grigoriipechkovskii/Desktop/biogramming/genomics/test/genome_out'
props = {'Level':'Complete Genome'}
props = {'Replicons':'pXO1'}#props = {'Replicons':'pXO1|pXO2'}

#path = os.path.abspath('genomes_proks.csv')
#genome_table = pd.read_csv(genome_table,engine='python')
#props = {'name':['1','2']}

def get_genome(genome_table,properties,name_access='Assembly'):
    '''Input genome table Otput list with acssesion or name genome with properties'''
    genome_table = pd.read_csv(genome_table,engine='python')
    for prop in properties:
        #index_choice = genome_table[prop] == properties[prop]
        index_choice = genome_table[prop].str.contains(properties[prop],)#!isin only list required
        
        return(list(genome_table[index_choice][name_access]))#!divide str !maybe yield

access_numbers = get_genome(genome_table,props)

for i in range(0,len(access_numbers)):
    access_numbers[i] = access_numbers[i].replace('GCA','GCF').strip()    

def distr_genome(dir_in,access_numbers,dir_out=''):
    '''Copy genome file with properties in dir_out'''
    os.mkdir(dir_out)
    files_in = os.listdir(dir_in)
    
    for access_number in access_numbers:
        for file_genome in files_in:
            if access_number in file_genome:                
                shutil.copy(dir_in+'/'+file_genome,dir_out+'/'+file_genome)
    
distr_genome(dir_in,access_numbers,dir_out)