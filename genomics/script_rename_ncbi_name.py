#script for rename stv and ncbi name
print('start')

import re
import pandas as pd

file = 'lef_c.aln'
table = 'genomes_proks.csv'

#with open('table') as table_opened:
table_read = pd.read_csv('genomes_proks.csv')
rep = table_read[table_read['Replicons']!='-'][['Replicons','Strain']]
rep.index = rep['Strain']
strain_dict = rep['Replicons'].to_dict()

for strain in strain_dict:
    pass
    #print(strain_dict[strain])


with open('lef_p.aln','a') as new_file_opened:
    with open(file) as file_opened:
        for file_line in file_opened:

            if '>' in file_line:                
                
                file_line = file_line.replace(":",'')
                file_line = file_line.replace('+','')
                file_line = file_line.replace("'",'')
                file_line = file_line.replace('%','')
                file_line = file_line.replace(',','')
                file_line = file_line.replace('|','')

                #result = re.findall(r'N._\w*',file_line)
                #print(result)
                result = re.search(r'N._[\w]*',file_line)#not full NZ id, del after dot
                result2 = re.search(r'stv[\w-]*',file_line)

                if result!=None:
                    #print(result.group(0))
                    for strain in strain_dict:                       
                        
                        if result.group(0) in strain_dict[strain]:
                            new_file_opened.write('>' + strain.replace(' ','_').replace(";",'') + ' ' + file_line[1:])
                
                elif result2!=None:#stv
                    strain_stv = result2.group(0).replace('stv_B_anthracis','stv').replace('str_','')
                    new_file_opened.write('>' + strain_stv + ' ' + file_line[1:])


                else:
                    new_file_opened.write(file_line)
            else:
                new_file_opened.write(file_line)

                
               

print('end')
