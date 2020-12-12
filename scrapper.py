import webbrowser
import gzip
import os
import glob
import re
import pandas as pd




f=gzip.open("/home/soumya/Documents/citybike/data_0_0_0.csv.gz",'rb')
file_content=f.read()
file_content=file_content.decode("utf-8")
#print(type(file_content))

file_content=int(file_content)
file_content=file_content+1

file_content=str(file_content)

#print(file_content)
#print(type(file_content))


webbrowser.open("http://dev.hsl.fi/citybikes/od-trips-"+file_content+"/od-trips-"+file_content+".zip")