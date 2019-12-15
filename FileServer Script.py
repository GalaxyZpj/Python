import os
import shutil
from distutils.dir_util import copy_tree

copy_tree('/Users/pranavjain/Documents/Acadmics/Semester\ 4/Algorithms\ and\ Problem\ Solving', '/Users/pranavjain/Desktop/Pra')
e = os.scandir('/Users/pranavjain/Github/Python')
for x in e:
    i = x.stat()
    print(x.name, i.st_size)hi There!
#hutil.copytree('/Volumes/Computer Science & IT/Even Sem 2019/B.Tech/2nd Year/OOAD', '/Users/pranavjain/Desktop/Pra')