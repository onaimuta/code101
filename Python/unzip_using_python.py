from zipfile import ZipFile
import zipfile
with ZipFile("C:\\Users\\Onai Hector\\Desktop\\pics\Photos-003.zip", "r") as zipObj:
    zipObj.extractall("C:\\Users\\Onai Hector\\Desktop\\unzipped")
#list of files that are zipped in the Zip file