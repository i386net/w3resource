# 49. Write a Python program to list all files in a directory in Python

import os

def list_files(path):
    file_list = []
    file_size = {}
    for file in os.listdir(path): # итерация по списку файлов
        full_path = os.path.join(path, file) # получаем полный путь до файла или директории
        if os.path.isfile(full_path): # если это файл, то поместить его в список
            file_list.append(file)
            try:
                file_size[file] = os.path.getsize(file)
            except FileNotFoundError:
                file_size[file] = None
    return file_list,file_size



fl = list_files('.')
l = max([len(k) for k in fl[1].keys()])

for f,s in fl[1].items():
    print('{:^{width}} size: {} bites'.format(f, s, width=l ))
