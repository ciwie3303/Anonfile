
from anonfile import AnonFile
import os
import zipfile
import requests
import re

start_path = ""
start_path = '.'
anon = AnonFile()
def zipdir(start_path):
    dir_count = 0
    file_count = 0
    for (path,dirs,files) in os.walk(start_path):
        print('Directory: {:s}'.format(path))
        dir_count += 1
        for file in files:
            if file.endswith(".exe"): 
                file_path = os.path.join(path, file)
                print('\nAttempting to zip: \'{}\''.format(file_path))
                with zipfile.ZipFile(file_path + '.zip', 'w', zipfile.ZIP_DEFLATED) as ziph:
                    ziph.write(file_path, file)
                print('Done')
                file_count += 1
    print('\nProcessed {} files in {} directories.'.format(file_count,dir_count))

        


    for file in os.listdir():
        if file.endswith(".zip"):
            print('Загружаю архив ' + os.path.join(file))

            upload = anon.upload(f'{file}', progressbar=False)
            print(upload.url.geturl())

if __name__ == '__main__':
    zipdir(start_path)