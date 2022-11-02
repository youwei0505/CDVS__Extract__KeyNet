import os 
import time
import shutil
import sys
from os import listdir
from os.path import isfile, isdir, join

# 2022/11/02，By 蔣有為
# 這份程式碼是將hpatches-sequences-release(jpg)過濾出只有jpg的檔案


# Source__hpatches__Data
source_Dir = "hpatches-sequences-release(jpg)\\"
print("source_Dir", source_Dir)
source_Folders = listdir(source_Dir)

# __JPG__Data 
target_Dir = "F:__JPG\\"
if not os.path.exists(target_Dir):
    print("not exist target_Dir + ", target_Dir)
    # 建立一個新的資料夾
    os.mkdir(target_Dir)
print( "target_Dir = ", target_Dir ) 

# print( "--------------------------------------------------------------------------")
# Processing
count = 1
for folder in source_Folders:    
    source_folder_Dir = source_Dir + "\\" + folder
    # print( "folder ", count, " = " , folder )   
    print( "source_folder_Dir = ", source_folder_Dir )
    
    # 歷遍所有的資料夾中的資料夾
    source_files = listdir(source_folder_Dir)       
    print( "source_Files = ", source_files )
    count = count + 1

    for file in source_files:
        target_file = folder + "_" + file
        if file.endswith('.jpg'):
            # 複製檔案    
            shutil.copy( source_folder_Dir + "\\" + file, target_Dir + "\\" + target_file )   
        
# print( "--------------------------------------------------------------------------")
   
