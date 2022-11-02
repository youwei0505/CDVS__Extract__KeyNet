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
for folder in source_Folders:
    print(folder)
    # 產生資料夾的路徑
    folder_source_Dir = join(source_Dir, folder)
    folder_target_Dir = join(target_Dir, folder)
    print("folder_source_Dir", folder_source_Dir)
    print("folder_target_Dir", folder_target_Dir)

    # 歷遍所有的source資料夾中的所有檔案( *.jpg, *.DB.cdvs,... )
    files = listdir(folder_source_Dir)
    print(files)
    # 歷遍所有的檔案
    for file in files:
        # # 判斷 fullpath 是檔案還是目錄
        # if os.path.exists(folder_source_Dir + '\\' + file):
        #     print("檔案+")
        # else:
        #     print("資料夾-")
        # 只需要 x.DB.cdvs檔案
        if file.endswith('.DB.cdvs'):
            print("file", file)
            path1 = str(folder_source_Dir + '\\' + file)
            print("path1", path1)
            # path2 = str(folder_target_Dir + '\\' + folder+'_'+file)
            path2 = str(target_Dir + '\\' + "keynet" + '_' + folder + '_' + file)
            print("path2", path2)
            # 因在Match中，會將所有的檔案重新命名和集中
            # ---
            # # 如果沒有當下的資料夾，則建立(shutil會需要用到)
            # if not os.path.exists(folder_target_Dir):
            #     print("not exist folder + ", folder)
            #     # 建立一個新的資料夾
            #     os.mkdir(folder_target_Dir) 
            # ---
            # 複製檔案    
            shutil.copy(path1, path2)