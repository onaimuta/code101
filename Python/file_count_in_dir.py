import os
# counts multiplr files in directory and subdirectories 
count = 0
for root_dir, cur_dir, files in os.walk(r'C:\\Users\\HP\\OneDrive - Tragela\Desktop\\Projects\\code101\\Python\\'):
    count += len(files)
print('file count:', count)