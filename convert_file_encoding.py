import os
import chardet
import codecs


### 获取文件编码 ###
def get_encoding_type(filename):
    with open(filename, 'rb') as f:
        rawdata = f.read()
    return chardet.detect(rawdata)['encoding']

### 文件转码 ###
def convert_file_encoding(filename, to_codec):
    from_codec = get_encoding_type(filename)  # 获取文件编码
    if from_codec == to_codec:
        print("File '{0}''s Encoding is already '{1}'.".format(os.path.basename(filename), to_codec))
        return
    src_filename = filename
    dst_filename = filename + "_tmp"
    try: 
        with open(src_filename, 'r', encoding=from_codec) as f, open(dst_filename, 'w', encoding=to_codec) as e:
            text = f.read() # for small files, for big use chunks
            e.write(text)
        os.remove(src_filename) # remove old encoding file
        os.rename(dst_filename, src_filename)  # rename new encoding
        print("Converted '{0}' from '{1}' to '{2}'.".format(os.path.basename(src_filename),from_codec,to_codec))
    except UnicodeDecodeError:
        print("File '{0}' Decode Error.".format(os.path.basename(src_filename)))
    except UnicodeEncodeError:
        print("File '{0}' Encode Error.".format(os.path.basename(src_filename)))

### 递归批量将文件转码 ###
def convert_file_encoding_recrisive(file_dir, to_codec):
    for root, dirs, files in os.walk(file_dir):
        for filename in files:
            # 文件名操作
            if filename.lower().endswith('.h') or filename.lower().endswith('.cpp') or filename.lower().endswith('.hpp'):
                full_filename = os.path.join(root, filename)
                convert_file_encoding(full_filename, to_codec)

        # 递归操作
        for dirname in dirs:
            sub_file_dir = os.path.join(root, dirname)
            convert_file_encoding_recrisive(sub_file_dir, to_codec)


if __name__ == '__main__':
    folder_path = R"C:\Users\zhangyue\Documents\MyProject\MAISP"
    to_codec = 'utf-8'
    convert_file_encoding_recrisive(folder_path, to_codec)

