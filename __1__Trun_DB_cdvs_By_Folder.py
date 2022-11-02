import os 
import time
import shutil
import sys
from os import listdir
from os.path import isfile, isdir, join

# 2022/10/26，By 蔣有為
# 這份程式碼是

# Input
print(len(sys.argv),", " ,str(sys.argv))
version_name = str(sys.argv[1])
print("version_name : ", version_name)
# 列印出輸入列的參數，應該要帶入model的name+此程式碼所extract的點

# Source__KeyNet__Data
source_Dir = "F:\\CDVS\\__KeyNet__Data\\" + version_name
print("source_Dir", source_Dir)
source_Folders = listdir(source_Dir)
# 歷遍所有的source資料夾

# Target__Extract__Data 
target_Dir = "F:\\CDVS\\__TestEnv\\__Extract__KeyNet\\__KeyNet__Data\\" + version_name
# 如果Match資料夾中沒有當下的資料夾，則建立(shutil會需要用到)
if not os.path.exists(target_Dir):
    print("not exist target_Dir + ", target_Dir)
    # 建立一個新的資料夾
    os.mkdir(target_Dir)
print("target_Dir + ", target_Dir)

# print( "--------------------------------------------------------------------------")
# Processing
count = 1
# 歷遍所有的資料夾
for folder in source_Folders:    
    source_folder_Dir = source_Dir + "\\" + folder
    print( "folder ", count, " = " , folder )   
    print( "source_folder_Dir = ", source_folder_Dir )
    print( "target_Dir = ",        target_Dir ) 
    # 歷遍所有的資料夾中的資料夾
    source_Files = listdir(source_folder_Dir)       
    print( "source_Files = ",      source_Files )
    count = count + 1
    # print( "--------------------------------------------------------------------------")

    for file in source_Files:
        target_File = folder + "_" + file
        if file.endswith('kyp.txt') :
            # 複製檔案    
            shutil.copy(source_folder_Dir + "\\" + file, target_Dir + "\\" + target_File)   
        
# print( "--------------------------------------------------------------------------")
      
