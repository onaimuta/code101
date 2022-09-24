<<<<<<< HEAD
import os
from os.path import exists

dir_path = r"c:\\users\\onai hector\\desktop\\programming\\python\\"
file_exists = exists(dir_path)
file_to_purge = input("Filename:\n")

if os.path.exists(dir_path):
    os.chdir(dir_path)
    print (os.listdir(dir_path))
    print (file_to_purge)
    
    os.remove(file_to_purge)
    print ("File Purged")
else:
=======
import os
from os.path import exists

dir_path = r"C:\\Users\\Onai Hector\\Desktop\\code101\\Python\\"
file_exists = exists(dir_path)
file_to_purge = input("Filename:\n")

if os.path.exists(dir_path):
    os.chdir(dir_path)
    print (os.listdir(dir_path))
    print (file_to_purge)
    
    os.remove(file_to_purge)
    print ("File has been deleted successfully")
else:
>>>>>>> code102
    print("The system cannot find the file specified")