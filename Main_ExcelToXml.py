# excel2xml.py

from clean_WB import *
from convert2xml import *
from deleteFile import *
from sendPost import *

# Loops in order to input mulitple POs
numPos = int(input('Number of POs entering: '))

for i in range(0, numPos):
# The xlsx should be saved by PO number only, no file extension.
    po = str(input('Enter PO number: '))


    poWorkbook = po + '.xlsx'
    date = date.today()
    xmlFile = f"alcon_fw_{po}_{date}.xml"


    clean_WB(poWorkbook)
    convert2xml('clean_wb.xlsx', po, date)
    sendPost(xml)
    deleteFile(poWorkbook, xmlFile)