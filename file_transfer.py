import shutil
import os
import glob
import re


###move the downloaded zip file to landing directory####

downloads="/home/soumya/Downloads/"

landing="/home/soumya/Documents/citybike/landing/"

file_name="od-trips-"

files=str(glob.glob(downloads+file_name+"*.zip"))

#print(files)

file=files.strip('[]')
file=re.sub(downloads,"",file)
file=file.strip("'")

#print(file)

#print(downloads+file)

shutil.move(downloads+file,landing+file)