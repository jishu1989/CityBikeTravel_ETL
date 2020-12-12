import zipfile
import os
import glob
import re
import pandas as pd


landing="/home/soumya/Documents/citybike/landing/"


files=str(glob.glob(landing+"*.zip"))

#print(files)

file=files.strip('[]')
file=re.sub(landing,"",file)
file=file.strip("'")


year=re.sub("od-trips-","",file)
year=re.sub(".zip","",year)

#print(file)

#print(year)

#### file extraction #####

with zipfile.ZipFile(landing+file, 'r') as zip_ref:
    zip_ref.extractall(landing+year+'/')


##### file-integration #####

#path = r'file path'
path=landing+year+'/'                   
all_files = glob.glob(os.path.join(path, "*.csv"))     

# df_from_each_file = (pd.read_csv(f) for f in all_files)
# concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
# concatenated_df['Year']=year
# concatenated_df.to_csv(landing+year+".csv",index=False,header =0)

df_all_files=[]

for f in all_files:
	df_from_each_file=pd.read_csv(f)
	df_from_each_file['Month']=os.path.basename(f)
	df_from_each_file['Month']=df_from_each_file['Month'].map(lambda x: x.rstrip('.csv'))
	df_all_files.append(df_from_each_file)

concatenated_df = pd.concat(df_all_files, ignore_index=True)
concatenated_df['Year']=year
concatenated_df.to_csv(landing+year+".csv",index=False,header =0)

#print(df_all_files)




