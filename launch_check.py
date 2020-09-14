sign_4 = False

try:
    """Attempt to send file"""
    file = open('copy_data.zip')
    file.close()
    sign_4 = True
    
except FileNotFoundError:
    """If unable to find file, send a error email"""
    import launch_error_1
except PermissionError:
    """If permission of reading the file is denied，send a error email"""
    import launch_error_2
