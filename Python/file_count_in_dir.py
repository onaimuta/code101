import os
# counts multiplr files in directory and subdirectories 
count = 0
for root_dir, cur_dir, files in os.walk(r'C:\\Users\\Onai Hector\\Desktop\\work\\2021-22\\CLPA\\'):
    count += len(files)
print('file count:', count)