'''Script extension mauve''' 

import os

print('start programm')

path = '/home/grigoriipechkovskii/Desktop/BA_re6'


def get_gbk(path_gbk):
    '''Function to get a list of absolue gbk path'''
    home_path = os.getcwd()
    os.chdir(path_gbk)
    path_gbk_file = os.listdir()
    gbk_abs_lst = list()
    for gbk in path_gbk_file:
        if gbk.endswith('.gbk'):
            gbk_abs_lst.append(os.path.abspath(gbk))
    #print(gbk_abs_lst)
    os.chdir(home_path)
    return gbk_abs_lst

path1 = get_gbk(path)[0]

class gbk():
    '''Class for work with genbank forman(gbk,gbff)'''
    def __init__(self,path):
        self.path = path
        
    def process(self):
        with open(self.path,'r') as gbk_opened:
            for gbk_line in gbk_opened:
                print(gbk_line)


#for gbk in gbk_abs_lst:



print('end programm','qwerty')
