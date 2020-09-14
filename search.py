import shutil,os,re

sign_2 = False

def search():
    """Find the file that has the desired suffix name and copy it into a new folder"""
    global sign_2
    """Create a new folder"""
    new_path='./copy_data'
    os.makedirs(new_path)
    """Find all the files that meeting the requirements recursively"""
    for derName, subfolders, filenames in os.walk('data'):
        #print(derName/subfolders/filenames)
        for i in range(len(filenames)):
            if (filenames[i].endswith('.txt')
                #or filenames[i].endswith('.xlsx')
                #or filenames[i].endswith('.ppt')
                #or filenames[i].endswith('.pptx')
                #or filenames[i].endswith('.xls')
                #or filenames[i].endswith('.doc')
                #or filenames[i].endswith('.docx')
                #or filenames[i].endswith('.pdf')
                #or filenames[i].endswith('.py')
                #or filenames[i].endswith('.jpg')
                #or filenames[i].endswith('.png')
                ):
                file_path = derName + '/' +filenames[i]
                shutil.copy(file_path, new_path)
                sign_2 = True
