
import os, shutil

from pathlib import Path 

p = Path.cwd()
print(p)
print('the directory before:')
os.chdir('C:/Users/miart/Desktop/Python_Cusenza/Assignment_Nov22')
os.makedirs(p / 'copied_work')

for foldername, subfolders, filenames in os.walk('C:/Users/miart/Desktop/Python_Cusenza/Assignment_Nov22'):
    print('The current folder is ' + foldername)
    for subfolder in subfolders:
        print('subfolder of', foldername + ':', subfolder)
    for filename in filenames:
        print('File inside', foldername + ':', filename)
        print(' ')
    for filename in Path.cwd().glob('*.png'):
        print('Coping file...', filename)
        shutil.copy(filename, p / 'copied_work')
print(' ')