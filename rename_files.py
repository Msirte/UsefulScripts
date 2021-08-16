import os
import csv
import pandas as pd


### 递归输出文件夹中的文件数目 ###
def print_filenum_recursive(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print("{0}\t{1}".format(root, len(files)))
        
        # 递归操作
        for dirname in dirs:
            sub_file_dir = os.path.join(root, dirname)
            print_filenum_recursive(sub_file_dir)

### 批量重命名文件 ###
def rename_filename(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for filename in files:
            # 文件名操作
            if filename.split('.')[-1] == 'MP4':
                new_filename = filename[:8] + ".MP4"
                old_full_filename = os.path.join(root, filename)
                new_full_filename = os.path.join(root, new_filename)
                os.rename(old_full_filename,new_full_filename)

### 批量重命名文件夹 ###
def rename_dirname(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for dirname in dirs:
            new_dirname = dirname[:8]
            old_full_dirname = os.path.join(root, dirname)
            new_full_dirname = os.path.join(root, new_dirname)
            os.rename(old_full_dirname, new_full_dirname)

### 递归批量重命名文件 ###
def rename_filename_recursive(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for filename in files:
            # 文件名操作
            new_filename = filename.replace(' ', '_')
            old_full_filename = os.path.join(root, filename)
            new_full_filename = os.path.join(root, new_filename)
            os.rename(old_full_filename, new_full_filename)
            
        # 递归操作
        for dirname in dirs:
            sub_file_dir = os.path.join(root, dirname)
            rename_filename_recursive(sub_file_dir)

### 递归批量提取文件名到list ###
def extract_filename_to_list_recursive(file_dir, filelist):
    for root, dirs, files in os.walk(file_dir):
        for filename in files:
            # 文件名操作
            full_filename = os.path.join(root, filename)
            filelist.append(full_filename)

        # 递归操作
        for dirname in dirs:
            sub_file_dir = os.path.join(root, dirname)
            extract_filename_to_list_recursive(sub_file_dir, filelist)


if __name__ == '__main__':
    folder_path = R"D:\202107海试数据\水下彩色图像增强数据集\彩色数据库"
    csv_filename = os.path.join(folder_path,"imgs.csv")
    filelist = []
    extract_filename_to_list_recursive(folder_path, filelist)

    # 将绝对路径转为相对路径
    relative_filelist = []
    for filename in filelist:
        relative_filelist.append(filename.replace(folder_path,'.'))

    df = pd.DataFrame(relative_filelist)
    df.to_csv(csv_filename,encoding='gbk',index=None,header=None)
    

