import wget
from zipfile import ZipFile
import os

class courseUtils:
    def __init__(self):
        super().__init__()


    def download(self, fileUrlPath,downloadFolder ):
        wget.download(fileUrlPath,downloadFolder)

    def unzipAndDelete(self, sourcePath, destFolder):
        with ZipFile(sourcePath, 'r') as zipObj:
              zipObj.extractall(destFolder)

        #Delete the zip file
        os.remove(sourcePath)

