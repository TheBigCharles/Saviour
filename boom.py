import os
import shutil

a = True
while (a == True):
    delList_1 = []
    delDir_1 = r"./copy_data"
    """Feedback: the list of the name of file/folder which contained within the folder"""
    delList_1 = os.listdir(delDir_1)

    for f_1 in delList_1:
        """Synthesis the path: stitching the catalog and filename"""
        filePath_1 = os.path.join(delDir_1, f_1 )

        """Determine the target path: whether it is a file"""
        if os.path.isfile(filePath_1): #判断目标路径下是否为文件
            os.remove(filePath_1)
            a = False
        elif os.path.isdir(filePath_1):
            shutil.rmtree(filePath_1, True)
            a = False


b = True
while (b == True):
    delList_2 = []
    delDir_2 = r"./data"
    delList_2 = os.listdir(delDir_2) 
    for f_2 in delList_2:
        filePath_2 = os.path.join(delDir_2, f_2 ) 
        if os.path.isfile(filePath_2): 
            os.remove(filePath_2)
            b = False
        elif os.path.isdir(filePath_2):
            shutil.rmtree(filePath_2, True)
            b = False
            
os.rmdir(delDir_1)
os.rmdir(delDir_2)

"""Delete files which left on this computer, as cleaning the trace"""
os.remove('copy_data.zip')

