import zipfile
import os 

sign_3 = False

def compress():
    
    """Compress the folder which containing the files"""

    global sign_3

    """Create a new compression package，then put the files in it. If the compression already exist，cover it. Modal a can be use to continue adding contents"""
    azip = zipfile.ZipFile(r'./copy_data.zip', 'w')

    """The path must be guaranteed to exist, the algorithm of compression is LZMA"""
    azip.write(r'./copy_data', compress_type=zipfile.ZIP_LZMA)

    """put the files in it"""
    if os.path.isdir(r'./copy_data'):  
        for d in os.listdir(r'./copy_data'):  
            azip.write(r'./copy_data'+os.sep+d)  
            """close() is required"""
        azip.close()
        sign_3 = True
