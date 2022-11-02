import os 
import time
import shutil
import sys
from os import listdir
from os.path import isfile, isdir, join

# 2022/10/25，By 蔣有為
# 這份程式碼是將CDVS Extracted 並且 Encoded的內容搬到Match的資料夾中並且改成所需要的格式

# 列印出輸入列的參數，應該要帶入model的name+extract的點
print(len(sys.argv), str(sys.argv))
version_Name = str(sys.argv[1])
print("version_Name : ", version_Name)
# CDVS Extract 好的 x.DB.cdvs 檔案 資料夾
source_Dir="F:\\CDVS\\TestEnv\\CDVS_DB_Extract_Keynet\\" + version_Name
# CDVS Match 所需要的 x.DB.cdvs 檔案 資料夾
# target_Dir="F:\\CDVS\\TestEnv\\CDVS_DB_Extract_Keynet\\Move_Test"
target_Dir="F:\\CDVS\\TestEnv\\CDVS_DB_Match_Keynet\\" + version_Name
print(target_Dir)
# 如果Match資料夾中沒有當下的資料夾，則建立(shutil會需要用到)
if not os.path.exists(target_Dir):
    print("not exist target_Dir + ", target_Dir)
    # 建立一個新的資料夾
    os.mkdir(target_Dir)

# 歷遍所有的Extract中有的source資料夾(Hpatches)
source_Folders = listdir(source_Dir)
for file in source_Folders:
    # 歷遍所有的檔案
    # # 判斷 fullpath 是檔案還是目錄
    # if os.path.exists(folder_source_Dir + '\\' + file):
    #     print("檔案+")
    # else:
    #     print("資料夾-")
    # 只需要 x.DB.cdvs檔案
    if file.endswith('.DB.cdvs'):
        print("file", file)
        path1 = str(source_Dir + '\\' + file)
        print("path1", path1)
        path2 = str(target_Dir + '\\' + "keynet" + '_' + file)
        print("path2", path2)       
        # 複製檔案    
        shutil.copy(path1, path2)