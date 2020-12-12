import shutil
import os
import re
import glob

landing="/home/soumya/Documents/citybike/landing/"

archive="/home/soumya/Documents/citybike/archive/"


files=str(glob.glob(landing+"*.zip"))

print(files)

file=files.strip('[]')
file=re.sub(landing,"",file)
file=file.strip("'")

print(file)


year=re.sub("od-trips-","",file)
year=re.sub(".zip","",year)


shutil.move(landing+year+'/', archive+year+'/')
shutil.move(landing+file, archive+file)
shutil.move(landing+year+'.csv', archive+year+'.csv')


