from importlib.metadata import files
import os
import shutil
from unittest import result

def find_files (filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path): 
        if filename in files: 
            result.append(os.path.join(root, filename))
    return result
print (find_files("tutorial", "C:\\Users\\Onai Hector\\"))