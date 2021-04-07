import os
import shutil
path=input("Enter the source name of the Folder to be sorted:   ")

listOfFiles=os.listdir(path)
for file in listOfFiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=='':
        #continue-skip
        #break-stop
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
