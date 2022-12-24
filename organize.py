import os
import shutil

from_dir = "C:/Users/Johan/Downloads"
to_dir = "C:Users/Johan/downloadedimages"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:

    name, extention = os.path.splitext(file_name)

    if extention == '':
        continue
    if extention in ['.gif','.png','.jpg','.jpeg','.jfif']:

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Image_Files"
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name




        if os.path.exists(path2):
            print("Moving"+ file_name+".....")

            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving"+file_name + ".....")
            shutil.move(path1,path3)


