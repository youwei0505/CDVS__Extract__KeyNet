import os 
import time
import shutil
import sys
from os import listdir
from os.path import isfile, isdir, join

# 2022/10/25，By 蔣有為
# 這份程式碼是將CDVS Extracted，自動進行Encode的動作，會產生 x.DB.cdvs檔案

# 列印出輸入列的參數，應該要帶入model的name+此程式碼所extract的點
print(len(sys.argv), str(sys.argv))
version_name = str(sys.argv[1])
print("version_name : ", version_name)
version_name = version_name.replace("\\", "/")
print("version_name : ", version_name)
# CDVS Extract 好的 x.DB.cdvs 檔案 資料夾
source_Dir = "F:\\CDVS\\__TestEnv\\__Extract__KeyNet\\" + version_name
print("source_Dir", source_Dir)
# 歷遍所有的source資料夾
source_Folders = listdir(source_Dir)

# annotations 檔案
annotations_file = "F:\\CDVS\\__TestEnv\\__Extract__KeyNet\\" + "annotations.txt"
print("annotations_file", annotations_file)


# 歷遍所有的 illum資料夾
for folder in source_Folders:
    print( "folder = ", folder )
    # print( "source_folder = ", source_Dir + "\\" + folder )
    print( "--------------------------------------------------------------------------")
    # # 每個資料夾中都會需要有annotations檔案
    # # 複製檔案    
    shutil.copy(annotations_file, source_Dir + "\\" + folder)
    # print(version_name + "\\" + folder)
    string = "extract__1101.exe annotations.txt 0 " + version_name + "/" + folder + " " + version_name + "/" + folder + " keynet_label.txt"
    print("cmd = ", string)
    cmd = os.system(string)
    # print( "--------------------------------------------------------------------------")
    # break

# # 歷遍所有的 view 資料夾
for folder in source_Folders:
    print( "folder = ", folder )
    # print( "source_folder = ", source_Dir + "\\" + folder )
    print( "--------------------------------------------------------------------------")
    # # 每個資料夾中都會需要有annotations檔案
    # # 複製檔案    
    shutil.copy(annotations_file, source_Dir + "\\" + folder)
    # print(version_name + "\\" + folder)
    string = "extract__1101 annotations.txt 0 " + version_name + "/" + folder + " " + version_name + "/" + folder + " keynet_label.txt"
    # print("cmd = ", string)
    cmd = os.system(string)
    # print( "--------------------------------------------------------------------------")
    # break