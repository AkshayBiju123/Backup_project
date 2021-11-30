import os
import shutil

prankingFile = input('Which file 1 you like to move')
destination = input('enter the destination folder')
source = 'source+'/''
destination = 'destination+'/''
list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.move((source+file), destination)
    shutil.move((source+file), prankingFile)