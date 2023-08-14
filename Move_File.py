import os
import shutil

from_dir = "C:/Users/suvis/Downloads"
to_dir = "C:/Users/suvis/Desktop"

listOfFiles = os.listdir(from_dir)

for file_name in listOfFiles:
    name,ext = os.path.splitext(file_name)
    
    if ext == "":
        continue
    
    if ext in [".pdf"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Document_files"
        path3 = to_dir + "/" + "Document_files" + "/" + file_name
        
        
        if os.path.exists(path2):
            print("Moving " + file_name + "...")
            shutil.move(path1,path3)
        
        else:
            os.makedirs(path2)
            print("Moving " + file_name + "...")
            shutil.move(path1,path3)