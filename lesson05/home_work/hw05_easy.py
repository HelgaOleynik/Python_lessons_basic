# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
#Create

import os

try:
    for idx in range(1, 10):
        os.mkdir("dir_" + str(idx))
except:
    print('Такая директория уже существует')
    

#Delete
try:
    for idx in range (1,10):
        os.rmdir("dir_" + str(idx))
    
except:
    print('Эта директория уже удалена')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

dirs = os.listdir()
current_dirs = [itm for itm in dirs if os.path.isdir(itm)]
print (current_dirs)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
import os

def copy_dir():
    shutil.copy(os.getcwd(), easy3_dupl.py)

