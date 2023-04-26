import os

def deleteFile(poWorkbook, xmlFile):
    file = poWorkbook
    file2 = xmlFile
    location = 'C:\Program Files\Python310\ExcelToXml'
    path = os.path.join(location, file)
    path2 = os.path.join(location, file2)
    os.remove(path)
    os.remove(path2) ## Make active after all testing is complete
    print(f'{file} and {file2} have been removed successfully')