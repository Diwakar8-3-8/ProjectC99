import os
import shutil
source=input("Enter the source name of the Folder:   ")
destination=input("Enter the destination name of the Folder:   ")

source=source + '/'
destination=destination + '/'

listOfFiles=os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)

