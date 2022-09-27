### References
# 1. http://pybrary.net/pyPdf/

import os
import glob
from pyPdf import PdfFileReader

parent = "C:\\Users\\Onai Hector\\Desktop\\pdf_page_count\\"
os.chdir(parent)
for infile in glob.glob(os.path.basename('*.pdf')):
    input = PdfFileReader(file(infile, "rb"))
    page_count = str(input.getNumPages())
    print "".join([infile, ",", page_count])