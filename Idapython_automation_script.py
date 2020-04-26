import os
import subprocess
import string

sam_list = os.listdir('sample path')
command = "C:\Program Files (x86)\IDA 6.9\idaq.exe -A -SC:\Python27\statically_extract_func.py C:\Lab09-01.exe"
command=command.split(' ')
#print command[6] #list index six's must chanded

print("Running...!")
for files in sam_list:
    command[6]=files

    subprocess.call("{path for idaq64.exe} -A -S{path for statically_extract_func.py} {sample path}\\%s" %command[6])

print("All done...!")
