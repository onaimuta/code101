from zipfile import ZipFile
import zipfile
with ZipFile("C:\\Users\\Onai Hector\\Desktop\\zipped\\30-data-types-testcases.zip", "r") as zipObj:

with ZipFile("C:\\Users\\Onai Hector\\Desktop\\zipped\\docker-nodejs-basic-demo.zip", "r") as zipObj:

with ZipFile("C:\\Users\\Onai Hector\\Desktop\\zipped\\docker-nodejs-basic-demo.zip", "r") as zipObj:
    zipObj.extractall("C:\\Users\\Onai Hector\\Desktop\\unzipped")
    print ("Done!")
#list of files that are zipped in the Zip file